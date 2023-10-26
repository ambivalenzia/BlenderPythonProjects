import bpy
import math
import random

def create_mesh():
    bpy.ops.mesh.primitive_cube_add()

    obj = bpy.context.active_object #same as bpy.context.object

    obj.scale.x = obj.scale.x * 0.5
    obj.scale.y = obj.scale.y * 2
    obj.scale.z = obj.scale.z * 0.1

    # apply random rotation
    random_rotation = random.uniform(0, 360)
    obj.rotation_euler.z = math.radians(random_rotation)

    bpy.ops.object.transform_apply()

    return obj

def animate_rotation(obj, current_frame, rotation_frame_count, clockwise):
    # remove the animation data from the duplicated object
    obj.animation_data_clear()

    # insert keyframe
    obj.keyframe_insert("rotation_euler", frame = current_frame)

    # rotate object
    if clockwise:
        angle = -360
    else:
        angle = 360
    obj.rotation_euler.z += math.radians(angle)

    # calculate the end frame
    frame = current_frame + rotation_frame_count

    # insert key frame
    obj.keyframe_insert("rotation_euler", frame = frame)

def create_next_layer(angle_step, current_frame, rotation_frame_count, clockwise):
    # duplicate the mesh
    bpy.ops.object.duplicate(linked=True)

    # get a reference to the currently active object
    obj = bpy.context.active_object

    # update transform
    update_obj_transform(obj, angle_step)

    animate_rotation(obj, current_frame, rotation_frame_count, clockwise)


    
def update_obj_transform(obj, angle_step):
    obj.location.z += obj.dimensions.z
    obj.rotation_euler.z += math.radians(angle_step)

    

def main():
    obj = create_mesh()
    
    angle_step = 3
    count = int(360 / angle_step)

    current_frame = 1
    frame_step = 1
    rotation_frame_count = 90

    clockwise = True

    # rotate first mesh
    animate_rotation(obj, current_frame, rotation_frame_count, clockwise)


    for i in range(count):

        clockwise = not clockwise
        create_next_layer(angle_step, current_frame, rotation_frame_count, clockwise)

        current_frame += frame_step

    bpy.context.scene.frame_end = current_frame + rotation_frame_count

        


main()
