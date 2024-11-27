import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# surface plot
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# labels for axes
ax.set_xlabel('Strike Price (X)')
ax.set_ylabel('Volatility (Y)')
ax.set_zlabel('Option Price (Z)')

# fixed annotation above the plot (outside of the rotating loop)
strike_price = 2
volatility = 2
option_price = np.sin(np.sqrt(strike_price**2 + volatility**2))

# annotation at the top of the plot (fixed position)
ax.text2D(0.5, 0.95, r'$\sin(\sqrt{x^2 + y^2})$', 
ha='center', va='top', color='red', fontsize=12, transform=ax.transAxes)

# Function to update the plot for each frame (for rotation)
def update(frame):
    ax.view_init(elev=30, azim=frame)  # view angle for rotation
    return surf,

# animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=100, blit=False)

# Display the plot interactively
plt.show()
