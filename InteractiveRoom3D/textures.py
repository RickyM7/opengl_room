from OpenGL.GL import *
from PIL import Image
import numpy as np

def load_texture(filename):
    """Carrega uma imagem e converte para textura do OpenGL"""
    image = Image.open(filename)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Inverte para alinhar com OpenGL
    img_data = np.array(image, dtype=np.uint8)  # Converte para array

    # Gera um ID de textura e configura os parâmetros
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Envia a textura para o OpenGL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0,
                 GL_RGB, GL_UNSIGNED_BYTE, img_data)

    return texture_id