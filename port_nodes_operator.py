'''
import bpy
from . node_group import load_node_group, save_node_group

class ImportNodeOperator(bpy.types.Operator):
    bl_idname = "node.import_node_operator"
    bl_label = "Import Node Group into Library"
    bl_description = "save a custom node group so you can access it in future projects"

    group_name = bpy.props.StringProperty(name="Node Group Name", default="")
    group_desc = bpy.props.StringProperty(name="Node Group Description", default="")

    @classmethod
    def poll(cls, context):
        return hasattr(context.active_node, "node_tree")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        material = context.active_object.active_material
        save_node_group(self.group_name, self.group_desc, context.active_node.node_tree)
        context.scene.glaze_props.node_type.items.append((self.group_name.lower(), self.group_name, self.group_desc))
        return {"FINISHED"}
'''