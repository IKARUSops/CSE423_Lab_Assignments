from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import time

background_color = (0.0, 0.0, 0.0)
door_color = (37/255, 146/255, 255/255)
house_color = (255/255, 244/255, 233/255)  
roof_color = (81/255, 38/255, 182/255) 
rain_color = (	37/255, 146/255, 255/255) 

num_raindrops = 50  
rain_x1 = [0.0] * num_raindrops
rain_y1 = [1.0] * num_raindrops
rain_x2 = [0.0] * num_raindrops
rain_y2 = [0.9] * num_raindrops
rain_direction = 0.0  

def drawBackground():
    """Draws the background."""
    glColor3fv(background_color)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()



def drawHorizon():
    """Draws a horizon line representing the ground."""
    glColor3f(0.5, 0.35, 0.05)  
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




    

def drawHouse():

    house_arr = [(-0.35, 0.2), (-0.35, -0.2), (0.35, -0.2), (0.35, 0.2)]


    glColor3fv(house_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(house_arr[0][0], house_arr[0][1])  
    glVertex2f(house_arr[1][0], house_arr[1][1])  
    glVertex2f(house_arr[2][0], house_arr[2][1]) 
    glEnd()

   
    glColor3fv(house_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(house_arr[0][0], house_arr[0][1])  
    glVertex2f(house_arr[2][0], house_arr[2][1])  
    glVertex2f(house_arr[3][0], house_arr[3][1])  
    glEnd()


    
    glColor3fv(roof_color)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.4, 0.2)
    glVertex2f(0.4, 0.2)
    glVertex2f(0.0, 0.5)
    glEnd()

    
    glColor3fv(door_color)

    
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.05, -0.2)
    glVertex2f(0.05, -0.2)
    glVertex2f(-0.05, 0.1)
    glEnd()

    
    glBegin(GL_TRIANGLES)
    glVertex2f(0.05, -0.2)
    glVertex2f(0.05, 0.1)
    glVertex2f(-0.05, 0.1)
    glEnd()


    glPointSize(8)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(0.02, -0.05)
    glEnd()

    glColor3fv(door_color)

    glBegin(GL_TRIANGLES)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.1, -0.05)
    glEnd()

    
    glBegin(GL_TRIANGLES)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.2, -0.05)
    glVertex2f(0.1, -0.05)
    glEnd()


    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0.15, 0.1)
    glVertex2f(0.15, -0.05)
    glVertex2f(0.1, 0.025)
    glVertex2f(0.2, 0.025)
    glEnd()


    glColor3fv(door_color)

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.1, 0.1)
    glVertex2f(-0.2, 0.1)
    glVertex2f(-0.1, -0.05)
    glEnd()

    
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.2, 0.1)
    glVertex2f(-0.2, -0.05)
    glVertex2f(-0.1, -0.05)
    glEnd()



    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(-0.15, 0.1)
    glVertex2f(-0.15, -0.05)
    glVertex2f(-0.1, 0.025)
    glVertex2f(-0.2, 0.025)
    glEnd()

    

def drawRain():

    glColor3fv(rain_color)
    glLineWidth(1)
    glBegin(GL_LINES)
    for j in range(3):  
        for i in range(num_raindrops):
            glVertex2f(rain_x1[i], rain_y1[i])
            glVertex2f(rain_x2[i] + rain_direction, rain_y2[i])
        

        for k in range(num_raindrops):
            time.sleep(0.0001)
            offset = random.uniform(0, 0.5)
            rain_y1[k] -= offset
            rain_y2[k] -= offset


            if rain_y1[k] < -0.75:
                rain_y1[k] = 1.0
                rain_y2[k] = 0.9
                rain_x1[k] = random.uniform(-1, 1)
                rain_x2[k] = rain_x1[k]
    glEnd()

def animate():

    glutPostRedisplay()

def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    drawBackground()
    drawHorizon() 
    drawHouse()
    drawRain()
    glutSwapBuffers()

def initializeRain():

    for i in range(num_raindrops):
        rain_x1[i] = random.uniform(-1, 1)
        rain_x2[i] = rain_x1[i]

def specialKeyListener(key, x, y):

    global rain_direction
    if key == GLUT_KEY_LEFT:
        rain_direction -= 0.05 
    elif key == GLUT_KEY_RIGHT:
        rain_direction += 0.05  
    glutPostRedisplay()

def keyboardListener(key, x, y):

    global background_color
    if key == b'n':  
        background_color = tuple(max(0.0, c - 0.1) for c in background_color)
    elif key == b'd':  
        background_color = tuple(min(1.0, c + 0.1) for c in background_color)
    glutPostRedisplay()

def mouse_click(button, state, x, y):

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        initializeRain()
    glutPostRedisplay()

glutInit()
glutInitWindowSize(1280, 720)
glutCreateWindow(b"Assignment1 Task1")
glutDisplayFunc(display)
glutIdleFunc(animate) 
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouse_click)
initializeRain()
glutMainLoop()
