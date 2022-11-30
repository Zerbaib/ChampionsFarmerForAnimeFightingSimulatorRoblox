import pyautogui
from screenposition import *

# permet de savoir la taille de l'ecran
print(pyautogui.size())

def loop():
    # afficher le menue acheter
    pyautogui.moveTo(AchtMenu, duration = 1)
    pyautogui.click()

    # Bouton acheter
    pyautogui.moveTo(AchtClick, duration = 1)
    pyautogui.click()

# verif a faire si noir ou non

    # si pas noir
    pyautogui.moveTo(ProfilClick, duration = 5) # allez dans le menue perso
    pyautogui.click()

    # Allez dans le menu des champion pour vendre
    pyautogui.moveTo(ChampClick, duration = 1)
    pyautogui.click()

    # Allez dans le menue de vante du chamion
    pyautogui.moveTo(VendrMenu, duration = 1)
    pyautogui.click()
    # click et valider
    pyautogui.moveTo(VendreClick, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(ValidClick, duration = 1)
    pyautogui.click()

    # reboot
    pyautogui.moveTo(close, duration = 1)
    pyautogui.click()