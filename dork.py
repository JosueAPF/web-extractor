#!/usr/bin/env ptyhon

from terminaltables import AsciiTable

def dork():
    while True:
        print("     # # #                     ")
        print("   #                           ")
        print(" |¨¨|¨¨¨¨¨¨¨¨¨¨¨\              ")
        print(" |  |            \             ")
        print(" |  |  GOOGle     \            ")
        print(" |  |        ++  | \           ")
        print(" |  |  |--|  ++  |             ")
        print(" |__|__|__|______|Dorks        ")

        frame = [['Lista de Dorks'],
                 ['1). Google Dorks V1'],
                 ['2). Google Dorks V2'],
                 ['3). Google Dorks V3'],
                 ['4). Google Dorks V4'],
                 ['q). Salir'],
                 ]
        table = AsciiTable(frame)
        print(table.table)
        user_input = input(" :")

        if user_input == "1":
            filename = 'GDV1.txt'
            f = open(filename)
            contenido = f.read()
            print(contenido)
            f.close()

        elif user_input == "2":
            file = 'GDV2.txt'
            f = open(file,'r')
            contenido = f.read()
            print(contenido)
            f.close()
        elif user_input == "3":
            f = open('GDV3.txt')
            contenido = f.read()
            print(contenido)
            f.close()
        elif user_input == "4":
            file = 'GDV4.txt'
            f = open(file,'r')
            contenido = f.read()
            print("Despliegue el menu :")
            print(contenido)
            f.close()
        elif user_input == "5,6,7,8,9,10,11,12,13,14,15" or "a,b,c,d,e,f,g,h,i,g,k,l,m,n":
            print("infeliz esa opcion no funciona :")
            break
        elif user_input == "q":
            break
        else:
            print("\n")



   

