#!/usr/bin/env python
from terminaltables import AsciiTable
#from colorama import init , Fore  
from constructor import *
import texto
import reloj
import dork


def menu():
    #init()
    print("")
    print( "$$\      $$\         $$\             $$$$$$$$\           $$\                                $$\                       ")
    print( "$$ | $\  $$ |        $$ |            $$  _____|          $$ |                               $$ |                      ")
    print( "$$ |$$$\ $$ |$$$$$$\ $$$$$$$\        $$ |     $$\   $$\$$$$$$\   $$$$$$\ $$$$$$\  $$$$$$$\$$$$$$\   $$$$$$\  $$$$$$\  ")
    print( "$$ $$ $$\$$ $$  __$$\$$  __$$\       $$$$$\   \$$\ $$  \_$$  _| $$  __$$\\____$$\$$  _____\_$$  _| $$  __$$\$$  __$$\ ")
    print( "$$$$  _$$$$ $$$$$$$$ $$ |  $$ |      $$  __|   \$$$$  /  $$ |   $$ |  \__$$$$$$$ $$ /       $$ |   $$ /  $$ $$ |  \__|")
    print( "$$$  / \$$$ $$   ____$$ |  $$ |      $$ |      $$  $$<   $$ |$$\$$ |    $$  __$$ $$ |       $$ |$$\$$ |  $$ $$ |      ")
    print( "$$  /   \$$ \$$$$$$$\$$$$$$$  |      $$$$$$$$\$$  /\$$\  \$$$$  $$ |    \$$$$$$$ \$$$$$$$\  \$$$$  \$$$$$$  $$ |      ")
    print( "\__/     \__|\_______\_______/       \________\__/  \__|  \____/\__|     \_______|\_______|  \____/ \______/\__|      ")
    print( " 1.0                                                                                                                  ")
    print( "                                                                                                                      ")
    print( "                                                                                                                      ")
    while True:
        frame =[['MENU','descripcion'],
                ['1). Extraer una pagina','*web scraping'],
                ['2). Extraer una Etiquieta','*solo una etiqueta a la vez'],
                ['3). importarla a txt','*guarda la pagina extraida en txt'],
                ['4). salir','*adopta un niño ugandes'],['5). default links','*muestra una lista de links'],['q). mostrar menu','*vuelve a desplegar el menu'],
                ['h). Hora del sistema','*muestra la hora del sistema'],['d). Google Dorks','*Muestra una lista con links a paginas dorks'],]
        table = AsciiTable(frame)
        print(table.table)
        break


while True:

    try:
        menu()
        user_input = input("ingrese una opcion :")
        info = estractor()
        if user_input == "1":
            info.estract_n()
            print("\n")
        elif user_input == "2":
            print("Etiquieta por defecto <a href=>")
            info.etiquet_a()
            print("\n")
        elif user_input == "5":#default links
            info.default()
            print("\n")
        elif user_input == "3":
            texto.texto()
        elif user_input == "h":#hora actual
            reloj.reloj()
        elif user_input == "d":
            dork.dork()
        elif user_input == "4":
            break
        else:
            print("\n")
    except KeyboardInterrupt:
        print("Preisone '4' para salir")
    except EOFError:
        print("Preisone '4' para salir")
    finally:
        pass
        
# error KeyboardInterrupt
#
