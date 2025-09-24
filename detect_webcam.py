import cv2
import mediapipe as mp
import subprocess
import os
# Programas

notepad_process = None
mspaint_process = None
calc_process = None


def start_program(program):
    return subprocess.Popen(program, shell=True)

def close_program(process_name):
    os.system(f"TASKKILL /IM {process_name} /F")

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

camera = cv2.VideoCapture(0) # se o valor for 0 é camêra do notebook se for 1 é a camêra externa
resolution_x = 1280 # define a qualidade da imagem
resolution_y = 720  # define a qualidade da imagem
camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x) # passa a configuracao da qualidade da imagem
camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_y) # passa a configuracao da qualidade da imagem

def find_coord_hand(img, side_inverted = False):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #conversão de BGR2 PARA RGB
    result = hands.process(img_rgb)
    all_hands = []
    hand_info = {} # cria uma tupla para guardar informacoes das maos
    coords = [] # cria uma lista para guardar as coordenadas
    if result.multi_hand_landmarks:
        for hand_side, hand_landmarks in zip(result.multi_handedness,result.multi_hand_landmarks):
            for mark in hand_landmarks.landmark: #responsavel por mostrar as coordenadas da mão
               
                coord_x = int(mark.x * resolution_x)
                coord_y = int(mark.y * resolution_y)
                coord_z = int(mark.z * resolution_x)
                coords.append((coord_x, coord_y, coord_z)) #guardas as posicoes x, y e z na lista
            hand_info['coordenadas'] = coords # hand_info recebe coordenadas
            if side_inverted:
                if hand_side.classification[0].label == "Left":
                    hand_info["side"] = "Right"
                else:
                    hand_info["side"] = "Left" 
            else:
                hand_info["side"] = hand_side.classification[0].label   

            all_hands.append(hand_info) #all hands recebe as coordenadas das maos

            print(hand_info["side"])

            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS) #desenhar os pontos e conexoes das maos
    
    return img, all_hands


def fingers_raised(hand):
    fingers = []
    for fingertip in [8,12,16,20]:
        if hand['coordenadas'][fingertip][1] < hand['coordenadas'][fingertip-2][1]:
            # coorndenada y | posicao media do dedo
            fingers.append(True)
        else:
            fingers.append(False)

    return fingers               

while camera.isOpened():
    ret, frame = camera.read() # captura os dados da imagem e a imagem
    frame = cv2.flip(frame,1) # inverte esquerda pela direita
    
    if not ret:
        print('Frame vazio') # se não capturou os dados é porque deu erro
        continue # caso contrario continue
    img, all_hands = find_coord_hand(frame, False)
    if len(all_hands) == 1:
        info_finger_hand = fingers_raised(all_hands[0])
        if info_finger_hand == [True, False, False, True]:
            break
        elif info_finger_hand == [True, False, False, False] and notepad_process is None:
            notepad_process = start_program("notepad")
        elif info_finger_hand == [True, True, False, False] and calc_process is None:
            calc_process = start_program("calc")
        elif info_finger_hand == [True, True, True, False] and mspaint_process is None:
            mspaint_process = start_program("mspaint")
        elif info_finger_hand == [False, False, False, False]:
            if notepad_process is not None:
                close_program("notepad.exe")
                notepad_process = None
            if calc_process is not None:
                close_program("CalculatorApp.exe")
                calc_process = None
            if mspaint_process is not None:
                close_program("mspaint.exe")
                mspaint_process = None                   
    cv2.imshow('Camera', img) # funcao para abrir a camera
    key = cv2.waitKey(1) # tempo de aguardo de 1 segundo para sair do loop
    if key == 27: # se a tecla for esc encerra o programa
        break






