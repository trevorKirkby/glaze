import bpy

class ViewportPanel(bpy.types.Panel):
    bl_idname = "GLAZE_PT_Viewport_Panel"
    bl_label = "Glaze Viewport Panel"
    bl_category = "Glaze"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.glaze_props, "material_type", text="") 
        layout.operator("view3d.set_material", text = "Set Material")
        layout.operator("view3d.quick_unwrap", text = "Quick Unwrap")