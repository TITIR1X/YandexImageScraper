import os

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

ruta = input('Arrastre la carpeta con imagenes a capturar: ')
ruta = ruta.replace("\\", '/')
ruta = ruta.replace('"', '')

contador = int(input(' [*] Establece desde que número comenzar: '))
contador2 = 0
contador3 = 0 # siempre empieza con 0
contador4 = 0
path_list = os.listdir(ruta)


cadena = []

while contador3 <= (len(path_list) // 50):

    os.mkdir(f'stacks_50\\{contador}')
    
    while contador2 <= 20:
        try:
            with open(f'{ruta}/{path_list[contador4]}') as text_file:
                contents = text_file.read()

            cadena.append(contents)

            with open(f'stacks_50/{contador}/ALL_LINKS.html', 'w') as file:
                for link in cadena:
                    file.write(link)
            file.close()

            print(f'{contador2} ..ok')

            contador2 += 1
            contador4 += 1
        except IndexError:
            break
    
    cadena = []
    contador2 = 0
    contador3 +=1
    print(f'\n[{contador3 + 1} de {(len(path_list) // 50)}] ..ok\n')
    contador += 1
    
