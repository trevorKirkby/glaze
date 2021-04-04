#A hack to make YAML representation more human-friendly, credit to https://stackoverflow.com/questions/14000893/specifying-styles-for-portions-of-a-pyyaml-dump

import yaml

class flowmap(list): pass

def serialize(sequence):
    return flowmap([int(coord) if coord%1==0 else coord for coord in list(sequence)])

def flowmap_rep(dumper, data):
    return dumper.represent_sequence(u"tag:yaml.org,2002:seq", data, flow_style=True)

yaml.add_representer(flowmap, flowmap_rep)