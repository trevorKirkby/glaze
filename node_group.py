import bpy
import yaml
import collections

#TODO:
#   -Default values for node group inputs/outputs
#   -Parameters for internal nodes of node groups
#   -Better handling of a bad YAML file that may have been imported or altered

class flowmap(list): pass #A hack to make YAML look nicer, credit to https://stackoverflow.com/questions/14000893/specifying-styles-for-portions-of-a-pyyaml-dump
def flowmap_rep(dumper, data):
    return dumper.represent_sequence(u"tag:yaml.org,2002:seq", data, flow_style=True)
yaml.add_representer(flowmap, flowmap_rep)

def locify(pair):
    return flowmap([int(coord) for coord in list(pair)])

def load_node_group(source_file):
    with open(source_file, "r") as open_file:
        data = yaml.safe_load(open_file)

    group = bpy.data.node_groups.new(data["name"], "ShaderNodeTree")
    nodes = dict()

    group_inputs = group.nodes.new("NodeGroupInput")
    group_inputs.location = data["input"]["loc"]
    for group_input in data["input"]["inputs"]:
        group.inputs.new("NodeSocket"+group_input[0], group_input[1])
    nodes["input"] = group_inputs

    for name, node_data in data["nodes"].items():
        node = group.nodes.new(type="ShaderNode"+node_data["type"])
        node.location = node_data["loc"]
        nodes[name] = node
        for option, value in node_data.items():
            if option not in ["type", "loc", "defaults"]:
                node.__setattr__(option, value)
            if option == "defaults":
                for param in value:
                    node.inputs[param[0]].default_value = param[1]

    group_outputs = group.nodes.new("NodeGroupOutput")
    group_outputs.location = data["output"]["loc"]
    for group_output in data["output"]["outputs"]:
        group.outputs.new("NodeSocket"+group_output[0], group_output[1])
    nodes["output"] = group_outputs

    for outgoing_link in data["links"]:
        group.links.new(nodes[outgoing_link[0]].outputs[outgoing_link[1]], nodes[outgoing_link[2]].inputs[outgoing_link[3]])

    return group

def save_node_group(name, desc, node_group):
    data = dict()
    data["name"] = name
    data["desc"] = desc
    data["input"] = dict()
    data["output"] = dict()

    nodes_table = dict()
    nodes_counter = collections.Counter()
    for node in node_group.nodes:
        if node.type == "GROUP_INPUT":
            data["input"]["loc"] = locify(node.location)
        elif node.type == "GROUP_OUTPUT":
            data["output"]["loc"] = locify(node.location)
        else:
            nodes_table[node.bl_idname[10:]+str(nodes_counter[node.bl_idname[10:]])] = node
            nodes_counter[node.bl_idname[10:]] += 1

    data["input"]["inputs"] = []
    for input in node_group.inputs:
        data["input"]["inputs"].append(flowmap([input.bl_socket_idname[10:], input.name])) #input.name
    data["output"]["outputs"] = []
    for output in node_group.outputs:
        data["output"]["outputs"].append(flowmap([output.bl_socket_idname[10:], output.name]))
    
    data["nodes"] = dict()
    for node in nodes_table:
        #print(dir(nodes_table[node]))
        #print(nodes_table[node].bl_idname)
        data["nodes"][node] = dict()
        data["nodes"][node]["type"] = nodes_table[node].bl_idname[10:]
        data["nodes"][node]["loc"] = locify(nodes_table[node].location)
        '''
        special_attributes = [attribute for attribute in dir(nodes_table[node]) if attribute not in dir(bpy.types.ShaderNode)] #TODO: Only save special attributes that differ from their default values.
        for attribute in special_attributes:
            data["nodes"][node][attribute] = nodes_table[node].__getattribute__(attribute)
        data["nodes"][node]["defaults"] = []
        '''
        '''
        i = 0
        for input in nodes_table[node].inputs:
            if "default_value" not in dir(input): continue #Whatever these are, they don't have default values, and therefore do not concern this part of the program.
            try:
                yaml.safe_dump(input.default_value)
                data["nodes"][node]["defaults"].append([i, input.default_value]) #TODO: Again, only save these if they differ from the stock defaults.
            except yaml.representer.RepresenterError: #Quick way to identify if value can safely be serialized. Look into a better way to do this in the future.
                pass
            i += 1
        '''

    '''
    for node in node_group.nodes:
        for output in node_group.outputs:
            print(output)
            print(dir(output))
    '''

    with open("nodes/"+name+".yaml", "w") as open_file:
        #print(data)
        yaml.dump(data, open_file, sort_keys=False)