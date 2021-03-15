import bpy

class prop_material_id(bpy.types.PropertyGroup):
    material_id : bpy.props.IntProperty(
        name="materialid",
        description="an integer that represents a choice of material",
        default=1,
        min=1,
        max=5,
    )

class operator_set_material(bpy.types.Operator):
    bl_idname = "view3d.set_material"
    bl_label = "Set Material"
    bl_description = "an operator that sets the material of one or more selected objects"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        props = context.scene.prop_material_id
        if props.material_id == 1:
            material = bpy.data.materials.new(name = "Light Emission Shader") #Todo: Have these materials instantiated somewhere else, globally.
            material.use_nodes = True
            material_output = material.node_tree.nodes.get("Material Output")
            emission = material.node_tree.nodes.new("ShaderNodeEmission")
            emission.inputs["Strength"].default_value = 5.0
            material.node_tree.links.new(material_output.inputs[0], emission.outputs[0])
        else:
            material = bpy.data.materials.new(name = "Reflective Metal Shader")
            material.use_nodes = True
            material_output = material.node_tree.nodes.get("Material Output")
            metal = material.node_tree.nodes.new("ShaderNodeBsdfPrincipled")
            metal.inputs["Metallic"].default_value = 1
            metal.inputs["Roughness"].default_value = 0
            material.node_tree.links.new(material_output.inputs[0], metal.outputs[0])
        for obj in bpy.context.selected_objects:
            obj.active_material = material
        return {'FINISHED'}

class panel_set_material(bpy.types.Panel):
    bl_idname = "panel_set_material"
    bl_label = "Glaze"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        #layout.prop(context.scene.prop_material_id, "materialid", text="Material Property")
        props = context.scene.prop_material_id
        row = layout.row()
        row.prop(props, "materialid")
        row = layout.row()
        row.operator("view3d.set_material", text = "Set Material")