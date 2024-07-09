# Work in progress calculations baby!!!!!!!!!!
# work postponed untill i solve it for one 

import numpy as np
import pyvista as pv
import sys

# Defining numbers of slices
num_slc = 10

# Load the STL file
mesh = pv.read('Rechteckrohr_verjuengt_Volumen.stl')

# Get the coordinates of all points in the mesh
points = mesh.points

# Calculate the dimensions
x_min, x_max = points[:, 0].min(), points[:, 0].max()
y_min, y_max = points[:, 1].min(), points[:, 1].max()
z_min, z_max = points[:, 2].min(), points[:, 2].max()

# Compute the length, width, and height
length = x_max - x_min
width = y_max - y_min
height = z_max - z_min

# Making sure the beam is in correct orientation (Length is the biggest dimension)
biggest_dimension = max(length, width, height)
if biggest_dimension != length:
    print("Beam in not in correct orientaion!")
    sys.exit(1)

# Setting fixed variables needed throughout the process
slc_pitch = length/(num_slc-1) #Defining the pitch between slices
normal = np.array([1, 0, 0], dtype=float)  # Normal vector of the plane (z-direction) + ensuring format is float for numpy
normal /= np.linalg.norm(normal) # Make sure the normal vector is normalized

# Making list of future slices 
sliced_mesh_list = []

# Generate the slice at i = 0 separately
origin = np.array([1, 0, 0])  # Origin of the plane for the first slice
sliced_mesh = mesh.slice(normal=normal, origin=origin)
sliced_mesh_list.append(sliced_mesh)

# Making the slices for for i > 0
for i in range(1, num_slc-1):
    origin = np.array([i*slc_pitch, 0, 0])  # Origin of the plane
    point_on_plane = origin + normal  # Define a point on the plane
    sliced_mesh = mesh.slice(normal=normal, origin=origin)
    sliced_mesh_list.append(sliced_mesh) # filling the list with the appropriate slices

# Generate the slice at the end separately
origin = np.array([x_max, 0, 0])  # Origin of the plane for the last slice
sliced_mesh = mesh.slice(normal=normal, origin=origin)
sliced_mesh_list.append(sliced_mesh)

# Making the visualization of all the slices
plotter = pv.Plotter()# Create a plotter
plotter.add_mesh(mesh, color="lightgrey", opacity=0.5)# Add the original mesh to the plotter
basic_colors =  ["blue", "red", "green", "yellow", "purple", "orange", "cyan", "magenta", "lime", "teal", "pink", "brown", "navy", "olive", "maroon"] # Define a list of basic colors for visualization

# Add each sliced mesh to the plotter with a basic color
for i, sliced_mesh in enumerate(sliced_mesh_list):
    color = basic_colors[i % len(basic_colors)]  # Cycle through basic colors
    plotter.add_mesh(sliced_mesh, color=color)

plotter.show() #final plot
