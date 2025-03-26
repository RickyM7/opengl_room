from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from InteractiveRoom3D.core import init, setup, display, keyboard, mouse_motion

def main():
    """ Função principal """
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Quarto 3D - OpenGL")

    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse_motion)  # Captura movimento do mouse
    setup()
    glutMainLoop()

if __name__ == "__main__":
    main()