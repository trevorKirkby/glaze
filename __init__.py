# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

from . property_group import GlazeProperties

from . unwrap_operator import UnwrapOperator

from . add_nodes_operator import AddNodeOperator
from . save_nodes_operator import SaveNodeOperator
from . shading_ui import NodeMenu, ShadingPanel

from .save_material_operator import SaveMaterialOperator
from . set_materials_operator import SetMaterialOperator
from . viewport_ui import ViewportPanel

bl_info = {
    "name" : "glaze",
    "author" : "tkirkby",
    "description" : "A simple add-on to streamline shading and texturing objects in Blender 2.8+",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

classes = (GlazeProperties, UnwrapOperator, AddNodeOperator, SaveNodeOperator, NodeMenu, ShadingPanel, SaveMaterialOperator, SetMaterialOperator, ViewportPanel)

def register():
    for bpy_class in classes:
        bpy.utils.register_class(bpy_class)
    bpy.types.Scene.glaze_props = bpy.props.PointerProperty(type=GlazeProperties)

def unregister():
    for bpy_class in classes:
        bpy.utils.unregister_class(bpy_class)
    del bpy.types.Scene.glaze_props