import bpy

class ViewportPanel(bpy.types.Panel):
    bl_idname = "GLAZE_PT_Viewport_Panel"
    bl_label = "Glaze Viewport Panel"
    bl_category = "Glaze"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("view3d.set_material", text = "Set Material")