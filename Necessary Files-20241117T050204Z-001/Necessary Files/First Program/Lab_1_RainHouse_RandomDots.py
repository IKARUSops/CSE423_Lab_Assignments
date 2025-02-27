'''Task-1'''

from OpenGL.GL import *
from OpenGL.GLUT import *
import random
import time

background_color = (0.0, 0.0, 0.0)
door_color = (37/255, 146/255, 255/255)
house_color = (255/255, 244/255, 233/255)  
roof_color = (81/255, 38/255, 182/255) 
rain_color = (	37/255, 146/255, 255/255) 

raindrops = 50  
rain_x1 = [0.0] * raindrops
rain_y1 = [1.0] * raindrops
rain_x2 = [0.0] * raindrops
rain_y2 = [0.9] * raindrops
rain_direction = 0.0  

def drawBackground():

    glColor3fv(background_color)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()



def drawHorizon():

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
        for i in range(raindrops):
            glVertex2f(rain_x1[i], rain_y1[i])
            glVertex2f(rain_x2[i] + rain_direction, rain_y2[i])
        

        for k in range(raindrops):
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

    for i in range(raindrops):
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





# '''Task-2'''

# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# import random

# box_color = (0.0, 0.0, 0.0)  
# points = []  
# speed = 0.0001  
# blink_speed = 2.0 
# blink_on = False 
# blinks = None 
# space_pressed = False 


# glutInit()
# glutInitWindowSize(1280, 720)
# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
# glutCreateWindow(b"Assignment1 Task2")


# def change_blink_state(value):
#     global blink_on
#     if blinks is not None:
#         blink_on = not blink_on
#         glutTimerFunc(int(blink_speed * 1000), change_blink_state, 0)
#     else:
#         blink_on = False


# def color_select():
#     return (random.random(), random.random(), random.random())


# def direction_select():
#     return (random.choice([1, -1]), random.choice([1, -1]))


# def draw_point(position, color):
#     if not space_pressed:  
#         if blink_on:
#             glColor3f(0.0, 0.0, 0.0)  
#         else:
#             glColor3fv(color)  
#         glBegin(GL_POINTS)
#         glVertex3fv(position)
#         glEnd()
#     else:
        
#         glColor3fv(color)
#         glBegin(GL_POINTS)
#         glVertex3fv(position)
#         glEnd()

# def update_points():
#     if not space_pressed:  
#         for i in range(len(points)):
#             x, y, color, direction = points[i]
#             new_x = x + speed * direction[0]
#             new_y = y + speed * direction[1]

            
#             if abs(new_x) >= 1:
#                 direction = (-direction[0], direction[1])
#                 new_x = max(min(new_x, 1), -1)  
#             if abs(new_y) >= 1:
#                 direction = (direction[0], -direction[1])
#                 new_y = max(min(new_y, 1), -1)  

#             points[i] = (new_x, new_y, color, direction)


# def blink_control(button, state, x, y):
#     global blink_on, blinks
#     if not space_pressed:
#         if state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON:
            
#             x = (x / 1280) * 2 - 1  
#             y = -((y / 720) * 2 - 1) 
#             color = color_select()
#             direction = direction_select()
#             points.append((x, y, color, direction))
#         elif state == GLUT_DOWN and button == GLUT_LEFT_BUTTON:
            
#             if blinks is None:
#                 blinks = 0
#                 glutTimerFunc(int(blink_speed * 1000), change_blink_state, 0)
#             else:
#                 blinks = None


# def speed_control(key, x, y):
#     global speed
#     if not space_pressed:
#         if key == GLUT_KEY_UP:
#             speed += 0.0001
#         elif key == GLUT_KEY_DOWN:
#             if speed > 0.0002:
#                 speed -= 0.0001


# def blink_speed_control(key, x, y):
#     global space_pressed, blink_speed
#     if key == b" ":
#         space_pressed = not space_pressed


#     if key == b"+":
#         blink_speed = max(0.05, blink_speed - 0.05) 
#     if key == b"-":
#         blink_speed = min(0.5, blink_speed + 0.05) 




# def display():
#     global box_color, points
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    
#     update_points()
#     for x, y, color, _ in points:
#         glPointSize(7.0)
#         draw_point((x, y, 0), color)
    
#     glutSwapBuffers()  


# glutDisplayFunc(display)
# glutIdleFunc(glutPostRedisplay)
# glutMouseFunc(blink_control)
# glutSpecialFunc(speed_control)
# glutKeyboardFunc(blink_speed_control)


# glutMainLoop()
