from OpenGL.GL import *
from .textures import load_texture
from .core_tools import cores
from .table import draw_table


def init():
    # Carrega as texturas
    global wall_texture, floor_texture, sky_texture, wood_texture
    glEnable(GL_TEXTURE_2D)
    wall_texture = load_texture("texturas/wall.jpg")
    floor_texture = load_texture("texturas/floor.jpg")
    sky_texture = load_texture("texturas/sky.jpg")
    wood_texture = load_texture("texturas/wood.jpg")

    # Configura o modo de repetição para as texturas
    glBindTexture(GL_TEXTURE_2D, wall_texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glBindTexture(GL_TEXTURE_2D, floor_texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glBindTexture(GL_TEXTURE_2D, sky_texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)


def draw_room():
    init()
    """ Desenha um quarto com paredes texturizadas de tijolos, chão com textura de madeira repetida e teto vermelho. """

    # Chão
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, floor_texture)  # Aplica a textura do chão
    glBegin(GL_QUADS)
    glColor3fv(cores[8])  # Cor branca

    # Repete a textura 5 vezes em ambas as direções (10 unidades de largura/profundidade)
    glTexCoord2f(0, 0)
    glVertex3f(-5.0, 0.0, -5.0)
    glTexCoord2f(5, 0)
    glVertex3f(5.0, 0.0, -5.0)
    glTexCoord2f(5, 5)
    glVertex3f(5.0, 0.0, 5.0)
    glTexCoord2f(0, 5)
    glVertex3f(-5.0, 0.0, 5.0)

    glEnd()

    # Teto
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, sky_texture)  # Aplica a textura do teto
    glBegin(GL_QUADS)
    glColor3fv(cores[8])  # Cor branca

    glTexCoord2f(0, 0)
    glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2f(5, 0)
    glVertex3f(-5.0, 5.0, 5.0)
    glTexCoord2f(5, 5)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2f(0, 5)
    glVertex3f(5.0, 5.0, -5.0)

    glEnd()

    # Parede esquerda
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, wall_texture)  # Aplica a textura da parede
    glBegin(GL_QUADS)
    glColor3fv(cores[8])  # Cor branca para as paredes

    # Repete a textura 10 vezes horizontalmente e 5 vezes verticalmente
    glTexCoord2f(0, 0)
    glVertex3f(-5.0, 0.0, -5.0)
    glTexCoord2f(0, 5)
    glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2f(10, 5)
    glVertex3f(-5.0, 5.0, 5.0)
    glTexCoord2f(10, 0)
    glVertex3f(-5.0, 0.0, 5.0)

    # Parede direita
    glTexCoord2f(0, 0)
    glVertex3f(5.0, 0.0, 5.0)
    glTexCoord2f(0, 5)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2f(10, 5)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(10, 0)
    glVertex3f(5.0, 0.0, -5.0)

    # Parede do fundo
    glTexCoord2f(0, 0)
    glVertex3f(5.0, 0.0, -5.0)
    glTexCoord2f(0, 5)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(10, 5)
    glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2f(10, 0)
    glVertex3f(-5.0, 0.0, -5.0)

    glEnd()

    # Mesa
    draw_table(wood_texture, cores)

    glDisable(GL_TEXTURE_2D)  # Desativa a textura após o uso