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

def mouse_button(button, state, x, y):
    """Callback para eventos de clique do mouse"""
    global left_button_down, right_button_down, last_x, last_y

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            left_button_down = True
            last_x = x
            last_y = y
        elif state == GLUT_UP:
            left_button_down = False

    elif button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            right_button_down = True
            last_x = x
            last_y = y
        elif state == GLUT_UP:
            right_button_down = False


def mouse_motion(x, y):
    """Callback para eventos de movimento do mouse"""
    global angle_x, angle_y, last_x, last_y, camera_front

    if left_button_down:
        # Calcula a mudança de posição do mouse
        dx = x - last_x
        dy = y - last_y

        # Ajusta os ângulos (inverte dx e dy para movimento natural)
        angle_y += dx * 0.5  # Rotação horizontal (yaw)
        angle_x -= dy * 0.5  # Rotação vertical (pitch) - inverte dy

        # Limita a rotação vertical para evitar flips
        angle_x = max(-70, min(70, angle_x))  # Limite mais natural (-89° a 89°)
        angle_y = max(-60, min(60, angle_y))  # Limite mais natural (-89° a 89°)

        # Converte para radianos
        yaw = np.radians(angle_y)
        pitch = np.radians(angle_x)

        # Calcula o novo vetor camera_front
        camera_front[0] = np.cos(pitch) * np.sin(yaw)  # X
        camera_front[1] = np.sin(pitch)                # Y
        camera_front[2] = -np.cos(pitch) * np.cos(yaw) # Z

        # Atualiza as últimas posições do mouse
        last_x = x
        last_y = y

        # Redesenha a cena
        glutPostRedisplay()

    elif right_button_down:
        dy = y - last_y
        last_y = y
        glutPostRedisplay()


def setup():
    """ Configura o OpenGL """
    glEnable(GL_DEPTH_TEST)  # Ativa teste de profundidade
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75, 800 / 600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)