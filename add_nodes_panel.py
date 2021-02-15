import bpy

'''
class NodeSettings(bpy.types.PropertyGroup):
    node_type : bpy.types.EnumProperty(
        items=[
            ('TEXTURIZE', 'Texturize', "multiplicatively apply noise texture with color ramp"),
            ('GRAIN', 'Wood Grain', "generate a basic wood grain pattern"),
            ('IRIDESCENT', 'Iridescence', "apply an iridescent effect over a texture"),
            ('PRISMATIC', 'Prismatic Scattering', "apply prismatic scattering to a transparent texture"),
            ('CAUSTIC', 'Fake Caustics', "apply fake caustics to a transparent texture"),
        ],
        name="Nodes",
        description="add a node",
        default=None,
        options={'ANIMATABLE'},
        update=None,
        get=None,
        set=None,
    )
'''

class AddNodePanel(bpy.types.Panel):
    bl_idname = "AddNode_PT_Panel"
    bl_label = "Add Node"
    bl_category = "Glaze"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        #layout.prop(context.scene.prop_node_settings, "Nodes")
        layout.operator("node.add_node_operator", text = "Add Node")