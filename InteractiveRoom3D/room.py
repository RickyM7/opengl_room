from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from .textures import load_texture
from .core_tools import cores
from .table import draw_table
import math


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

def draw_lamp():
    """ Função para desenhar uma luminária pendurada no teto, apontada para a mesa. """

    # Define a posição da luminária
    lamp_pos_x = 0.0
    lamp_pos_y = 2.0 
    lamp_pos_z = 0.0

    # Luminária: esfera representando a lâmpada
    glPushMatrix()
    glTranslatef(lamp_pos_x, lamp_pos_y, lamp_pos_z)  # Move para o centro da mesa
    glColor3f(1.0, 1.0, 0.0)  # Cor amarela para simular uma luz quente
    glutSolidSphere(0.3, 20, 20)  # Desenha a esfera
    glPopMatrix()

    # Suporte da luminária: um cilindro
    glPushMatrix()
    glTranslatef(lamp_pos_x, lamp_pos_y + 0.3, lamp_pos_z)  # Coloca o suporte acima da lâmpada, mais perto do teto
    glRotatef(-90, 1, 0, 0)
    glColor3f(0.3, 0.3, 0.3)  # Cor cinza para o suporte
    gluCylinder(gluNewQuadric(), 0.05, 0.05, 2.5, 10, 10)
    glPopMatrix()


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

    # Desenha a luminária
    draw_lamp()  # Aqui chamamos a função da luminária

    glDisable(GL_TEXTURE_2D)  # Desativa a textura após o uso