
import c
import dq
import dp
import ve
import di

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation  # Import FuncAnimation
import numpy as np

cEF = False

dq.cEM(1,0,0,10000)



dp.mdp(0, -2.5, 1, 0, 0, 0, 1E-5, 1)
#di.mdIL(1, 5E11)
#dq.mdq(-1,-2.5,0,1)

#List to store particle positions for each frame
particle_positions = []
particle_positionsi = []
particle_positionsq = []
r = ve.ve(0, 0, 0)

# Number of frames
num_frames = 500


for j in range(len(di.ldi)): 
    r = (di.ldi[j].r)
    particle_positionsi.append((r.x, r.y, r.z))
    ve.vP(di.ldi[j].s)

for j in range(len(dq.ldq)): 
    r = (dq.ldq[j].r)
    particle_positionsq.append((r.x, r.y, r.z))

# Create 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot particle trajectories (initial plot)
line, = ax.plot([], [], [], label='Particle', marker='o', color='blue')
linei, = ax.plot([], [], [], label='Currents', marker='o', color='red')
lineq, = ax.plot([], [], [], label='Charges', marker='o', color='green')

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

# Set the size of the grid
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])  

# Function to update the plot for each frame
def update(frame):
    # Calculate particle positions using cM function for set 1
    for n in range(len(dp.ldp)):
        r = dp.cM(dp.cE(n), dp.cB(n), n)
        particle_positions.append((r.x, r.y, r.z))

    # Convert the list of positions to numpy array for easy plotting
    particle_positions_array = np.array(particle_positions)

    # Update the plot data
    line.set_data(particle_positions_array[:, 0], particle_positions_array[:, 1])
    line.set_3d_properties(particle_positions_array[:, 2])

    # Calculate particle positions for set 2
    if(len(di.ldi) != 0):
        for j in range(len(di.ldi)): 
            r = (di.ldi[j].r)
            particle_positionsi.append((r.x, r.y, r.z))

        # Convert the list of positions to numpy array for easy plotting
        particle_positionsi_array = np.array(particle_positionsi)

        # Update the plot data for set 2
        linei.set_data(particle_positionsi_array[:, 0], particle_positionsi_array[:, 1])
        linei.set_3d_properties(particle_positionsi_array[:, 2])

    if(len(dq.ldq) != 0):
        # Calculate particle positions for set 3
        for k in range(len(dq.ldq)): 
            r = (dq.ldq[k].r)
            particle_positionsq.append((r.x, r.y, r.z))

        # Convert the list of positions to numpy array for easy plotting
        particle_positionsq_array = np.array(particle_positionsq)

        # Update the plot data for set 3
        lineq.set_data(particle_positionsq_array[:, 0], particle_positionsq_array[:, 1])
        lineq.set_3d_properties(particle_positionsq_array[:, 2])

    return line, linei, lineq

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=c.dt*1000)  # Adjust interval as needed

# Show the plot
plt.show()