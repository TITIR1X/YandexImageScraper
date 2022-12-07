from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import URLS_, os, time


text_to_search = input('Escriba el texto con los parametros a buscar, ejemplo: Male face, Female face, etc\nBuscar: ')


# CONFIGURACIÓN DE WEBDRIVER.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(r"--user-data-dir=C:\Users\Santi\AppData\Local\Google\Chrome\User Data")
options.add_argument("window-size=1200x800")
driver = webdriver.Chrome(executable_path=r'webdriver//chromedriver.exe', chrome_options=options)


### C O N F I G U R A R ###

output_folder = 'SRC_HD'

limit = 100

direct_imgs = URLS_.direct_imgs

retomar_trabajo = None


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f'./{output_folder}, carpeta creada!')

image_src_list = []

driver.get(f"https://yandex.com/images/search?text={text_to_search}&isize=large")
time.sleep(1)

try:
    driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a/img').click()
except:
    driver.find_element("xpath", '/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div/a/img').click()
time.sleep(1)

for i in range(limit):
    try:
        element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element("xpath", '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/img'))
        src = element.get_attribute("src")
        image_src_list.append(src)
        print('[{0} de {1}] img src adquiridas!'.format(len(image_src_list), limit))
        ActionChains(driver).key_down(Keys.DOWN).perform()
    except TimeoutError:
        pass

    with open(f'{output_folder}/busqueda_{text_to_search}.html', 'w') as fp:
        for src in image_src_list:
            fp.write('<img src="{0}"/>\n'.format(src))

time.sleep(1)
print('programa finalizado!')