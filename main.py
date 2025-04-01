from OpenGL.GLUT import *
from InteractiveRoom3D.core import init, setup, display, keyboard
from InteractiveRoom3D.camera import mouse_button, mouse_motion

def main():
    """Função principal"""
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Quarto 3D - OpenGL")

    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse_button)
    glutMotionFunc(mouse_motion)
    setup()
    glutMainLoop()

if __name__ == "__main__":
    main()