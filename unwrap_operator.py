import bpy
import bmesh

class UnwrapOperator(bpy.types.Operator):
    bl_idname = "view3d.quick_unwrap"
    bl_label = "Quick Unwrap"
    bl_description = "perform a rudimentary automatic UV unwrapping on the actively selected object"

    @classmethod
    def poll(cls, context):
        return bpy.context.active_object.mode == "OBJECT"

    def execute(self, context):
        obj = bpy.context.active_object
        
        mesh = obj.data

        bm = bmesh.new()
        bm.from_mesh(mesh)
        bm.edges.ensure_lookup_table()
        for edge in bm.edges:
            edge.seam = True
        bm.to_mesh(mesh)
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action = 'SELECT')
        bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
        bpy.ops.uv.pack_islands(rotate=True, margin=0.001)
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}