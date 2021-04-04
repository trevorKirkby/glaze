from . material import load_material

loaded_materials = {}

def lookup_material(name):
    if name in loaded_materials.keys():
        return loaded_materials[name]
    else:
        loaded_materials[name] = load_material("materials/"+name)
        return loaded_materials[name]