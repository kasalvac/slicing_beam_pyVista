# Working one slice
import numpy as np
import pyvista as pv

# Load the STL file
mesh = pv.read('Rechteckrohr_verjuengt_Volumen.stl')
# mesh.plot() #plot the original mesch

# Define the origin and normal vector for the slicing plane
origin = np.array([100, 0, 0])  # Origin of the plane
normal = np.array([1, 0, 0], dtype=float)  # Normal vector of the plane (z-direction) + ensuring format is float for np

# Make sure the normal vector is normalized
normal /= np.linalg.norm(normal)

# Define a point on the plane
point_on_plane = origin + normal  # You can adjust this to position the plane as needed

# Make the slice
sliced_mesh = mesh.slice(normal=normal, origin=origin)

# Get the coordinates of all points in the mesh
points = sliced_mesh.points

# Calculate the dimensions
x_min, x_max = points[:, 0].min(), points[:, 0].max()
y_min, y_max = points[:, 1].min(), points[:, 1].max()
z_min, z_max = points[:, 2].min(), points[:, 2].max()

# Compute the length, width, and height
length = x_max - x_min
width = y_max - y_min
height = z_max - z_min

print(sliced_mesh)

print(length, width, height)

