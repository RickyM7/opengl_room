from OpenGL.GL import *
from .textures import load_texture
# from .core import light_position
from .core_tools import cores
from .table import draw_table, draw_table_shadow
from .lamp import draw_lamp

# Variáveis globais para texturas
wall_texture = None
floor_texture = None
roof_texture = None
wood_texture = None

def init_textures():
    """Carrega e configura as texturas"""
    global wall_texture, floor_texture, roof_texture, wood_texture
    glEnable(GL_TEXTURE_2D)
    wall_texture = load_texture("texturas/wall.jpg")
    floor_texture = load_texture("texturas/floor.jpg")
    roof_texture = load_texture("texturas/roof.jpg")
    wood_texture = load_texture("texturas/wood.jpg")

    # Configura o modo de repetição para as texturas
    glBindTexture(GL_TEXTURE_2D, wall_texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glBindTexture(GL_TEXTURE_2D, floor_texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glBindTexture(GL_TEXTURE_2D, roof_texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

def draw_room(light_on):
    """Desenha um quarto com paredes texturizadas de tijolos, chão e teto."""
    init_textures()  # Carrega as texturas

    # Chão
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, floor_texture)  # Aplica a textura do chão
    glBegin(GL_QUADS)
    glColor3fv(cores[8])  # Cor branca
    glNormal3f(0.0, 1.0, 0.0)

    # Repete a textura 5 vezes em ambas as direções
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
    glBindTexture(GL_TEXTURE_2D, roof_texture)  # Aplica a textura do teto
    glBegin(GL_QUADS)
    glColor3fv(cores[8])  # Cor branca
    glNormal3f(0.0, -1.0, 0.0)

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
    glBindTexture(GL_TEXTURE_2D, wall_texture)  # Aplica a textura da parede
    glBegin(GL_QUADS)
    glColor3fv(cores[8])  # Cor branca para as paredes
    glNormal3f(1.0, 0.0, 0.0)

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
    glNormal3f(-1.0, 0.0, 0.0)
    glTexCoord2f(0, 0)
    glVertex3f(5.0, 0.0, 5.0)
    glTexCoord2f(0, 5)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2f(10, 5)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2f(10, 0)
    glVertex3f(5.0, 0.0, -5.0)

    # Parede do fundo
    glNormal3f(0.0, 0.0, 1.0)
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
    draw_table_shadow(light_on)

    # Desenha a luminária
    draw_lamp(light_on)

    glDisable(GL_TEXTURE_2D)  # Desativa a textura após o uso