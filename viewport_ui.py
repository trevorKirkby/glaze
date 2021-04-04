import bpy
from . set_materials_operator import SetMaterialOperator

class ViewportPanel(bpy.types.Panel):
    bl_idname = "GLAZE_PT_Viewport_Panel"
    bl_label = "Glaze Viewport Panel"
    bl_category = "Glaze"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.glaze_props, "material_type", text="")
        #layout.prop(bpy.context.active_object.active_material, "diffuse_color")
        layout.row().separator()
        layout.operator("view3d.set_material", text = "Set Material")
        for key, value in SetMaterialOperator.material_options.items():
            layout.prop(value, "default_value", text=key)
        layout.row().separator()
        layout.operator("view3d.save_material", text = "Save Material to Library")
        layout.row().separator()
        layout.operator("view3d.quick_unwrap", text = "Quick Unwrap")