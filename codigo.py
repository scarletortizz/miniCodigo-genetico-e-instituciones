import numpy as np


def traducirCodigo(cadena):
    tabla = {"AAU": "N", "ACA": "T", "AGA": "R", "GAC": "D"}
    partes = cadena.split("-")
    resultado = ""
    for codigo in partes:
        if codigo in tabla:
            resultado += tabla[codigo]
        else:
            resultado += "?"  
    return resultado


def cargarInformacion(lineas):
    codigos = np.array([])
    instituciones = np.array([])

    linea_num = 1
    for linea in lineas:
        linea = linea.strip()
        if linea == "":
            linea_num += 1
            continue

        
        if linea.count(";") != 2:
            print("Linea " + str(linea_num) + " inválida: " + linea)
            linea_num += 1
            continue

        partes = linea.split(";")
        codigoGen = partes[0].strip()
        
        codigoInst = partes[2].strip()

        
        if codigoGen == "":
            print("Linea " + str(linea_num) + " inválida, código vacío")
            linea_num += 1
            continue

    
        traducido = traducirCodigo(codigoGen)
        if traducido not in codigos:
            codigos = np.append(codigos, traducido)

        if len(codigoInst) < 6:
            print("Linea " + str(linea_num) + " inválida, institución muy corta: " + codigoInst)
            linea_num += 1
            continue

        
        instProcesada = codigoInst[2:7] + codigoInst[-3:]
        if instProcesada not in instituciones:
            instituciones = np.append(instituciones, instProcesada)

        linea_num += 1

    return codigos, instituciones


def escribirArchivo(codigos, instituciones):
    print("\nCodigos geneticos unicos:")
    for c in codigos:
        print(c)

    print("\nInstituciones unicas:")
    for inst in instituciones:
        print(inst)

def main():
    lineas = []
    n = int(input("Ingrese la cantidad de registros que va a agregar: "))

    for i in range(n):
        entrada = input("Ingrese códigoGenético;Nombre;CódigoInstitución: ")
        lineas.append(entrada)

    codigos, instituciones = cargarInformacion(lineas)
    escribirArchivo(codigos, instituciones)


main()

