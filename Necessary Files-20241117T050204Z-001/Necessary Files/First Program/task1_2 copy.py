from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import time

# Global Variables for Color and Rain
background_color = (0.0, 0.0, 0.0)
door_color = (0.855, 0.647, 0.125)
house_color = (0.5, 0.5, 0.5)  # Gray
roof_color = (0.7, 0.1, 0.1)  # Red
rain_color = (0.0, 0.0, 1.0)  # Blue

num_raindrops = 50  # Number of raindrops per layer
rain_x1 = [0.0] * num_raindrops
rain_y1 = [1.0] * num_raindrops
rain_x2 = [0.0] * num_raindrops
rain_y2 = [0.9] * num_raindrops
rain_direction = 0.0  # Rain direction offset

def drawBackground():
    """Draws the background."""
    glColor3fv(background_color)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()

def drawShapes():
    glBegin(GL_TRIANGLES)
    glVertex2d(-170,170)
    glColor3f(0, 1.0, 0.0)
    glVertex2d(-180,150)
    glColor3f(1,0, 0.0)
    glVertex2d(-160,150)
    glEnd()

def drawHorizon():
    """Draws a horizon line representing the ground."""
    glColor3f(0.5, 0.35, 0.05)  # Brown color for the ground
    glLineWidth(200)
    for i in range(30):
        glBegin(GL_LINES)
        glVertex2f(-1.0, -0.8+(i/30))
        glVertex2f(1.0, -0.8+(i/30))
        glEnd()
    
    y = -0.8 + (i/30)
    for j in range(-10,10,1):
        i = j/10
        glBegin(GL_TRIANGLES)
        glColor3f(0.5, 0.35, 0.05)
        glVertex2d(i+0.05,y+0.25)
        glColor3f(0, 1.0, 0.0)
        glVertex2d(i,y)
        glColor3f(0, 1.0, 0.0)
        glVertex2d(i+0.1,y)
        glEnd()




    # Ground direction indicator line

def drawHouse():
    """Draws the house structure."""
    glColor3fv(house_color)
    glBegin(GL_QUADS)
    glVertex2f(-0.35, -0.2)
    glVertex2f(0.35, -0.2)
    glVertex2f(0.35, 0.2)
    glVertex2f(-0.35, 0.2)
    glEnd()

    # Draw the roof
    glColor3fv(roof_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.4, 0.2)
    glVertex2f(0.4, 0.2)
    glVertex2f(0.0, 0.5)
    glEnd()

    # Draw the door
    glColor3fv(door_color)
    glBegin(GL_QUADS)
    glVertex2f(-0.05, -0.2)
    glVertex2f(0.05, -0.2)
    glVertex2f(0.05, 0.1)
    glVertex2f(-0.05, 0.1)
    glEnd()

    # Door knob
    glPointSize(6)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(0.02, -0.05)
    glEnd()

    # Draw window with grid
    glColor3fv(door_color)
    glBegin(GL_QUADS)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.2, -0.05)
    glVertex2f(0.1, -0.05)
    glEnd()

    # Draw grid lines on the window
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0.15, 0.1)
    glVertex2f(0.15, -0.05)
    glVertex2f(0.1, 0.025)
    glVertex2f(0.2, 0.025)
    glEnd()

def drawRain():
    """Draws 3 layers of raindrops and updates their positions."""
    glColor3fv(rain_color)
    glLineWidth(1)
    glBegin(GL_LINES)
    for j in range(3):  # 3 layers of rain
        for i in range(num_raindrops):
            glVertex2f(rain_x1[i], rain_y1[i])
            glVertex2f(rain_x2[i] + rain_direction, rain_y2[i])
        
        # Update rain positions for the next iteration
        for k in range(num_raindrops):
            time.sleep(0.0001)
            offset = random.uniform(0, 0.5)
            rain_y1[k] -= offset
            rain_y2[k] -= offset

            # Reset if raindrop reaches the bottom
            if rain_y1[k] < -0.75:
                rain_y1[k] = 1.0
                rain_y2[k] = 0.9
                rain_x1[k] = random.uniform(-1, 1)
                rain_x2[k] = rain_x1[k]
    glEnd()

def animate():
    """Triggers continuous display refresh."""
    glutPostRedisplay()

def display():
    """Clears and redraws the entire scene."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    drawBackground()
    drawHorizon()  # Draw the horizon line
    drawHouse()
    drawRain()
    glutSwapBuffers()

def initializeRain():
    """Initializes raindrop positions."""
    for i in range(num_raindrops):
        rain_x1[i] = random.uniform(-1, 1)
        rain_x2[i] = rain_x1[i]

def specialKeyListener(key, x, y):
    """Handles special key input for changing the rain direction."""
    global rain_direction
    if key == GLUT_KEY_LEFT:
        rain_direction -= 0.05  # Bend rain left
    elif key == GLUT_KEY_RIGHT:
        rain_direction += 0.05  # Bend rain right
    glutPostRedisplay()

def keyboardListener(key, x, y):
    """Handles keyboard input for background color change."""
    global background_color
    if key == b'n':  # Night mode
        background_color = tuple(max(0.0, c - 0.1) for c in background_color)
    elif key == b'd':  # Day mode
        background_color = tuple(min(1.0, c + 0.1) for c in background_color)
    glutPostRedisplay()

def mouse_click(button, state, x, y):
    """Handles mouse click events."""
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        initializeRain()
    glutPostRedisplay()

# OpenGL Initialization
glutInit()
glutInitWindowSize(1280, 720)
glutCreateWindow(b"Assignment1Task1")
glutDisplayFunc(display)
glutIdleFunc(animate)  # Set the animate function for continuous updates
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouse_click)
initializeRain()
glutMainLoop()
