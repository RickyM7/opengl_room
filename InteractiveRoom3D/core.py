from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from .room import draw_room
from .camera import *
import numpy as np

wall_texture = None

def init():
    """Inicializa as configurações do OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
    glEnable(GL_DEPTH_TEST)

    # Desativar iluminação automática para ter mais controle
    glDisable(GL_LIGHTING)

    # Habilitar sombreamento suave
    glShadeModel(GL_SMOOTH)

def display():
    """ Renderiza a cena """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Define a câmera
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],
              camera_pos[0] + camera_front[0], camera_pos[1] + camera_front[1], camera_pos[2] + camera_front[2],
              camera_up[0], camera_up[1], camera_up[2])

    draw_room()
    glutSwapBuffers()

def keyboard(key, x, y):
    """ Gerencia a movimentação do usuário usando WASD """
    global camera_pos

    direction = camera_front * speed
    right = np.cross(camera_front, camera_up) * speed

    if key == b'w':  # Para frente
        camera_pos += direction
    elif key == b's':  # Para trás
        camera_pos -= direction
    elif key == b'a':  # Para a esquerda
        camera_pos -= right
    elif key == b'd':  # Para a direita
        camera_pos += right

    glutPostRedisplay()

def mouse_motion(x, y):
    """ Atualiza a direção da câmera com o movimento do mouse """
    global yaw, pitch, last_x, last_y, first_mouse, camera_front

    if first_mouse:
        last_x, last_y = x, y
        first_mouse = False

    # Calcula deslocamento do mouse
    x_offset = (x - last_x) * sensitivity
    y_offset = (last_y - y) * sensitivity  # Invertido porque o OpenGL tem Y ao contrário
    last_x, last_y = x, y

    # Atualiza ângulos
    yaw += x_offset
    pitch += y_offset

    # Restringe o pitch para evitar giros indesejados
    pitch = max(-89.0, min(89.0, pitch))

    # Calcula nova direção da câmera
    direction = np.array([
        np.cos(np.radians(yaw)) * np.cos(np.radians(pitch)),
        np.sin(np.radians(pitch)),
        np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
    ])
    camera_front = direction / np.linalg.norm(direction)

    glutPostRedisplay()

def setup():
    """ Configura o OpenGL """
    glEnable(GL_DEPTH_TEST)  # Ativa teste de profundidade
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75, 800 / 600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)