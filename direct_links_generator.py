import os, re

os.system('cls')
print('Aisla -> \'<img src="LOREMIPSUM">\' a \'LOREMIPSUM\'')

print("""
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
#imagesPath = imagesPath.replace("\\", '/')

carpeta_salida = 'links_directos'
if not os.path.exists(carpeta_salida):
    os.mkdir(carpeta_salida)

contador = 0

imagesPathList = os.listdir(imagesPath)

cadena = []

while contador < len(imagesPathList):
    with open(f'{imagesPath}/{imagesPathList[contador]}') as text_file:
        contents = text_file.read()
        contents = contents.replace('<img src="', '')
        contents = contents.replace('"/>', '')

    file = f'{imagesPathList[contador]}'
    file = file.replace('.html', '.txt')
    file = open(f"{carpeta_salida}/{file}", "w")
    file.write(f'{contents}')
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