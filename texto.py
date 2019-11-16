#!/usrbin/env python
from terminaltables import AsciiTable

def texto():

    while True:
        frame = [
            ['1). Crear doc.txt','r). leer datos'],['q). Salir']
                 ]
        table = AsciiTable(frame)
        print(table.table)
        
        user_input = input(" :")

        if user_input == "1":
            archi1=open("datos.txt","w")
            archi1.write(input("pegue aqui : "+"\n"))
            archi1.close()
        elif user_input == "l":
            file = "datos.txt"
            archi1=open(file,'r')
            lec_1 = archi1.read()
            print(lec_1)
            archi1.close()
            
        elif user_input == "q":
            break
        else:
            print("\n")





