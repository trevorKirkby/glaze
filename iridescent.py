import bpy
from . node_group import load_node_group

#TODO: Create these nodes globally, so we do not ever need to make multiple instances of the same node group
def create_iridescent_group(context, operator, group_name):
    group = bpy.data.node_groups.new(group_name, "ShaderNodeTree")

    group_inputs = group.nodes.new("NodeGroupInput")
    group_inputs.location = (0, 0)
    group.inputs.new("NodeSocketColor", "Color")
    group.inputs.new("NodeSocketFloat", "Scale")
    group.inputs.new("NodeSocketFloat", "Intensity")

    group_outputs = group.nodes.new("NodeGroupOutput")
    group_outputs.location = (1200, 0)
    group.outputs.new("NodeSocketColor", "Color")

    camera_data = group.nodes.new(type="ShaderNodeCameraData")
    camera_data.location = (200, 200)

    texture_coordinate = group.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate.location = (200, -200)

    cross_product = group.nodes.new(type="ShaderNodeVectorMath")
    cross_product.location = (400, 0)
    cross_product.operation = "CROSS_PRODUCT"

    noise_texture = group.nodes.new(type="ShaderNodeTexNoise")
    noise_texture.location = (600, 0)
    noise_texture.inputs[3].default_value = 16
    noise_texture.inputs[5].default_value = 6

    hsv_adjust = group.nodes.new(type="ShaderNodeHueSaturation")
    hsv_adjust.location = (800, 0)
    hsv_adjust.inputs[1].default_value = 2

    layer_weight = group.nodes.new(type="ShaderNodeLayerWeight")
    layer_weight.location = (800, 200)

    rgb_mixer = group.nodes.new(type="ShaderNodeMixRGB")
    rgb_mixer.location = (1000, 0)

    link = group.links.new #Todo: This process can be made even more DRY
    link(group_inputs.outputs["Color"], rgb_mixer.inputs["Color1"])
    link(group_inputs.outputs["Scale"], noise_texture.inputs["Scale"])
    link(group_inputs.outputs["Intensity"], layer_weight.inputs[0])

    link(camera_data.outputs[0], cross_product.inputs[0])
    link(texture_coordinate.outputs[1], cross_product.inputs[1])
    link(cross_product.outputs[0], noise_texture.inputs[0])
    link(noise_texture.outputs[1], hsv_adjust.inputs[4])
    link(hsv_adjust.outputs[0], rgb_mixer.inputs[2])
    link(layer_weight.outputs[1], rgb_mixer.inputs[0])

    link(rgb_mixer.outputs["Color"], group_outputs.inputs["Color"])

    return group

class AddIridescentNodeOperator(bpy.types.Operator):
    bl_idname = "node.add_iridescent_operator"
    bl_label = "Add Iridescent Node Group"
    bl_description = "adds a custom node group to the shading panel"

    @classmethod
    def poll(cls, context):
        return context.active_object.active_material is not None

    def execute(self, context):
        #node_name = "Iridescence"
        #node_group = create_iridescent_group(self, context, node_name)
        node_group = load_node_group("nodes/iridescent.yaml")
        material = context.active_object.active_material
        node = material.node_tree.nodes.new("ShaderNodeGroup")
        node.node_tree = bpy.data.node_groups[node_group.name]
        node.inputs["Scale"].default_value = 1
        node.inputs["Intensity"].default_value = 0.2
        return {"FINISHED"}