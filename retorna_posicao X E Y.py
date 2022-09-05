import pyautogui
import keyboard





def Pega_posicao():
    pyautogui.displayMousePosition()
    if keyboard.is_pressed('space') and keyboard.is_pressed('0'):
        exit()
    else:
        print('')
Pega_posicao()    