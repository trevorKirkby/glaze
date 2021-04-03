import bpy
import yaml
from os import listdir

'''
node_types = [
    ('TEXTURIZE', 'Texturize', "multiplicatively apply noise texture with color ramp"),
    ('GRAIN', 'Grain', "generate a basic grain pattern"),
    ('CRACKED', 'Cracked', "generate a basic cracked pattern"),
    ('IRIDESCENT', 'Iridescence', "apply an iridescent effect over a texture"),
    ('PRISMATIC', 'Prismatic Scattering', "apply prismatic scattering to a transparent texture"),
    ('CAUSTIC', 'Fake Caustics', "apply fake caustics to a transparent texture"),
]
'''

node_types = []
for node in listdir("nodes"):
    with open("nodes/"+node, "r") as infile:
        data = yaml.safe_load(infile)
    node_types.append((node, data["name"], data["desc"]))

class GlazeProperties(bpy.types.PropertyGroup):
    node_type : bpy.props.EnumProperty(
        name="Nodes",
        description="choose a node to add",
        items=node_types,
    )
    material_type : bpy.props.EnumProperty(
        name="Materials",
        description="choose a material to apply",
        items=[
            ("EMISSION", "Emission", ""),
            ("FOG", "Fog", ""),
            ("SOIL", "Soil", ""),
            ("METAL", "Metal", ""),
        ]
    )