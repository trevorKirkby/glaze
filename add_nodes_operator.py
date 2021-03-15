import bpy
from . node_group import load_node_group

#TODO: Create these nodes globally, so we do not ever need to make multiple instances of the same node group
#TODO: Make this setup from a YAML file or something, instead of writing code for each node
def create_node_group(context, operator, group_name):
    group = bpy.data.node_groups.new(group_name, "ShaderNodeTree")

    group_inputs = group.nodes.new("NodeGroupInput")
    group_inputs.location = (-300, 0)
    group.inputs.new("NodeSocketColor", "Color")
    group.inputs.new("NodeSocketFloat", "Scale")
    group.inputs.new("NodeSocketFloat", "Intensity")

    group_outputs = group.nodes.new("NodeGroupOutput")
    group_outputs.location = (300, 0)
    group.outputs.new("NodeSocketColor", "Color")

    noise_texture = group.nodes.new(type="ShaderNodeTexNoise")
    noise_texture.location = (-100, 200)

    rgb_mixer = group.nodes.new(type="ShaderNodeMixRGB")
    rgb_mixer.location = (100, 0)
    rgb_mixer.blend_type = "MULTIPLY"

    link = group.links.new #Todo: This process can be made even more DRY
    link(group_inputs.outputs["Color"], rgb_mixer.inputs["Color1"])
    link(group_inputs.outputs["Scale"], noise_texture.inputs["Scale"])
    link(group_inputs.outputs["Intensity"], rgb_mixer.inputs["Fac"])
    link(noise_texture.outputs["Fac"], rgb_mixer.inputs["Color2"])
    link(rgb_mixer.outputs["Color"], group_outputs.inputs["Color"])

    return group

class AddNodeOperator(bpy.types.Operator):
    bl_idname = "node.add_node_operator"
    bl_label = "Add Node Group"
    bl_description = "adds a custom node group to the shading panel"

    @classmethod
    def poll(cls, context):
        return context.active_object.active_material is not None

    def execute(self, context):
        #node_name = "Texturize"
        #node_group = create_node_group(self, context, node_name)
        node_group = load_node_group("nodes/texturize.yaml")
        material = context.active_object.active_material
        node = material.node_tree.nodes.new("ShaderNodeGroup")
        node.node_tree = bpy.data.node_groups[node_group.name]
        node.inputs["Intensity"].default_value = 0.5
        return {"FINISHED"}