# give python to Blender's functionality
import bpy

# add a cube into the scene
bpy.ops.mesh.primitive_cube_add()

# get a reference to the currently active object
cube = bpy.context.active_object

# change the location of the cube on all-axis
cube.location = (-2,-1,4)

# insert keyframe at frame one
start_frame = 1
cube.keyframe_insert("location", frame = start_frame)

# change the location of the cube on the all-axis
cube.location = (1,2,3)

# mid frame
mid_frame = 90
cube.keyframe_insert("location", frame = mid_frame)

# change the location of the cube on the all-axis
cube.location = (-5,3,-1)


# insert keyframe at the last frame
last_frame = 180
cube.keyframe_insert("location", frame = last_frame)

