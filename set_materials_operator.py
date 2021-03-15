import bpy
from . node_group import load_node_group

'''
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
'''

class SetMaterialOperator(bpy.types.Operator):
    bl_idname = "view3d.set_material"
    bl_label = "Set Material"
    bl_description = "set the material for all selected objects"

    def execute(self, context):
        options = context.scene.glaze_props
        material_type = options.material_type
        if material_type == "EMISSION": #Make this more DRY, can probably save materials in YAML format as well once there is a better way to serialize Blender objects.
            material = bpy.data.materials.new(name = "Light Emission Shader")
            material.use_nodes = True
            material.node_tree.nodes.remove(material.node_tree.nodes['Principled BSDF'])
            material_output = material.node_tree.nodes.get('Material Output')
            emission = material.node_tree.nodes.new('ShaderNodeEmission')
            emission.inputs['Strength'].default_value = 5.0
            material.node_tree.links.new(material_output.inputs[0], emission.outputs[0])
        elif material_type == "FOG":
            material = bpy.data.materials.new(name = "Fog Shader")
            material.use_nodes = True
            material.node_tree.nodes.remove(material.node_tree.nodes['Principled BSDF'])
            material_output = material.node_tree.nodes.get('Material Output')
            volume = material.node_tree.nodes.new('ShaderNodeVolumePrincipled')
            volume.inputs['Density'].default_value = 0.5
            material.node_tree.links.new(material_output.inputs[1], volume.outputs[0])
        elif material_type == "SOIL":
            material = bpy.data.materials.new(name = "Soil Shader")
            material.use_nodes = True
            material.node_tree.nodes.remove(material.node_tree.nodes['Principled BSDF'])
            material_output = material.node_tree.nodes.get('Material Output')
            volume = material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
            volume.inputs['Roughness'].default_value = 1
            node_group = load_node_group("nodes/texturize.yaml")
            texnode = material.node_tree.nodes.new("ShaderNodeGroup")
            texnode.node_tree = bpy.data.node_groups[node_group.name]
            texnode.inputs['Color'].default_value = (0.1657115, 0.1024018, 0.0638535, 1)
            texnode.inputs['Scale'].default_value = 7
            texnode.inputs['Intensity'].default_value = 1
            texnode2 = material.node_tree.nodes.new("ShaderNodeGroup")
            texnode2.node_tree = bpy.data.node_groups[node_group.name]
            texnode2.inputs['Scale'].default_value = 30
            texnode2.inputs['Intensity'].default_value = 0.9
            material.node_tree.links.new(texnode2.inputs[0], texnode.outputs[0])
            material.node_tree.links.new(volume.inputs[0], texnode2.outputs[0])
            material.node_tree.links.new(material_output.inputs[0], volume.outputs[0])
        elif material_type == "METAL":
            material = bpy.data.materials.new(name = "Metal Shader")
            material.use_nodes = True
            material.node_tree.nodes.remove(material.node_tree.nodes['Principled BSDF'])
            material_output = material.node_tree.nodes.get('Material Output')
            principled = material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
            principled.inputs[4].default_value = 1
            node_group = load_node_group("nodes/texturize.yaml")
            texnode = material.node_tree.nodes.new("ShaderNodeGroup")
            texnode.node_tree = bpy.data.node_groups[node_group.name]
            texnode.inputs['Color'].default_value = (0.7, 0.7, 0.7, 1)
            texnode.inputs['Scale'].default_value = 70
            texnode.inputs['Intensity'].default_value = 1
            material.node_tree.links.new(principled.inputs[7], texnode.outputs[0])
            material.node_tree.links.new(material_output.inputs[0], principled.outputs[0])
        for obj in bpy.context.selected_objects:
            obj.active_material = material
            if material_type == "FOG":
                obj.display_type = "WIRE"
            else:
                obj.display_type = "TEXTURED"
        return {'FINISHED'}