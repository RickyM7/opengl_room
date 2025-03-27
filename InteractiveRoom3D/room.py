from OpenGL.GL import *
from .textures import load_texture
from .core_tools import cores

def init():
    # carrega as texturas
    global wall_texture
    glEnable(GL_TEXTURE_2D)
    wall_texture = load_texture("texturas/wall.jpg")

def draw_room():
    init()
    """ Desenha um quarto com paredes, chão e teto vermelhos. """
    glBegin(GL_QUADS)
    glColor3fv(cores[0])  # Cor vermelha

    # Chão
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5.0, 0.0, -5.0)
    glVertex3f(5.0, 0.0, 5.0)
    glVertex3f(-5.0, 0.0, 5.0)

    # Teto
    glColor3fv(cores[0])  # Cor vermelha

    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)

    glEnd()

    # Parede esquerda
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, wall_texture)  # Aplica a textura da parede esquerda
    glBegin(GL_QUADS)

    glColor3fv(cores[8])  # Cor Branca para as paredes

    glTexCoord2f(0, 0); glVertex3f(-5.0, 0.0, -5.0)
    glTexCoord2f(1, 0); glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2f(1, 1); glVertex3f(-5.0, 5.0, 5.0)
    glTexCoord2f(0, 1); glVertex3f(-5.0, 0.0, 5.0)

    # Parede direita

    glTexCoord2f(0, 0); glVertex3f(5.0, 0.0, 5.0)
    glTexCoord2f(1, 0); glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2f(1, 1); glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(0, 1); glVertex3f(5.0, 0.0, -5.0)

    # Parede do fundo

    glTexCoord2f(0, 0); glVertex3f(5.0, 0.0, -5.0)
    glTexCoord2f(1, 0); glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(1, 1); glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2f(0, 1); glVertex3f(-5.0, 0.0, -5.0)

    glEnd()