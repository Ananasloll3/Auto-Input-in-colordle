from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import os
import time
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://colourdle.co.uk/"
driver.get(url)

    



def auto_input(location : dict, background : str):
    print("Location div = " + str(location))
    
    os.system("start " + url)
    time.sleep(4)

    background = background[5:18]
    background = background.replace(" ", "")
    background = background.replace(",", "")
    print(background)

    pyautogui.click(location["x"] + 100, location["y"] + 100)
    time.sleep(1)
    
    for i in range(len(background)):
        pyautogui.write(background[i])
        time.sleep(0.3)
        print("Writed : " + background[i])

    time.sleep(0.5)
    pyautogui.press("enter")
    

try:
    # Attendre jusqu'à 10 secondes que l'élément avec la classe "maClasse" soit présent
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "swatch"))
    )

    div = element.find_element(By.TAG_NAME, "div")
    
    background_color = div.value_of_css_property("background-color")
    print("Couleur:", background_color)
    location = div.location
    
    auto_input(location, background_color)

except Exception as e:
    print("L'élément n'a pas été trouvé :", e)
finally:
    driver.quit()
