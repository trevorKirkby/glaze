import bpy

class test_operator(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple Test Operator"
    bl_description = "A simple test operator that puts the cursor in the center of the screen"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}

class test_operator2(bpy.types.Operator):
    bl_idname = "view3d.material_glowy"
    bl_label = "Simple Test Operator 2"
    bl_description = "A simple test operator that sets the material for all selected objects"

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