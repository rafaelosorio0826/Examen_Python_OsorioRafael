import json

def abrirArchivo(archivo):
    with open(f".archnivosj/{archivo}.json","r") as archivoAbrir:
        final = json.load(archivoAbrir)
    return final
def guardarSArchivo(archivo.diccionario):
    objetoJson= json.dumps(diccionario, indent=3)
    with open(f'./archivosJ/{archivo}.json',"w") as archivoAbrir:
        archivoAbrir.Write(objetoJson)

baseDatos = abrirQArchivo('baseDatos')

RUTA_BASE_DATOS = 'baseDatos'
