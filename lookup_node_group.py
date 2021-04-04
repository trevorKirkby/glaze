from . node_group import load_node_group

loaded_node_groups = {}

def lookup_node_group(name):
    if name in loaded_node_groups.keys():
        return loaded_node_groups[name]
    else:
        loaded_node_groups[name] = load_node_group("nodes/"+name)
        return loaded_node_groups[name]