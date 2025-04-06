# Quarto 3D Interativo com PyOpenGL

Bem-vindo ao projeto **Quarto 3D Interativo**! Este é um ambiente tridimensional desenvolvido em Python utilizando as bibliotecas **PyOpenGL**, **Pillow** e **NumPy**. O projeto simula um quarto 3D com paredes texturizadas, chão, teto, uma mesa e uma luminária, oferecendo funcionalidades como movimentação da câmera, iluminação dinâmica e aplicação de texturas realistas.

---

## 🎯 **Objetivo**
O objetivo deste projeto é demonstrar conceitos fundamentais de computação gráfica, como:
- **Renderização 3D**: Criação de objetos tridimensionais com texturas e iluminação.
- **Iluminação**: Uso de luz ambiente, difusa e especular para criar realismo.
- **Mapeamento de Texturas**: Aplicação de imagens como texturas em superfícies 3D.
- **Controle de Câmera**: Movimentação e rotação da câmera com sistema de colisão.

Este projeto foi desenvolvido como parte da avaliação final da disciplina de Computação Gráfica.

---

## ✨ **Funcionalidades**
- **Movimentação da Câmera**:
  - Use as teclas **W**, **A**, **S**, **D** para mover a câmera.
  - Rotacione a câmera com o **mouse (botão esquerdo)**.
  - Um sistema de colisão impede que a câmera atravesse paredes, chão, teto ou a mesa.
  
- **Iluminação Dinâmica**:
  - A tecla **Espaço** alterna a luz da luminária entre ligada e desligada.
  - A iluminação afeta o ambiente e a sombra projetada pela mesa.

- **Texturas Realistas**:
  - Paredes, chão, teto e mesa possuem texturas carregadas de imagens JPG.
  - As texturas são aplicadas com repetição para maior realismo.

- **Objetos 3D**:
  - **Mesa**: Tampo texturizado com madeira e pernas sólidas.
  - **Luminária**: Composta por uma esfera (lâmpada) e um cilindro (suporte).

---

## 🛠️ **Requisitos**
Para executar o projeto, você precisará das seguintes dependências:
- **Python 3.8+**
- **PyOpenGL**: `pip install PyOpenGL PyOpenGL_accelerate`
- **Pillow**: `pip install Pillow`
- **NumPy**: `pip install numpy`

---

## 🚀 **Instalação**
1. **Clone este repositório**:

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Nota: Certifique-se de que o arquivo `requirements.txt` contém `PyOpenGL`, `Pillow` e `numpy`.)*

3. **Certifique-se de que as texturas estão no diretório `texturas/`**:
   - `wall.jpg`: Textura das paredes.
   - `floor.jpg`: Textura do chão.
   - `roof.jpg`: Textura do teto.
   - `wood.jpg`: Textura da mesa.

---

## ▶️ **Como Executar**
1. Navegue até o diretório raiz do projeto:
   ```bash
   cd opengl_room
   ```

2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

3. **Controles**:
   - **W, A, S, D**: Movimentar a câmera.
   - **Mouse (botão esquerdo)**: Rotacionar a câmera.
   - **Espaço**: Ligar/desligar a luminária.

---

## 📂 **Estrutura do Projeto**
```
opengl_room/
├── main.py                  # Ponto de entrada do programa
├── InteractiveRoom3D/       # Módulo principal do projeto
│   ├── __init__.py          # Arquivo de inicialização do módulo
│   ├── core.py              # Configurações OpenGL, iluminação e renderização
│   ├── camera.py            # Controle da câmera (movimento e rotação)
│   ├── room.py              # Desenho do quarto e integração de objetos
│   ├── table.py             # Desenho da mesa e sua sombra
│   ├── lamp.py              # Desenho da luminária
│   ├── textures.py          # Carregamento e configuração de texturas
│   ├── core_tools.py        # Definição de cores usadas
├── texturas/                # Diretório com imagens de texturas
│   ├── wall.jpg             # Textura das paredes
│   ├── floor.jpg            # Textura do chão
│   ├── roof.jpg             # Textura do teto
│   ├── wood.jpg             # Textura da mesa
└── README.md                # Este arquivo
```

---

## 🔍 **Detalhes Técnicos**
- **Iluminação**:
  - Configurada com luz ambiente (`[0.1, 0.1, 0.1, 1.0]`), difusa (`[1.5, 1.5, 1.2, 1.0]`) e especular (`[1.0, 1.0, 1.0, 1.0]`).
  - A iluminação é alternada com a tecla **Espaço**.

- **Texturas**:
  - Carregadas com a biblioteca Pillow e aplicadas com `glTexImage2D` e `glBindTexture`.
  - As texturas são configuradas para repetição (`GL_REPEAT`) para maior realismo.

- **Colisão**:
  - Implementada na função `check_collision` em `core.py`.
  - Verifica os limites do quarto e da mesa para impedir que a câmera atravesse objetos.

- **Câmera**:
  - Usa vetores NumPy para calcular direção e posição.
  - A rotação é controlada pelo movimento do mouse.

---

## 💻 **Exemplo de Código**
### Alternância da Luz
```python
# core.py
if key == b' ':  # Tecla espaço
    light_on = not light_on
    if light_on:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
```

### Movimentação da Câmera
```python
# camera.py
if key == b'w':  # Para frente
    camera_pos += direction
elif key == b'a':  # Para a esquerda
    camera_pos -= right
```

---

## 🤝 **Contribuições**
Sinta-se à vontade para contribuir! Faça um fork deste repositório, implemente suas alterações e envie um pull request. Algumas sugestões de melhorias incluem:
- Adicionar mais objetos (cadeiras, janelas, quadros, etc.).
- Implementar animações (como uma lâmpada oscilando).
- Melhorar o sistema de sombras para maior realismo.

---

## 🏆 **Créditos**
Este projeto foi desenvolvido por Sara Abreu, Lucas Victor, Ricardo Martins e Felipe Mendes como parte da avaliação final da disciplina de Computação Gráfica, no curso de Ciência da Computação, oferecido pela Universidade Federal do Agreste de Pernambuco.