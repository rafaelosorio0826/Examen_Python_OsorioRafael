from importaciones import *

while True:
    print(menuPrincipal)
    print('')
    print(menu1)
    opcion = getInt('Selecciones una opcion :')

    match opcion:
        case 1:
            pressEnter()
            usuario()
        case 2:
            pressenter()
            servicios()
        case 3:
            pressEnter()
            reportes()
        case 4:
            print('Opcion invalida, seleccione una opcion')
            input('Presione cualquier tecla')
            break
        case _:
            print('Fue un placer atenderte') 