import numpy as np

# Posição e ângulo da câmera
camera_pos = np.array([0.0, 2.0, 3.0])  # Posição inicial
camera_front = np.array([0.0, 0.0, -1.0])  # Direção inicial
camera_up = np.array([0.0, 1.0, 0.0])  # Vetor para cima

# Variáveis para controlar a rotação do mouse
angle_x = 1.0
angle_y = -1.0
last_x = 0
last_y = 0
left_button_down = False
right_button_down = False

# Configurações de movimento
speed = 0.05  # Velocidade de movimento
sensitivity = 0.01  # Sensibilidade do mouse