import glfw
from OpenGL.GL import *
import numpy as np
import os

# Glfw: https://www.glfw.org/docs/latest/index.html
# Microssoft: https://learn.microsoft.com/en-us/windows/win32/opengl/opengl
# Tutorial: https://www.youtube.com/watch?v=sUJo9KXFzAM&list=PL1P11yPQAo7opIg8r-4BMfh1Z_dCOfI0y&index=2
# Keys: https://www.glfw.org/docs/3.3/group__keys.html#ga9845be48a745fc232045c9ec174d8820


# Initializing glfw library
if not glfw.init():
    raise Exception("glfw cant' be initialized")

# Screen dimensions
user32 = ctypes.windll.user32
s_width = user32.GetSystemMetrics(78)
s_height = user32.GetSystemMetrics(79)

# Window dimensions
w_width = 1280
w_height = 720

# Creating the window
window = glfw.create_window(w_width, w_height, "My OpenGL Window", None, None)

# Check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can't be created!")

# Set window's position
glfw.set_window_pos(window, int((s_width-w_width)/2.0), int((s_height-w_height-20)/2.0))

# Make the context current
glfw.make_context_current(window)

# Specify the clear colors used by glClear to clear the color buffers
# This will change the window background color
glClearColor(0, 0.1, 0.1, 1)

# Triangle vertice positions x, y, z
t_vertices = [-0.5, -0.5, 0.0,
              0.5, -0.5, 0.0,
              0.0, 0.5, 0.0]

t_colors = [1.0, 0.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0]

# Convert to numpy array
t_vertices = np.array(t_vertices, dtype=np.float32)
t_colors = np.array(t_colors, dtype=np.float32)

# Enable options
glEnableClientState(GL_VERTEX_ARRAY)
glEnableClientState(GL_COLOR_ARRAY)

# Create a object of size 3 = x, y, z
glVertexPointer(3, GL_FLOAT, 0, t_vertices)

# Apply color to object
glColorPointer(3, GL_FLOAT, 0, t_colors)

# Setup key callback
def keyCallback(window: COpaquePointer, key: Int32, scancode: Int32, action: Int32, mode: Int32)
{
    if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS) {
        glfwSetWindowShouldClose(window, GL_TRUE)
    }
}

# The main applicaiton loop
while not glfw.window_should_close(window):
    # Events here
    key = window.getkey()

    if key == 265:
        # KEY_UP
        print("keyUp")

    # Render here
    # Clear the buffer colors
    glClear(GL_COLOR_BUFFER_BIT)

    # Rotate in Y axis
    glRotatef(2, 0, 1, 0)

    # Draw the content using triangle polygon mode
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # Swap front and back buffers, the drawing will occur in back buffer
    # Then the back buffer becomes the front buffer and user will be able to see
    # Drawed content
    glfw.swap_buffers(window)

    # Process all pending events, to allow mouse events and keyboard events
    glfw.poll_events()

# Terminate glfw, free up allocated resources
glfw.terminate()
