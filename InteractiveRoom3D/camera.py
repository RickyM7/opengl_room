import numpy as np

# Posição e ângulo da câmera
camera_pos = np.array([0.0, 2.0, 3.0])  # Posição inicial
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