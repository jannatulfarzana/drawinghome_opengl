
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Base():
    glBegin(GL_LINES)
    glVertex2f(320, 150) #bottom
    glVertex2f(170, 150)
    glVertex2f(170, 320) #left
    glVertex2f(170, 150)
    glVertex2f(170, 320) #right
    glVertex2f(320, 320)
    glVertex2f(320, 320) #top
    glVertex2f(320, 150)
    glEnd()

def triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(320, 320)
    glVertex2f(245, 400)
    glVertex2f(170, 320)
    glEnd()

def windowL():
    glBegin(GL_LINES)
    glVertex2f(190, 250)  # bottom
    glVertex2f(230, 250)
    glVertex2f(190, 250)  # left
    glVertex2f(190, 290)
    glVertex2f(230, 290)  # right
    glVertex2f(230, 250)
    glVertex2f(190, 290)  # top
    glVertex2f(230, 290)
    glEnd()

def windowR():
    glBegin(GL_LINES)
    glVertex2f(260, 250)  # bottom
    glVertex2f(300, 250)
    glVertex2f(260, 250)  # left
    glVertex2f(260, 290)
    glVertex2f(300, 250)  # right
    glVertex2f(300, 290)
    glVertex2f(260, 290)  # top
    glVertex2f(300, 290)
    glEnd()

def Door():
    glBegin(GL_LINES)
    glVertex2f(230, 150)  # left
    glVertex2f(230, 210)
    glVertex2f(230, 210)  # top
    glVertex2f(260, 210)
    glVertex2f(260, 150)  # right
    glVertex2f(260, 210)
    glEnd()
    glBegin(GL_POINTS)
    glVertex2f(257, 180)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    #call the draw methods here
    glPointSize(5)
    Base()
    triangle()
    windowL()
    windowR()
    Door()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
