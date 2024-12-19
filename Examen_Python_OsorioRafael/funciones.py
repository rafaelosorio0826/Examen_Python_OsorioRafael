from message import *
from module.DatosJSON import *


def getInt(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except Exception:
            print('Opcion invalida, seleccione una opcion.')

def getStr(mensaje):
    entrada = str(input(mensaje))
    if entrada = isalpha():
        return entrada
    else:
        print("ingrese una opcion valida.")
        return getStr(mensaje)
    
def intId(mensaje):
    while True:
        documento = getInt(mensaje)
        cad =str(documento)
        if len(cad) >= 10:
            return cad
    else:
        print("El documento ingresado ")

    
