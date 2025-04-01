import numpy as np
from OpenGL.GLUT import *

# Variáveis globais para a câmera
camera_pos = np.array([0.0, 2.0, 3.0])  # Posição inicial
camera_front = np.array([0.0, 0.0, -1.0])  # Direção inicial
camera_up = np.array([0.0, 1.0, 0.0])  # Vetor para cima

# Variáveis para controlar a rotação do mouse
angle_x = 1.0
angle_y = -1.0
last_x = 0
last_y = 0
left_button_down = False
right_button_down = False

# Configurações de movimento
speed = 0.05  # Velocidade de movimento
sensitivity = 0.01  # Sensibilidade do mouse

def move_camera(key, x, y):
    """Gerencia a movimentação da câmera usando WASD"""
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

        # Redesenha a cena a cada movimento do mouse
        glutPostRedisplay()

    elif right_button_down:
        dy = y - last_y
        last_y = y
        glutPostRedisplay()