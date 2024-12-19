from funciones.funciones import *
from message.message import *

def newusuary(baseDatos):
    print('*** Nuevo Usuario ***')
    documento = intId('*** ingrese Numero de Documento ***')
    for i in range(len(baseDatos["usuario"])):
        if baseDatos["usuario"][i]["documento"] == documento:
            print (baseDatos["usuario"][i][documento],"El nunmero de documento ya esta registrado :)")
            pressEnter()
            return baseDatos
nombre = input('Ingrese su nombre completo: ').capitalaze()
direccion = input('Ingrese la direccion del servicio a contratar: ')
telefono = input('Ingrese el numero del plan a contratar: ')
Estado = {"En estudio": True,
            "Aprovado": False,
            "Rechazado": False,
            }
                     

def loginDatosUsuario1(ingresar):
    datos = abrirArchivo(baseDatos)
    for usuario in baseDatos['usuario']:
        if ingresar == usuario['documento']:
            for usuario in usuario['documento']:
                print(f'Bienvenido: {usuario["nombre"]} ')
                print(f'Documento: {usuario["documento"]} ')
                print(f'Telefono: {usuario["telefono"]} ')
                print(f'Direccion: {usuario["direccion"]} ')
                print(f"Estado: Aprovado ")


def loginUsuario1():
    baseDatos = abrirArchivo(RUTA_BASE_DATOS)
    baseDatos = ingresarusuario(baseDatos)

def usuario():
    while True:
        print('menuUsuario')
        print('ingrese un documento')
        opcion = getint(':)')
        if opcion == 1:
            addusuario()
        elif opcion == 2:
            loginusuario()
        elif opcion == 3:
            pressEnter()
            break
        else:
            print('ingrese una opciopn valida')
            input('presione cualquier tecla para salir')




