from OpenGL.GL import *

def draw_table_shadow(light_on):
    """Desenha uma sombra projetada da mesa no chão"""
    if not light_on:
        return  # Não desenha sombra se a luz estiver apagada

    # Define a posição da sombra no chão (y = 0.01 para evitar z-fighting com o chão)
    shadow_y = 0.01
    table_width = 2.2  # Largura da mesa (x)
    table_depth = 1.2  # Profundidade da mesa (z)

    # Ajusta a posição da sombra para diretamente abaixo da mesa
    shadow_x_offset = 0.0
    shadow_z_offset = 0.0

    # Escurecimento da sombra (cinza escuro semi-transparente)
    glEnable(GL_BLEND)  # Ativa blending para transparência
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glDisable(GL_LIGHTING)  # Desativa iluminação para a sombra

    glBegin(GL_QUADS)
    glColor4f(0.0, 0.0, 0.0, 0.5)  # Preto com 50% de opacidade
    glVertex3f(-table_width / 2 + shadow_x_offset, shadow_y, -table_depth / 2 + shadow_z_offset)
    glVertex3f(table_width / 2 + shadow_x_offset, shadow_y, -table_depth / 2 + shadow_z_offset)
    glVertex3f(table_width / 2 + shadow_x_offset, shadow_y, table_depth / 2 + shadow_z_offset)
    glVertex3f(-table_width / 2 + shadow_x_offset, shadow_y, table_depth / 2 + shadow_z_offset)
    glEnd()

    glEnable(GL_LIGHTING)  # Reativa iluminação
    glDisable(GL_BLEND)  # Desativa blending

def draw_table(wood_texture, cores):
    """Desenha uma mesa com textura de madeira"""
    # Tampo (2.2x0.1x1.2, altura de 0.9 a 1.0)
    glBindTexture(GL_TEXTURE_2D, wood_texture)
    glBegin(GL_QUADS)
    glColor3fv(cores[8])  # Cor branca para a textura

    # Face superior
    glNormal3f(0.0, 1.0, 0.0)
    glTexCoord2f(0, 0)
    glVertex3f(-1.1, 1.0, -0.6)
    glTexCoord2f(2.2, 0)
    glVertex3f(1.1, 1.0, -0.6)
    glTexCoord2f(2.2, 1.2)
    glVertex3f(1.1, 1.0, 0.6)
    glTexCoord2f(0, 1.2)
    glVertex3f(-1.1, 1.0, 0.6)

    # Face inferior (menos iluminada, simulando sombra)
    glNormal3f(0.0, -1.0, 0.0)
    glColor3f(0.3, 0.3, 0.3)  # Escurecer a face inferior
    glTexCoord2f(0, 0)
    glVertex3f(-1.1, 0.9, -0.6)
    glTexCoord2f(2.2, 0)
    glVertex3f(1.1, 0.9, -0.6)
    glTexCoord2f(2.2, 1.2)
    glVertex3f(1.1, 0.9, 0.6)
    glTexCoord2f(0, 1.2)
    glVertex3f(-1.1, 0.9, 0.6)

    # Face frontal
    glNormal3f(0.0, 0.0, 1.0)
    glColor3fv(cores[8])  # Voltar para a cor branca
    glTexCoord2f(0, 0)
    glVertex3f(-1.1, 0.9, 0.6)
    glTexCoord2f(2.2, 0)
    glVertex3f(1.1, 0.9, 0.6)
    glTexCoord2f(2.2, 0.1)
    glVertex3f(1.1, 1.0, 0.6)
    glTexCoord2f(0, 0.1)
    glVertex3f(-1.1, 1.0, 0.6)

    # Face traseira
    glNormal3f(0.0, 0.0, -1.0)
    glTexCoord2f(0, 0)
    glVertex3f(-1.1, 0.9, -0.6)
    glTexCoord2f(2.2, 0)
    glVertex3f(1.1, 0.9, -0.6)
    glTexCoord2f(2.2, 0.1)
    glVertex3f(1.1, 1.0, -0.6)
    glTexCoord2f(0, 0.1)
    glVertex3f(-1.1, 1.0, -0.6)

    # Face esquerda
    glNormal3f(-1.0, 0.0, 0.0)
    glTexCoord2f(0, 0)
    glVertex3f(-1.1, 0.9, -0.6)
    glTexCoord2f(1.2, 0)
    glVertex3f(-1.1, 0.9, 0.6)
    glTexCoord2f(1.2, 0.1)
    glVertex3f(-1.1, 1.0, 0.6)
    glTexCoord2f(0, 0.1)
    glVertex3f(-1.1, 1.0, -0.6)

    # Face direita
    glNormal3f(1.0, 0.0, 0.0)
    glTexCoord2f(0, 0)
    glVertex3f(1.1, 0.9, 0.6)
    glTexCoord2f(1.2, 0)
    glVertex3f(1.1, 0.9, -0.6)
    glTexCoord2f(1.2, 0.1)
    glVertex3f(1.1, 1.0, -0.6)
    glTexCoord2f(0, 0.1)
    glVertex3f(1.1, 1.0, 0.6)
    glEnd()

    # Pernas (sem textura, só uma cor parecida com madeira)
    glDisable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.15, 0.05)  # Escurecer as pernas para simular sombra

    # Perna 1 (frente esquerda)
    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.45)
    glVertex3f(-1.0, 0.0, 0.55)
    glVertex3f(-1.0, 0.9, 0.55)
    glVertex3f(-1.0, 0.9, 0.45)

    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, 0.0, 0.45)
    glVertex3f(-0.9, 0.0, 0.55)
    glVertex3f(-0.9, 0.9, 0.55)
    glVertex3f(-0.9, 0.9, 0.45)

    glNormal3f(0.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, 0.45)
    glVertex3f(-0.9, 0.0, 0.45)
    glVertex3f(-0.9, 0.9, 0.45)
    glVertex3f(-1.0, 0.9, 0.45)

    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, 0.55)
    glVertex3f(-0.9, 0.0, 0.55)
    glVertex3f(-0.9, 0.9, 0.55)
    glVertex3f(-1.0, 0.9, 0.55)

    # Perna 2 (frente direita)
    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.45)
    glVertex3f(1.0, 0.0, 0.55)
    glVertex3f(1.0, 0.9, 0.55)
    glVertex3f(1.0, 0.9, 0.45)

    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(0.9, 0.0, 0.45)
    glVertex3f(0.9, 0.0, 0.55)
    glVertex3f(0.9, 0.9, 0.55)
    glVertex3f(0.9, 0.9, 0.45)

    glNormal3f(0.0, 0.0, -1.0)
    glVertex3f(0.9, 0.0, 0.45)
    glVertex3f(1.0, 0.0, 0.45)
    glVertex3f(1.0, 0.9, 0.45)
    glVertex3f(0.9, 0.9, 0.45)

    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(0.9, 0.0, 0.55)
    glVertex3f(1.0, 0.0, 0.55)
    glVertex3f(1.0, 0.9, 0.55)
    glVertex3f(0.9, 0.9, 0.55)

    # Perna 3 (trás esquerda)
    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, -0.55)
    glVertex3f(-1.0, 0.0, -0.45)
    glVertex3f(-1.0, 0.9, -0.45)
    glVertex3f(-1.0, 0.9, -0.55)

    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, 0.0, -0.55)
    glVertex3f(-0.9, 0.0, -0.45)
    glVertex3f(-0.9, 0.9, -0.45)
    glVertex3f(-0.9, 0.9, -0.55)

    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -0.45)
    glVertex3f(-0.9, 0.0, -0.45)
    glVertex3f(-0.9, 0.9, -0.45)
    glVertex3f(-1.0, 0.9, -0.45)

    glNormal3f(0.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, -0.55)
    glVertex3f(-0.9, 0.0, -0.55)
    glVertex3f(-0.9, 0.9, -0.55)
    glVertex3f(-1.0, 0.9, -0.55)

    # Perna 4 (trás direita)
    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, -0.55)
    glVertex3f(1.0, 0.0, -0.45)
    glVertex3f(1.0, 0.9, -0.45)
    glVertex3f(1.0, 0.9, -0.55)

    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(0.9, 0.0, -0.55)
    glVertex3f(0.9, 0.0, -0.45)
    glVertex3f(0.9, 0.9, -0.45)
    glVertex3f(0.9, 0.9, -0.55)

    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(0.9, 0.0, -0.45)
    glVertex3f(1.0, 0.0, -0.45)
    glVertex3f(1.0, 0.9, -0.45)
    glVertex3f(0.9, 0.9, -0.45)

    glNormal3f(0.0, 0.0, -1.0)
    glVertex3f(0.9, 0.0, -0.55)
    glVertex3f(1.0, 0.0, -0.55)
    glVertex3f(1.0, 0.9, -0.55)
    glVertex3f(0.9, 0.9, -0.55)
    glEnd()