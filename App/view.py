"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printLine():
    print("---------------------------------------------------------------")

def printMenu():
    printLine()
    print("Menu")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los videos con más views por país y categoría")
    print("3- Consultar el video que más dias ha sido trending por país")
    print("4- Consultar el video que más dias ha sido trending por categoría")
    print("5- Consultar el video con más likes por tag")
    print("0- Salir")
    printLine()



catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        #Cargar archivos

        file_name = input("Nombre del archivo:")
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        catalog = controller.loadData(catalog)
        print(catalog)
        print("Done")


    elif int(inputs[0]) == 2:
        #Req 1

        videos = int(input("Cuantos videos: "))
        country = int(input("País: "))
        category = int(input("Categoría: "))
        print("Cargando...")
        #function bla bla

    elif int(inputs[0]) == 3:
        #Req 2

        country = int(input("País: "))
        print("Cargando...")
        #funcion aqui

    elif int(inputs[0]) == 4:
        #Req 3

        category = int(input("Categoría: "))
        print("Cargando...")
        #funcion aqui

    elif int(inputs[0]) == 5:
        #Req 4

        videos = int(input("Cuantos videos: "))
        tag = input("Tag: ")
        print("Cargando...")
        #funcion aqui

    else:
        print("Adios!")
        sys.exit(0)
sys.exit(0)
