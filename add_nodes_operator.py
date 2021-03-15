import bpy
from . node_group import load_node_group

class AddNodeOperator(bpy.types.Operator):
    bl_idname = "node.add_node_operator"
    bl_label = "Insert Node Group"
    bl_description = "adds a custom node group to the shading panel"

    @classmethod
    def poll(cls, context):
        return context.active_object.active_material is not None

    def execute(self, context):
        options = context.scene.glaze_props
        node_group = load_node_group("nodes/"+options.node_type.lower())
        material = context.active_object.active_material
        node = material.node_tree.nodes.new("ShaderNodeGroup")
        node.node_tree = bpy.data.node_groups[node_group.name]
        return {"FINISHED"}