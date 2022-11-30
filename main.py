import verifsecu
import pyautogui
from screenposition import *

# permet de savoir la taille de l'ecran
print(pyautogui.size())

pyautogui.moveTo(firstClick, duration = 1)
pyautogui.click()