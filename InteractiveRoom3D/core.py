from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from .room import draw_room
from .camera import camera_pos, camera_front, camera_up, move_camera

# Variáveis para a luz
light_on = False  # Estado inicial da luz (desligada)
light_position = [0.0, 2.0, 0.0, 1.0]  # Posição da luminária
light_ambient = [0.1, 0.1, 0.1, 1.0]  # Luz ambiente um pouco mais clara
light_diffuse = [1.5, 1.5, 1.2, 1.0]  # Luz difusa mais intensa (levemente amarelada)
light_specular = [1.0, 1.0, 1.0, 1.0]  # Luz especular branca

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

def keyboard(key, x, y):
    """Gerencia a movimentação do usuário e a tecla espaço para a luz"""
    global light_on

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