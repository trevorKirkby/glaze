import bpy
from . node_group import load_node_group
from . lookup_material import lookup_material

class SetMaterialOperator(bpy.types.Operator):
    bl_idname = "view3d.set_material"
    bl_label = "Set Material"
    bl_description = "set the material for all selected objects"

    #bpy.props.FloatVectorProperty(size=4, subtype=‘COLOR_GAMMA’, min=0, max=1)
    #could use this to create dialogues to pick colors and other such properties

    material_options = dict()

    def execute(self, context):
        #print(dir(bpy.context.active_object.active_material))
        opt = context.scene.glaze_props
        material_type = opt.material_type
        material, options, postprocess = lookup_material(material_type)
        for obj in bpy.context.selected_objects:
            obj.active_material = material
            if "wire" in postprocess.keys() and postprocess["wire"] == True:
                obj.display_type = "WIRE"
            else:
                obj.display_type = "TEXTURED"
        self.__class__.material_options = options
        return {'FINISHED'}