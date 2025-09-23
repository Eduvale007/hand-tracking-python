import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

camera = cv2.VideoCapture(0) # se o valor for 0 é camêra do notebook se for 1 é a camêra externa
resolution_x = 1280 # define a qualidade da imagem
resolution_y = 720  # define a qualidade da imagem
camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x) # passa a configuracao da qualidade da imagem
camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_y) # passa a configuracao da qualidade da imagem

def find_coord_hand(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #conversão de BGR2 PARA RGB
    result = hands.process(img_rgb)
    all_hands = []
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            for mark in hand_landmarks.landmark: #responsavel por mostrar as coordenadas da mão
                hand_info = {} # cria uma tupla para guardar informacoes das maos
                coords = [] # cria uma lista para guardar as coordenadas
                coord_x = int(mark.x * resolution_x)
                coord_y = int(mark.y * resolution_y)
                coord_z = int(mark.z * resolution_x)
                coords.append((coord_x, coord_y, coord_z)) #guardas as posicoes x, y e z na lista
                hand_info['coordenadas'] = coords # hand_info recebe coordenadas
                all_hands.append(hand_info) #all hands recebe as coordenadas das maos
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS) #desenhar os pontos e conexoes das maos
    
    return img, all_hands

while camera.isOpened():
    ret, frame = camera.read() # captura os dados da imagem e a imagem
    
    
    if not ret:
        print('Frame vazio') # se não capturou os dados é porque deu erro
        continue # caso contrario continue
    img, all_hands = find_coord_hand(frame)
    cv2.imshow('Camera', img) # funcao para abrir a camera
    key = cv2.waitKey(1) # tempo de aguardo de 1 segundo para sair do loop
    if key == 27: # se a tecla for esc encerra o programa
        break






