import glfw
from OpenGL.GL import *

if not glfw.init():
    raise Exception("GLFW nao pode ser executado")

window = glfw.create_window(1200, 600, "Uma janela para o seu bruxo", None, None)

# Center GLFW Window
monitor = glfw.get_primary_monitor()
pos = glfw.get_monitor_pos(monitor)
size = glfw.get_window_size(window)
mode = glfw.get_video_mode(monitor)
print(int((mode.size.height - size[1]) / 2))
glfw.set_window_pos(
    window,
    int(pos[0] + (mode.size.width - size[0]) / 2),
    int(pos[1] + (mode.size.height - size[1]) / 2))

if not window:
    glfw.terminate()
    raise Exception("Uma janela para o seu bruxo nao pode ser aberta")

# glfw.set_window_pos(window, 400, 100)
glfw.make_context_current(window)

# Define a cor de fundo (vermelho, verde, azul, alpha)
glClearColor(0.4, 0.2, 0.1, 1.0)
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.poll_events()
    glfw.swap_buffers(window)
glfw.terminate()