import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Vertex Shader source code
vertex_shader_src = """
#version 330 core
layout (location = 0) in vec2 aPos;
void main()
{
    gl_Position = vec4(aPos, 0.0, 1.0);
}
"""

# Fragment Shader source code
fragment_shader_src = """
#version 330 core
out vec4 FragColor;
void main()
{
    FragColor = vec4(1.0, 0.5, 0.31, 1.0); // Change color as needed
}
"""

def create_shader_program():
    program = compileProgram(
        compileShader(vertex_shader_src, GL_VERTEX_SHADER),
        compileShader(fragment_shader_src, GL_FRAGMENT_SHADER)
    )
    return program

def draw_pixel_art(tortoise_coords, rabbit_coords, cat_coords, dragon_coords):
    vertices = []
    
    # Tortoise
    for (x, y) in tortoise_coords:
        vertices.extend([x/320, y/240])
    
    # Rabbit
    for (x, y) in rabbit_coords:
        vertices.extend([x/320, y/240])
    
    # Cat
    for (x, y) in cat_coords:
        vertices.extend([x/320, y/240])
    
    # Dragon
    for (x, y) in dragon_coords:
        vertices.extend([x/320, y/240])
    
    vertices = np.array(vertices, dtype=np.float32)

    program = create_shader_program()
    VBO = glGenBuffers(1)
    VAO = glGenVertexArrays(1)

    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * vertices.itemsize, None)
    glEnableVertexAttribArray(0)

    glUseProgram(program)
    glBindVertexArray(VAO)
    glDrawArrays(GL_POINTS, 0, len(vertices)//2)
    glBindVertexArray(0)
    glUseProgram(0)

def main():
    if not glfw.init():
        return

    window = glfw.create_window(768, 1024, "Pixel Art Game", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    tortoise_coords = [
        (-240, 200), (-200, 240),
        (-210, 180), (-170, 200),
        (-290, 170), (-210, 170), (-290, 190), (-170, 190),
        (-250, 160)
    ]
    
    rabbit_coords = [
        (-240, 240), (-200, 280),
        (-230, 220), (-210, 240),
        (-250, 260), (-190, 260),
        (-230, 245), (-210, 245)
    ]

    cat_coords = [
        (-240, 280), (-200, 320),
        (-230, 260), (-210, 280),
        (-250, 300), (-190, 300),
        (-230, 285), (-210, 285),
        (-220, 250)
    ]

    dragon_coords = [
        (-250, 320), (-190, 360),
        (-240, 300), (-200, 320),
        (-260, 340), (-210, 340), (-210, 360), (-180, 360),
        (-230, 280)
    ]

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        draw_pixel_art(tortoise_coords, rabbit_coords, cat_coords, dragon_coords)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
