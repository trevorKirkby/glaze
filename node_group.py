import bpy
import yaml

def load_node_group(source_file):
    with open(source_file, "r") as open_file:
        data = yaml.full_load(open_file)

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

def save_node_group(node_group):
    return