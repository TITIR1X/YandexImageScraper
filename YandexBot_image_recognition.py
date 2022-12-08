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

# Configuramos las opciones del webdriver de Chrome
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


# Configuramos el nombre de la carpeta de salida y comprobamos si existe. Si no existe, la creamos.
carpeta_salida = 'YandexBot_image_recognition'
if not os.path.exists(carpeta_salida):
    os.mkdir(carpeta_salida)

# Establecemos un límite de scroll para cargar nuevas imágenes para cada búsqueda
scrolling_limit = 1400

# Obtenemos la lista de términos de búsqueda a partir del archivo URLS_.py
images_src_list = URLS_.images_src_list

# Establecemos el índice de la lista desde el cual queremos comenzar
comenzar_desde = 1

# Iniciamos contadores que nos servirán para recorrer la lista de términos de búsqueda y contar el número de imágenes descargadas para cada término.
count = comenzar_desde - 1
count2 = count + 1

# Creamos un bucle que itera sobre la lista de términos de búsqueda
while count < len(images_src_list):
    print(f'\n [{count2} de {len(images_src_list)}] \n .. \n Trabajando...')
    time.sleep(1)

    # Abrimos la página de búsqueda de imágenes de Yandex
    driver.get("https://yandex.com/images")

    # Hacemos clic en el botón que nos permite seleccionar la opción de búsqueda por URL
    driver.find_element("xpath",'/html/body/header/div/div[2]/div[1]/form/div[1]/span/span/button/div').click()
    time.sleep(1)

    # Maximizamos la ventana del navegador 
    driver.maximize_window()

    
    # Introducimos el término de búsqueda (LINK ITERADO DE LA LISTA DE IMÁGENES) en el campo de búsqueda y realizamos la búsqueda
    driver.find_element("xpath", '/html/body/header/div/div[3]/div[1]/form/span/input').send_keys(images_src_list[count])
    driver.find_element("xpath", '/html/body/header/div/div[3]/div[1]/form/button').click()

    # Incrementamos el contador que nos indica el número de términos de búsqueda procesados
    count +=1

    # Creamos una variable a que se utilizará para controlar el bucle que se encarga de descargar las imágenes
    a=0

    # Creamos un bucle que se ejecutará hasta que se haya obtenido el número deseado de 'src images' para el término de búsqueda actual
    while a == 0:
        try:
            # Esperamos a que se carguen los resultados de la búsqueda
            time.sleep(2)
            # Hacemos clic en el botón que nos permite ver más resultados de la búsqueda
            driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/section/a').click()
            a = 1
        except:
            try:
                 # Si no encontramos el botón que se espera, inten,, ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/section/a').click()
                a = 1
                # Continuamos con el bucle que se encarga de descargar las imágenes para el término de búsqueda actual
            except:pass

    # Iniciamos un contador que nos indicará el número de src images obtenidas para el término de búsqueda actual
    count_img = 1

    # Iniciamos un contador que se utilizará para controlar el bucle que se encarga de descargar las src de imágenes
    contador = 0
    
    # Mientras el número del contador sea menor o igual al límite especificado del scroll, realizamos un scroll hacia abajo en la página para cargar más resultados de la búsqueda
    while contador <= scrolling_limit:
        print(f'Scrolleando página.. {contador} de {scrolling_limit}')

        # Realizamos un scroll hacia abajo en la página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            # Intentamos encontrar un elemento que contenga una imagen en la página
            driver.find_element("xpath", f'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[{contador}]/div/a/img').text()
            # Si el elemento se encuentra, incrementamos el contador de imágenes encontradas para luego obtener su src
            count_img +=1
        except:
            # Si no encontramos el elemento, no hacemos nada
            pass

        # Incrementamos el contador que se utiliza para controlar el bucle
        contador +=1

    # Reiniciamos el contador que se utiliza para controlar el bucle
    contador = 1

    # Creamos una lista vacía que se utilizará para almacenar las URLs de las imágenes descargadas
    src_list = []

    # Creamos un bucle que se ejecutará mientras no hayamos recorrido todos los elementos que contienen imágenes en la página
    while contador != scrolling_limit:

        # Utilizamos un try-except para controlar posibles errores al buscar elementos en la página
        try:
            driver.maximize_window()
            src = driver.find_element("xpath", f'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[{contador}]/div/a/img').get_attribute("src")
            contador += 1
            src_list.append(src)
            print(f'{len(src_list)} links IMG\'s adquiridas!')
        except:contador += 1
    
    # Crea un archivo donde se iterará cada src obtenido
    with open(f'{carpeta_salida}/src{count2}.html', 'w') as fp:
        for src in src_list:
            fp.write('%s.jpg">\n' % src + '<img src="')

    print(f'\n[{count2} de {len(images_src_list)}] ok\n')
    count2+=1

# Finalizando, crea un archivo de texto, donde almacenará todas las src de todas las imágenes similares encontradas.
with open(f'{carpeta_salida}/all_images_src.html', 'w') as fp:
    for src in src_list:
        fp.write('%s.jpg">\n' % src + '<img src="')

print('YandexBot_image_recognition.py: Programa finalizado.')
exit()

# Para descargar las imágenes, debe abrir el archivo .html deseado y hacer clic derecho en guardar página, esto hará que se descargen las imágenes a su ordenador.
