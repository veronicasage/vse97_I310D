volume_of_sphere

import math

def calculate_volume_of_sphere(radius):
    volume = radius * radius * radius * math.pi * 4/3
    print("The volume of the sphere is", volume)

calculate_volume_of_sphere(30)
calculate_volume_of_sphere(40)