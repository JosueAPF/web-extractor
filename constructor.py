#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib.request

class estractor():
    
    def estract_n(self):
        try:
            linka = input("Aqui el Link:")
            dataa = urllib.request.urlopen(linka).read().decode()
            print(dataa)
            print("\n")
        except ValueError:
            print("Error ingrese un link valido")
        except urllib.error.URLError:#error con urlopen no se puedo abrir la pagina
            print("\n\t\tno se pudo extraer")
        except KeyboardInterrupt:
            print("se ha interumpido el script ")
        finally :
            pass
        
    def etiquet_a(self):
        try:
            linkb = input("Aqui el Link: ")
            datab = urllib.request.urlopen(linkb).read().decode()
            sopa = BeautifulSoup(datab)
            tags = sopa('a')
            for tag in tags:
                print(tag.get('href'))
            print(data)
        except ValueError:
            print("ingrese un link valido")
        finally:
            pass
    def default(self):
        file = 'lista_links.txt'
        f = open(file)
        contenido = f.read()
        print("\nListado de link :",contenido)
        

