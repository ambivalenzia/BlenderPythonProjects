import bpy
import math
import pprint   # pretty print

def get_circle_vert_coordinates(vert_count, radius):


    vert_coordinates = list()

    # calculate coordinates
    for i in range(vert_count):
        angle_step = 2 * math.pi / vert_count

        current_angle = i * angle_step
        x = radius * math.cos(current_angle)
        y = radius * math.sin(current_angle)

        # visualize what is done
        # bpy.ops.mesh.primitive_ico_sphere_add(radius=0.1, location=(x, y, 0))

        vert_coordinates.append((x, y, 0))

    pprint.pprint(vert_coordinates)

    return vert_coordinates

def create_circle(vert_coordinates, vert_count):
    # define lists for the verts, edges, and faces
    verts = vert_coordinates
    edges = []

    for i in range(vert_count - 1):
        current_vert_index = i
        next_vert_index = i + 1
        edges.append((current_vert_index, next_vert_index))

    edges.append((vert_count - 1, 0))

    faces = []

    # create mesh data from the vert, edge, and face data
    mesh_data = bpy.data.meshes.new("circle_data")
    mesh_data.from_pydata(verts, edges, faces)

    # create an object using the mesh data
    mesh_obj = bpy.data.objects.new("circle_obj", mesh_data)

    # add the object to the scene collection
    bpy.context.collection.objects.link(mesh_obj)

    return mesh_obj

# initialize parameters
vert_count = 32
radius = 2

vert_coordinates = get_circle_vert_coordinates(vert_count, radius)

mesh_obj = create_circle(vert_coordinates, vert_count)
mesh_obj.rotation_euler.x = math.radians(90)