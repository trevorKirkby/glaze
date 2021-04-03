import bpy
import os
from . node_group import save_node_group

class SaveNodeOperator(bpy.types.Operator):
    bl_idname = "node.save_node_operator"
    bl_label = "Save Node Group to Library"
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
        #context.scene.glaze_props.node_type.items.append((self.group_name.lower(), self.group_name, self.group_desc)) #IF this doesnt work maybe just make a method to load/reload the property group?
        return {"FINISHED"}

'''
class DeleteNodeOperator(bpy.types.Operator):
    bl_idname = "node.delete_node_operator"
    bl_label = "Delete Node Group from Library"
    bl_description = "delete a node group from the library"

    def execute(self, context):
        options = context.scene.glaze_props
        os.remove("nodes/"+options.node_type.lower())
        context.scene.glaze_props.node_type.items.remove((self.group_name.lower(), self.group_name, self.group_desc))
        return {"FINISHED"}
'''