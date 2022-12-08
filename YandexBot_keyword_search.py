from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import os, time

# Este código usa la librería selenium para automatizar la búsqueda de imágenes en Yandex 
# a partir de un texto de búsqueda dado por el usuario. Luego, guarda las URL de las 
# imágenes encontradas en una lista y escribe esas URL en un archivo HTML.

try:
 os.system('cls')
 os.system('color 6')
except:os.system('clear')
 
print("""
 ./separador_stacks_50
  ____              _______ _   ______ _       ___ __    __
 |  _ \            /__   __(_)/__   __(_) _ __|_| |\ \\  / /
 | |_) |_   _         | |   _    | |   _ | '__| | | \ \\/ /
 |  _ <| | | |        | | 0| |   | |  | || |    | |  \  \\
 | |_) | |_| |        | | /| |   | |  | || |    | | / /\ \\
 |____/ \__, |        |_| /|_|   |_|  |_||_|    |_|/_/  \_\\
         __/ |                                               
        |___/                           
""")

# Aquí se está configurando el navegador Chrome para que se abra con las opciones especificadas
# (como el tamaño de la ventana y el directorio de datos del usuario).
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(r"--user-data-dir=C:\Users\Santi\AppData\Local\Google\Chrome\User Data")
options.add_argument("window-size=1200x800")
driver = webdriver.Chrome(executable_path=r'webdriver//chromedriver.exe', chrome_options=options)

text_to_search = input('Escriba el texto con los parametros a buscar, ejemplo: Male face, Female face, etc\nBuscar: ')

### C O N F I G U R A R ###

output_folder = 'YandexBot_keyword_search'

limit = 1400

retomar_trabajo = None

# Aquí se comprueba si la carpeta especificada en la variable output_folder existe. Si no existe, se crea una nueva carpeta con ese nombre.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f'./{output_folder}, carpeta creada!')

image_src_list = []

# Se abre la página de búsqueda de imágenes en Yandex con el texto de búsqueda dado por el usuario.
driver.get(f"https://yandex.com/images/search?text={text_to_search}&isize=large")
time.sleep(1)
# Luego, se intenta hacer clic en la primera imagen de la búsqueda.
try:
    driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a/img').click()
except:
    # Si no se encuentra la imagen en la primera ubicación, se intenta hacer clic en la segunda ubicación.
    driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div/a/img').click()

# Se espera un segundo después de hacer clic en la imagen para que la página tenga tiempo de cargar.
time.sleep(1)

# Se itera un número de veces especificado en la variable limit.
for i in range(limit):
    
    try:
        # En cada iteración, se busca la URL de la imagen en la página usando una expresión XPath y se guarda en una lista.
        element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element("xpath", '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/img'))
        src = element.get_attribute("src")
        image_src_list.append(src)
        # Luego, se imprime un mensaje en la consola indicando el progreso.
        print('[{0} de {1}] img src adquiridas!'.format(len(image_src_list), limit))
        # Después, se simula una pulsación de la tecla "abajo" en el teclado, lo que desplaza la página hacia abajo y muestra las siguientes images en la búsqueda.
        ActionChains(driver).key_down(Keys.DOWN).perform()
    except TimeoutError:
        pass

    # Finalmente, se escriben las URL de las imágenes en un archivo HTML en la carpeta especificada en la variable output_folder.
    with open(f'{output_folder}/SRCImages_keyword_search_{text_to_search}.html', 'w') as fp:
        for src in image_src_list:
            fp.write('<img src="{0}"/>\n'.format(src))

print('programa finalizado!')
