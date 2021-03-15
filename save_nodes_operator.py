import bpy
from . node_group import save_node_group

class SaveNodeOperator(bpy.types.Operator):
    bl_idname = "node.save_node_operator"
    bl_label = "Save Node Group to Library" #TODO: There also has to be an operator for deleting node groups from a library, and ideally one for loading a YAML file into library, or exporting a library entry as a YAML file you can send to other people.
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
        return {"FINISHED"}