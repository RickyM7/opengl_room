import numpy as np

# Posição e ângulo da câmera
camera_pos = np.array([0.0, 1.0, 0.0])  # Posição inicial
camera_front = np.array([0.0, 0.0, -1.0])  # Direção inicial
camera_up = np.array([0.0, 1.0, 0.0])  # Vetor para cima

# Controle de rotação do mouse
yaw = -90.0  # Inicialmente olhando para frente (sentido Z negativo)
pitch = 0.0
last_x, last_y = 400, 300
first_mouse = True

# Configurações de movimento
speed = 0.05  # Velocidade de movimento
sensitivity = 0.1  # Sensibilidade do mouse

def update_camera_direction(x, y):
    """ Atualiza a direção da câmera com o movimento do mouse """
    global yaw, pitch, last_x, last_y, first_mouse, camera_front

    if first_mouse:
        last_x, last_y = x, y
        first_mouse = False

    # Calcula deslocamento do mouse
    x_offset = (x - last_x) * sensitivity
    y_offset = (last_y - y) * sensitivity  # Invertido porque o OpenGL tem Y ao contrário
    last_x, last_y = x, y

    # Atualiza ângulos
    yaw += x_offset
    pitch += y_offset

    # Restringe o pitch para evitar giros indesejados
    pitch = max(-89.0, min(89.0, pitch))

    # Calcula nova direção da câmera
    direction = np.array([
        np.cos(np.radians(yaw)) * np.cos(np.radians(pitch)),
        np.sin(np.radians(pitch)),
        np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
    ])
    camera_front = direction / np.linalg.norm(direction)