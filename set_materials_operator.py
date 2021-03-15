import bpy

class SetMaterialOperator(bpy.types.Operator):
    bl_idname = "view3d.set_material"
    bl_label = "Set Material"
    bl_description = "set the material for all selected objects"

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            material = obj.active_material
            if material == None:
                material = bpy.data.materials.new(name = "Light Emission Shader")
                material.use_nodes = True
            material_output = material.node_tree.nodes.get('Material Output')
            emission = material.node_tree.nodes.new('ShaderNodeEmission')
            emission.inputs['Strength'].default_value = 5.0
            material.node_tree.links.new(material_output.inputs[0], emission.outputs[0])
            obj.active_material = material
        return {'FINISHED'}