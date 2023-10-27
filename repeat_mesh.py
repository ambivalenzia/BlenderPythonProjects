import bpy
import math

# create variables used in the loop
radius_step = 0.1
current_radius = 0.1
number_hexagon = 50
rotation_step = 10

# repeat
for i in range(number_hexagon):
    # add a hexagon mesh into the scene
    current_radius += radius_step
    bpy.ops.mesh.primitive_circle_add(vertices=6, radius=current_radius)

    # get a reference to the currently active object
    hexagon = bpy.context.active_object

    # rotate mesh around the x-axis
    hexagon.rotation_euler.x = math.radians(90)

    # rotate mesh around the z-axis
    hexagon.rotation_euler.z = i * math.radians(rotation_step)

    # convert mesh into a curve
    bpy.ops.object.convert(target='CURVE')

    # add bevel to curve
    hexagon.data.bevel_depth = 0.05
    bpy.context.object.data.bevel_resolution = 16

    # shade smooth
    bpy.ops.object.shade_smooth()