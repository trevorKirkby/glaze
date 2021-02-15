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
from . test_operator import test_operator, test_operator2
from . test_panel import test_panel, test_panel2

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

#def register():
#    ...

#def unregister():
#    ...

classes = (test_operator, test_operator2, test_panel, test_panel2)

register, unregister = bpy.utils.register_classes_factory(classes)