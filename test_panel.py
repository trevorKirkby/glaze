import bpy

class test_panel(bpy.types.Panel):
    bl_idname = "Test_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("view3d.cursor_center", text = "Center 3D Cursor")

class test_panel2(bpy.types.Panel):
    bl_idname = "Test_PT_Panel2"
    bl_label = "Test Panel 2"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("view3d.material_glowy", text = "Set Emission Shader")