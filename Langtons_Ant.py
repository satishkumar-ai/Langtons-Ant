import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ROWS = COLS = 100

grid = np.zeros((ROWS, COLS), dtype=int)

position = [50,50]
direction = 0


def movement_change(position, direction):
    row, col = position
    if direction == 0:
        row -= 1
    elif direction == 1:
        col += 1
    elif direction == 2:
        row += 1
    elif direction == 3:
        col -=1

    if 0 <= row < ROWS and 0 <= col < COLS:
        return [row, col]

    return None

def position_update(position,direction):
    row, col = position

    if grid[row, col] == 0:
        direction = (direction + 1) % 4
        grid[row, col] = 1
    else:
        direction = (direction - 1) % 4
        grid[row, col] = 0

    new_position = movement_change(position, direction)
    return new_position, direction

def movement(position, direction):
    new_position, new_direction = position_update(position, direction)
    return new_position, new_direction


fig, ax = plt.subplots(figsize=(7, 7))

image = ax.imshow(grid, cmap="binary", vmin=0, vmax=1, animated=True)

ant_marker, = ax.plot(
    position[1],
    position[0],
    "ro",
    markersize=5
)

ax.set_title("Langton's Ant")
ax.set_xticks([])
ax.set_yticks([])


def animate(frame):
    global position, direction

    new_position, new_direction = movement(position, direction)

    if new_position is None:
        ani.event_source.stop()
        return image, ant_marker

    position = new_position
    direction = new_direction

    image.set_data(grid)
    ant_marker.set_data([position[1]], [position[0]])

    return image, ant_marker


ani = FuncAnimation(
    fig,
    animate,
    interval=20,
    blit=True,
    cache_frame_data=False
)

plt.show()