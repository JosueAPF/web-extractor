#!/usr/bin/env python
from datetime import datetime , timedelta

def reloj():

    hora = datetime.now()
    print("\nHora segun la maquina","\n",hora.hour,":",hora.minute)

