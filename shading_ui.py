import bpy

class NodeMenu(bpy.types.Menu):
    bl_idname = "GLAZE_MT_NodeType_Menu"
    bl_label = "Node Type"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_node_operator", text = "Add Textured Node")

class ShadingPanel(bpy.types.Panel):
    bl_idname = "GLAZE_PT_Shading_Panel"
    bl_label = "Glaze Shading"
    bl_category = "Glaze"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.glaze_props, "node_type", text="") 
        layout.operator("node.add_node_operator", text = "Add Node Group")
        layout.row().separator()
        layout.operator("node.save_node_operator", text = "Save Node Group to Library")