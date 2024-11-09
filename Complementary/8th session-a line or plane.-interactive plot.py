#pip install numpy matplotlib ipywidgets

#The following code is the interactive plot of the system of equations of the following session: https://github.com/mjavadg/Econometrics_Fall-2024/blob/main/8th%20session%20linear%20algebra%20part%202.ipynb

#Download it then run it.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ipywidgets import interact, FloatSlider
import matplotlib.animation as animation

# Coefficients matrix and constants for the 3D system
A = np.array([[6, 5, 2], [3, 4, 1], [1, 2, 3]])  # 3x3 coefficients matrix
B = np.array([49, 32, 20])                      # Constants

# Calculate the solution
solutions = np.linalg.solve(A, B)
print("Solutions using numpy:", solutions)

# Create a 3D figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a grid for plotting the planes
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# Define Z for each plane based on the equations
Z1 = (49 - 6*X - 5*Y) / 2  # From equation 1: 6x + 5y + 2z = 49
Z2 = (32 - 3*X - 4*Y)      # From equation 2: 3x + 4y + z = 32
Z3 = (20 - X - 2*Y) / 3    # From equation 3: x + 2y + 3z = 20

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.4, color='blue', label='Plane 1: 6x + 5y + 2z = 49')
ax.plot_surface(X, Y, Z2, alpha=0.4, color='orange', label='Plane 2: 3x + 4y + z = 32')
ax.plot_surface(X, Y, Z3, alpha=0.4, color='green', label='Plane 3: x + 2y + 3z = 20')

# Highlight the solution point
ax.scatter(solutions[0], solutions[1], solutions[2], color='red', s=100, label='Solution Point')
ax.text(solutions[0], solutions[1], solutions[2], f'Solution: {solutions}', fontsize=10, ha='right')

# Function to update the 3D plot
def update(angle):
    ax.view_init(elev=10, azim=angle)

# Create the interactive slider
interact(update, angle=FloatSlider(min=0, max=360, step=1, value=0))

# Show the plot
plt.show()