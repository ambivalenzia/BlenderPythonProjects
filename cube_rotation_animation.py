import bpy
import math

bpy.context.scene.frame_end = 180

# add a cube
bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

# insert keyframe at frame one
start_frame = 1
cube.keyframe_insert("rotation_euler", frame=start_frame)
bpy.context.scene.frame_current = 180

# change the rotation of the cube around x-axis
degrees_x = 720
radians = math.radians(degrees_x)
cube.rotation_euler.x = radians

# change the rotation of the cube around z-axis
degrees_z = 360
radians = math.radians(degrees_z)
cube.rotation_euler.z = radians

# insert keyframe at the last frame
end_frame = 180
cube.keyframe_insert("rotation_euler", frame=end_frame)

