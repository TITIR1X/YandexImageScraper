import glob
import platform, os

os_name = platform.system()

if os_name == 'Windows':
    os.system('cls')
elif os_name == "Linux":
    os.system('clear')
 
print("""
 ./file_organizer.py
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
ruta = input('Arrastre la carpeta con imagenes src a capturar: ')
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

# Crear carpeta
try:
    os.mkdir(f"{output_dir}")
except FileExistsError:pass

file_count = 1

# Recorrer cada archivo en la lista
for file_path in path_list:
    if contador3 == LIMITE:
        # Escribir archivos en la carpeta
        with open(f"{output_dir}/{file_count}__{LIMITE}_files_in_one.html", 'w') as file:
            for link in cadena:
                file.write(link)
        file.close()

        contador += 1
        file_count +=1

        # Reiniciar contadores
        contador3 = 0
        cadena = []
        

    # Leer contenido del archivo
    with open(file_path) as text_file:
        contents = text_file.read()

    # Agregar contenido al arreglo
    cadena.append(contents)
    contador3 += 1

# Si hay archivos restantes, crear una carpeta adicional y agregar los archivos restantes
if contador3 > 0:
    # Crear carpeta
    os.makedirs(f"{output_dir}\\adicional")

    # Escribir archivos en la carpeta
    with open(f"{output_dir}/adicional/{file_count}__{LIMITE}_files_in_one.html", 'w') as file:

        for link in cadena:
            file.write(link)
        # Guarda el archivo
        file.close()
        
print('\nfile_organizer.py: Programa finalizado.')
exit()
