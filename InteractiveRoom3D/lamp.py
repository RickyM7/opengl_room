from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_lamp(light_on):
    """Função para desenhar uma luminária pendurada no teto, apontada para a mesa."""
    # Define a posição da luminária
    lamp_pos_x = 0.0
    lamp_pos_y = 2.0
    lamp_pos_z = 0.0

    # Luminária: esfera representando a lâmpada
    glPushMatrix()
    glTranslatef(lamp_pos_x, lamp_pos_y, lamp_pos_z)  # Move para o centro da mesa
    glDisable(GL_LIGHTING)  # Desativa a iluminação para a esfera
    if light_on:
        glColor3f(1.0, 1.0, 1.0)  # Branco puro para simular luz acesa
    else:
        glColor3f(0.2, 0.2, 0.2)  # Cinza bem escuro para simular a lâmpada apagada
    glutSolidSphere(0.3, 20, 20)  # Desenha a esfera
    glEnable(GL_LIGHTING)  # Reativa a iluminação
    glPopMatrix()

    # Suporte da luminária: um cilindro
    glPushMatrix()
    glTranslatef(lamp_pos_x, lamp_pos_y + 0.3, lamp_pos_z)  # Coloca o suporte acima da lâmpada
    glRotatef(-90, 1, 0, 0)
    glColor3f(0.3, 0.3, 0.3)  # Cor cinza para o suporte
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluCylinder(quadric, 0.05, 0.05, 2.5, 10, 10)
    glPopMatrix()