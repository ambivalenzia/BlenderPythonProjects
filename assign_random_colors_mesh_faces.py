import bpy
import bmesh    # important: bmesh gets destroyed when exiting edit mode
import random

def get_random_color():
    """generate a random color"""
    red = random.random()
    green = random.random()
    blue = random.random()
    alpha = 1.0
    color = (red, green, blue , alpha)
    return color

def generate_random_color_materials(obj, count):
    """create and assign materials to the object"""
    for i in range(material_count):
        
        # create a new material
        mat = bpy.data.materials.new(f"material_{i}")
        mat.diffuse_color = get_random_color()

        # add the material to the object
        obj.data.materials.append(mat)

def add_ico_sphere():
    """add ico sphere"""
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3)
    return bpy.context.active_object

def assign_materials_to_faces(obj):
    """iterates over all the faces of the object and assigns a random material to the face"""
    # turn ON edit mode
    bpy.ops.object.editmode_toggle()

    # deselect all faces
    bpy.ops.mesh.select_all(action='DESELECT')

    # get geometry data from mesh object
    bmesh_obj = bmesh.from_edit_mesh(obj.data)

    material_count = len(obj.data.materials)

    # iterate through each face of the mesh
    for face in bmesh_obj.faces:

        # set active material
        ico_object.active_material_index = random.randint(0, material_count)

        # select the face and assign the active material
        face.select = True
        bpy.ops.object.material_slot_assign()
        face.select = False

    # turn OFF edit mode
    bpy.ops.object.editmode_toggle()

ico_object = add_ico_sphere()

# create a variable for holding the number of materials to create
material_count = 30

generate_random_color_materials(ico_object, material_count) 

assign_materials_to_faces(ico_object)

