"""
From the book "The algorithmic beauty of plants": http://algorithmicbotany.org/papers/abop/abop-ch4.pdf
Phyllotaxis in Polar Coordinates: alpha = n * 137.5deg, r = const * sqrt(n)
Phyllotaxis in Cartesisan Coordinates: 
cos(alpha) = x / r -> x = r * cos(alpha)
sin(alpha) = y / r -> y = r * sin(alpha)
"""

import bpy
import random
import math

# c in formula
scale_fac = 0.2

# angle alpha
angle = 137.508

count = 300

for n in range(count):
    alpha = n * angle
    r = scale_fac * math.sqrt(n)

    x = r * math.cos(alpha)
    y = r * math.sin(alpha)

    bpy.ops.mesh.primitive_ico_sphere_add(radius=0.05, location=(x, y, 0))
