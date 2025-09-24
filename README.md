# 🖐 Controle de Programas com Gestos de Mão

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python) ![OpenCV](https://img.shields.io/badge/OpenCV-4+-green?logo=opencv) ![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10-orange)

Um projeto em **Python** que permite **abrir e fechar programas no Windows usando gestos da mão**, detectados em tempo real via **câmera**.

---

## 🎥 Demonstração

![Demo do Controle por Gestos](https://media.giphy.com/media/3o7TKP3VLk7nDq3qYo/giphy.gif)  
*O GIF acima mostra a detecção da mão e a execução dos programas.*

---

## 🖐 Gestos Suportados

| Gestos | Programa | Ação |
|--------|----------|------|
| ✌️ 1 dedo levantado (indicador) | Notepad | Abre o Notepad |
| ✌️ 2 dedos levantados (indicador + médio) | Calculadora | Abre a Calculadora |
| ✌️ 3 dedos levantados (indicador + médio + anelar) | MS Paint | Abre o Paint |
| ✋ Nenhum dedo | Todos | Fecha todos os programas abertos |

> **Dica:** Gestos precisam ser feitos **claramente e estáveis** para melhor reconhecimento.

---


## 🧩 Estrutura do Código

- find_coord_hand(img, side_inverted=False)
Detecta a mão, desenha os pontos, retorna coordenadas e identifica o lado da mão.

- fingers_raised(hand)
Identifica quais dedos estão levantados.

- start_program(program)
Abre um programa via subprocess.

- close_program(process_name)
Fecha um programa usando TASKKILL.

- Loop principal
Captura o vídeo da câmera, detecta gestos e executa ações correspondentes.

---

## 💡 Observações

- Funciona melhor em ambientes bem iluminados.

- A resolução da câmera pode ser ajustada no código (resolution_x e resolution_y).

- É possível adicionar mais gestos e programas editando a função fingers_raised() e as condições do loop principal.


## ⚙️ Instalação

Certifique-se de ter Python 3.7+ instalado. Depois, instale as dependências:

```bash
pip install opencv-python mediapipe

