from OpenGL.GL import *
import pygame

from pygame.locals import *

from OpenGL.GL import *

from OpenGL.GLU import *

vertices = (

    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (

    (0, 1),
    (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
    (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
)


def Draw():
    glBegin(GL_LINE)

    for edge in edges:
        for node in edge:
            glVertex3fv(vertices[node])
    glEnd()


def main():
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(45.0,(display[0]/display[1]), 1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    glRotatef(18, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Draw()
        pygame.display.flip()
        pygame.time.wait(10)

main()
