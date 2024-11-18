from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

box_color = (0.0, 0.0, 0.0)  
points = []  
point_speed = 0.0001  
blink_speed = 2.0 
blink_on = False 
blinks = None 
space_pressed = False 


glutInit()
glutInitWindowSize(1280, 720)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b"Assignment1 Task2")


def change_blink_state(value):
    global blink_on
    if blinks is not None:
        blink_on = not blink_on
        glutTimerFunc(int(blink_speed * 1000), change_blink_state, 0)
    else:
        blink_on = False


def color_select():
    return (random.random(), random.random(), random.random())


def direction_select():
    return (random.choice([1, -1]), random.choice([1, -1]))


def draw_point(position, color):
    if not space_pressed:  
        if blink_on:
            glColor3f(0.0, 0.0, 0.0)  
        else:
            glColor3fv(color)  
        glBegin(GL_POINTS)
        glVertex3fv(position)
        glEnd()
    else:
        
        glColor3fv(color)
        glBegin(GL_POINTS)
        glVertex3fv(position)
        glEnd()

def update_points():
    if not space_pressed:  
        for i in range(len(points)):
            x, y, color, direction = points[i]
            new_x = x + point_speed * direction[0]
            new_y = y + point_speed * direction[1]

            
            if abs(new_x) >= 1:
                direction = (-direction[0], direction[1])
                new_x = max(min(new_x, 1), -1)  
            if abs(new_y) >= 1:
                direction = (direction[0], -direction[1])
                new_y = max(min(new_y, 1), -1)  

            points[i] = (new_x, new_y, color, direction)


def blink_control(button, state, x, y):
    global blink_on, blinks
    if not space_pressed:
        if state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON:
            
            x = (x / 1280) * 2 - 1  
            y = -((y / 720) * 2 - 1) 
            color = color_select()
            direction = direction_select()
            points.append((x, y, color, direction))
        elif state == GLUT_DOWN and button == GLUT_LEFT_BUTTON:
            
            if blinks is None:
                blinks = 0
                glutTimerFunc(int(blink_speed * 1000), change_blink_state, 0)
            else:
                blinks = None


def speed_control(key, x, y):
    global point_speed
    if not space_pressed:
        if key == GLUT_KEY_UP:
            point_speed += 0.0001
        elif key == GLUT_KEY_DOWN:
            if point_speed > 0.0002:
                point_speed -= 0.0001


def blink_speed_control(key, x, y):
    global space_pressed, blink_speed
    if key == b" ":
        space_pressed = not space_pressed


    if key == b"+":
        blink_speed = max(0.05, blink_speed - 0.05) 
    if key == b"-":
        blink_speed = min(0.5, blink_speed + 0.05) 




def display():
    global box_color, points
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    
    update_points()
    for x, y, color, _ in points:
        glPointSize(7.0)
        draw_point((x, y, 0), color)
    
    glutSwapBuffers()  


glutDisplayFunc(display)
glutIdleFunc(glutPostRedisplay)
glutMouseFunc(blink_control)
glutSpecialFunc(speed_control)
glutKeyboardFunc(blink_speed_control)


glutMainLoop()
