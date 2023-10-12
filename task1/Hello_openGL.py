from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

res_x, res_y = 500, 500

def draw_points(size:int, x:int, y:int):
    glPointSize(size) # pixel size. default: 1
    glBegin(GL_POINTS)
    glVertex2f(x,y) # pixel co-ordination
    glEnd()

def iterate():
    glViewport(0, 0, res_x, res_y)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def Draw_line(x1:int,y1:int,x2:int,y2:int)-> None:

    while (x1!=x2 and y1!=y2):
        draw_points(4, x1,y1)
        x1+=1
        y1+=1

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(15, 500,500)
    # Draw_line(220,220,320,320)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(res_x, res_y) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()