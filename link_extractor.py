import os, re

os.system('cls')
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


imagesPath = input('Arrastra la carpeta contenedora de links: ')

carpeta_salida = 'links_directos'
if not os.path.exists(carpeta_salida):
    os.mkdir(carpeta_salida)

contador = 0

imagesPathList = os.listdir(imagesPath)

cadena = []

# Utilizar expresión regular para buscar enlaces de imágenes
pattern = re.compile(r'<img src="([^"]+)"')

while contador < len(imagesPathList):
    with open(f'{imagesPath}/{imagesPathList[contador]}') as text_file:
        contents = text_file.read()

        # Encontrar todos los enlaces de imágenes en el archivo
        matches = pattern.findall(contents)

        file = f'{imagesPathList[contador]}'
        file = file.replace('.html', '.txt')
        file = open(f"{carpeta_salida}/{file}", "w")

    # Escribir cada enlace en una línea separada del archivo de texto
    for match in matches:
        file.write(f'{match}')
        file.write(os.linesep)

    file.close()
    print(f'[{contador + 1} de {len(imagesPathList)}].. ok')

    cadena.append(contents)
    contador += 1

    print('\n¡Espere!\nJuntando todo en un solo archivo...')
    with open(f'{imagesPath}/ALL_LINKS.txt', 'w') as file:
        for link in cadena:
            file.write('%s\n' % link + '')
            file.close()

print(' ..terminado!\nPrograma finalizado con éxito!')