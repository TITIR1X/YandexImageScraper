import glob
import os

try:os.system('cls')
except:os.system('clear')
print("""
 ./organizador_de_archivos.py
  ____              _______ _   ______ _       ___ __    __
 |  _ \            /__   __(_)/__   __(_) _ __|_| |\ \\  / /
 | |_) |_   _         | |   _    | |   _ | '__| | | \ \\/ /
 |  _ <| | | |        | | 0| |   | |  | || |    | |  \  \\
 | |_) | |_| |        | | /| |   | |  | || |    | | / /\ \\
 |____/ \__, |        |_| /|_|   |_|  |_||_|    |_|/_/  \_\\
         __/ |                                               
        |___/                           
""")

# Solicitar ruta de la carpeta de entrada
ruta = input('Arrastre la carpeta con imagenes a capturar: ')
ruta = ruta.replace("\\", '/')
ruta = ruta.replace('"', '')

# Obtener la lista de archivos en la carpeta
path_list = glob.glob(f"{ruta}/*")

# Establecer límite de archivos por carpeta
LIMITE = 50

# Solicitar número inicial para la carpeta
contador = int(input(' [*] Establece desde que número comenzar (utiliza "1"): '))

# Inicializar contadores
contador3 = 0
cadena = []

# Establecer nombre de la carpeta de salida
output_dir = "stacks_50"

# Recorrer cada archivo en la lista
for file_path in path_list:
    if contador3 == LIMITE:
        # Crear carpeta
        os.makedirs(f"{output_dir}\\{contador}")

        # Escribir archivos en la carpeta
        with open(f"{output_dir}/{contador}/ALL_LINKS.html", 'w') as file:
            for link in cadena:
                file.write(link)
        file.close()

        # Reiniciar contadores
        contador3 = 0
        cadena = []
        contador += 1

    # Leer contenido del archivo
    with open(file_path) as text_file:
        contents = text_file.read()

    # Agregar contenido al arreglo
    cadena.append(contents)
    contador3 += 1

# Si hay archivos restantes, crear una carpeta adicional y agregar los archivos restantes
if contador3 > 0:
    # Crear carpeta
    os.makedirs(f"{output_dir}\\{contador}")

    # Escribir archivos en la carpeta
    with open(f"{output_dir}/{contador}/ALL_LINKS.html", 'w') as file:

        for link in cadena:
            file.write(link)
        file.close()
