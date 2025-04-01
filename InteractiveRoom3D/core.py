from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from .room import draw_room
from .camera import camera_pos, camera_front, camera_up, move_camera, speed
import numpy as np

# Variáveis para a luz
light_on = False  # Estado inicial da luz (desligada)
light_position = [0.0, 2.0, 0.0, 1.0]  # Posição da luminária
light_ambient = [0.1, 0.1, 0.1, 1.0]  # Luz ambiente um pouco mais clara
light_diffuse = [1.5, 1.5, 1.2, 1.0]  # Luz difusa mais intensa (levemente amarelada)
light_specular = [1.0, 1.0, 1.0, 1.0]  # Luz especular branca

# Limites do quarto
room_limits = {
    "x_min": -5.0,
    "x_max": 5.0,
    "y_min": 0.5,  # Altura mínima (acima do chão)
    "y_max": 5.0,  # Altura máxima (abaixo do teto)
    "z_min": -5.0,
    "z_max": 5.0
}

# Limites da mesa (opcional, para evitar colisão com a mesa)
table_limits = {
    "x_min": -1.1,
    "x_max": 1.1,
    "y_min": 0.9,  # Altura do tampo da mesa
    "y_max": 1.0,
    "z_min": -0.6,
    "z_max": 0.6
}

def init():
    """Inicializa as configurações do OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fundo preto
    glEnable(GL_DEPTH_TEST)

    # Habilitar iluminação
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Configurar a luz da luminária
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # Ajustar a atenuação para que a luz alcance mais longe
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)  # Reduzir a atenuação linear
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.005)  # Reduzir a atenuação quadrática

    # Desativar a luz inicialmente
    if light_on:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)

    # Sombreamento suave
    glShadeModel(GL_SMOOTH)

def display():
    """Renderiza a cena"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Define a câmera
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],
              camera_pos[0] + camera_front[0], camera_pos[1] + camera_front[1], camera_pos[2] + camera_front[2],
              camera_up[0], camera_up[1], camera_up[2])

    # Atualiza a posição da luz
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Desenha o quarto, passando o estado da luz
    draw_room(light_on)

    glutSwapBuffers()

def check_collision(new_pos):
    """Verifica se a nova posição da câmera está dentro dos limites"""
    # Verifica os limites do quarto
    if not (room_limits["x_min"] <= new_pos[0] <= room_limits["x_max"]):
        return False
    if not (room_limits["y_min"] <= new_pos[1] <= room_limits["y_max"]):
        return False
    if not (room_limits["z_min"] <= new_pos[2] <= room_limits["z_max"]):
        return False

    # Verifica os limites da mesa (opcional)
    if (table_limits["x_min"] <= new_pos[0] <= table_limits["x_max"] and
        table_limits["y_min"] <= new_pos[1] <= table_limits["y_max"] and
        table_limits["z_min"] <= new_pos[2] <= table_limits["z_max"]):
        return False

    return True

def keyboard(key, x, y):
    """Gerencia a movimentação do usuário e a tecla espaço para a luz"""
    global light_on, camera_pos

    direction = camera_front * speed
    right = np.cross(camera_front, camera_up) * speed
    new_pos = camera_pos.copy()

    if key == b'w':  # Para frente
        new_pos += direction
    elif key == b's':  # Para trás
        new_pos -= direction
    elif key == b'a':  # Para a esquerda
        new_pos -= right
    elif key == b'd':  # Para a direita
        new_pos += right

    # Verifica colisão antes de atualizar a posição
    if check_collision(new_pos):
        camera_pos = new_pos
    # Movimentação da câmera
    move_camera(key, x, y)

    # Controle da luz
    if key == b' ':  # Tecla espaço
        light_on = not light_on  # Alterna o estado da luz
        if light_on:
            glEnable(GL_LIGHT0)  # Acende a luz
        else:
            glDisable(GL_LIGHT0)  # Apaga a luz

    glutPostRedisplay()

def setup():
    """Configura o OpenGL"""
    glEnable(GL_DEPTH_TEST)  # Ativa teste de profundidade
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75, 800 / 600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)