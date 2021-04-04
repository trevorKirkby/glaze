import bpy
import os
from . material import save_material

class SaveMaterialOperator(bpy.types.Operator):
    bl_idname = "view3d.save_material"
    bl_label = "Save Material to Library"
    bl_description = "save a custom material of a selected object so you can access it in future projects"

    material_name = bpy.props.StringProperty(name="Material Name", default="")
    material_desc = bpy.props.StringProperty(name="Material Description", default="")

    @classmethod
    def poll(cls, context):
        return bpy.context.active_object.active_material.use_nodes == True

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        save_material(self.material_name, self.material_desc, context.active_object.active_material.node_tree)
        #context.scene.glaze_props.node_type.items.append((self.group_name.lower(), self.group_name, self.group_desc)) #IF this doesnt work maybe just make a method to load/reload the property group?
        return {"FINISHED"}
