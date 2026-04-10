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


def getColor(background_color : str):
    background_color = background_color[5:15]
    backgound_color = background_color.replace(" ", "")
    backgound_color = background_color.replace(")", "")
    backgound_color = background_color.replace("(", "")

    backgound = background_color.split(",")
    finalBack = "";

    for i in range(len(backgound)):
        backgound[i] = backgound[i].replace(" ", "")
        
        if len(backgound[i]) == 1:
            backgound[i] = "00" + backgound[i]
        elif len(backgound[i]) == 2:
            backgound[i] = "0" + backgound[i]
        finalBack += backgound[i]
        
    return finalBack



def auto_input(location : dict, background : str):
    print("Location div = " + str(location))
    
    os.system("start " + url)
    time.sleep(4)
    
    finalBack = getColor(background)
    print("Final background : " + finalBack)

    pyautogui.click(location["x"] + 100, location["y"] + 100)
    time.sleep(1)
    
    for i in range(len(finalBack)):
        pyautogui.write(finalBack[i])
        time.sleep(0.3)
        print("Writed : " + finalBack[i])

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
