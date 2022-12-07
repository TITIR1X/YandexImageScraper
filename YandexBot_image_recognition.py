import URLS_
from bs4 import BeautifulSoup
import re, time, requests, shutil, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from threading import Thread, Barrier
from datetime import datetime
from collections import defaultdict

# webdriver_config: #
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(r"--user-data-dir=C:\Users\Santi\AppData\Local\Google\Chrome\User Data")
options.add_argument("window-size=1200x800")
driver = webdriver.Chrome(executable_path=r'webdriver//chromedriver.exe', chrome_options=options)

os.system('cls')
print("""
 ./YandexBot_image_recognition.py
  ____              _______ _   ______ _       ___ __    __
 |  _ \            /__   __(_)/__   __(_) _ __|_| |\ \\  / /
 | |_) |_   _         | |   _    | |   _ | '__| | | \ \\/ /
 |  _ <| | | |        | | 0| |   | |  | || |    | |  \  \\
 | |_) | |_| |        | | /| |   | |  | || |    | | / /\ \\
 |____/ \__, |        |_| /|_|   |_|  |_||_|    |_|/_/  \_\\
         __/ |                                               
        |___/                           
""")

### C O N F I G U R A R ###


carpeta_salida = 'recognition_images_src'
if not os.path.exists(carpeta_salida):
    os.mkdir(carpeta_salida)

limite = 1400

images_src_list = URLS_.images_src_list

comenzar_desde = 1


count = comenzar_desde - 1
count2 = count + 1

while count < len(images_src_list):
    print(f'\n [{count2} de {len(images_src_list)}] \n .. \n Trabajando...')
    time.sleep(1)

    driver.get("https://yandex.com/images")
    driver.find_element("xpath",'/html/body/header/div/div[2]/div[1]/form/div[1]/span/span/button/div').click()
    time.sleep(1)
    driver.maximize_window()
    driver.find_element("xpath", '/html/body/header/div/div[3]/div[1]/form/span/input').send_keys(images_src_list[count])
    driver.find_element("xpath", '/html/body/header/div/div[3]/div[1]/form/button').click()

    count +=1
    a=0
    while a == 0:
        try:
            time.sleep(2)
            driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/section/a').click()
            a = 1
        except:
            try:
                driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/section/a').click()
                a = 1
            except:pass
            
    count_img = 1
    contador = 0
    src_list = []
    while contador <= limite:
        print(f'refrescando página.. {contador} de {limite}')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            driver.find_element("xpath", f'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[{contador}]/div/a/img').text()
            count_img +=1
        except:pass
        contador +=1

    contador = 1
    while contador != limite:
        try:
            driver.maximize_window()
            src = driver.find_element("xpath", f'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[{contador}]/div/a/img').get_attribute("src")
            contador += 1
            src_list.append(src)
            print(f'{len(src_list)} links IMG\'s adquiridas!')
        except:contador += 1
    
    with open(f'{carpeta_salida}/src{count2}.html', 'w') as fp:
        for src in src_list:
            fp.write('%s.jpg">\n' % src + '<img src="')

    print(f'\n[{count2} de {len(images_src_list)}] ok\n')
    cant_src = len(src_list)
    cant_src_list = []
    cant_src_list.append
    count2+=1


with open(f'{carpeta_salida}/all_images_src.txt', 'w') as fp:
    for src in src_list:
        fp.write('%s.jpg">\n' % src + '<img src="')

print('YandexBot_image_recognition.py: Programa finalizado.')
exit()