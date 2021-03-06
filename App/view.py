﻿"""
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

def printMenuTAD():
    print("Seleccione el tipo de lista que quiere crear:")
    print("1- Array list")
    print("2- Linked list")

def obtenerTipoLista():
    iterate=True
    while iterate:
        printMenuTAD()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            tipo_lista='ARRAY_LIST'
            iterate=False
        elif int(inputs[0]) == 2:
            tipo_lista='LINKED_LIST'
            iterate=False
    return tipo_lista

def printMenuSort():
    print("Seleccione el tipo de ordanamiento que quiere usar:")
    print("1- Selection")
    print("2- Insertion")
    print("3- Shell")
    print("4- Merge")
    print("5- Quick")


def obtenerTipoOrdenamiento():
    iterate=True
    while iterate:
        printMenuSort()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            tipo_ord='selection'
            iterate=False
        elif int(inputs[0]) == 2:
            tipo_ord='insertion'
            iterate=False
        elif int(inputs[0]) == 3:
            tipo_ord='shell'
            iterate=False
        elif int(inputs[0]) == 4:
            tipo_ord='merge'
            iterate=False
        elif int(inputs[0]) == 5:
            tipo_ord='quick'
            iterate=False
    return tipo_ord

def initCatalog(tipo_lista):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tipo_lista)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        #Cargar archivos
        tipo_lista='ARRAY_LIST'
        print("Cargando información de los archivos...")
        catalog = initCatalog(tipo_lista)
        loadData(catalog)

        print('Videos cargados: ' + str(lt.size(catalog['videos'])))

        firstVid = lt.firstElement(catalog['videos'])
        print('\nPrimer video: ',
        "\nTitulo:",firstVid['title'], "\nCanal:",firstVid['channel_title'], "\nFecha trending:",firstVid['trending_date'],
        "\nPais:",firstVid['country'], "\nViews:",firstVid['views'], "\nLikes:",firstVid['likes'], "\nDislikes:",firstVid['dislikes'])

        print('\nCategorias cargadas: ')
        for i in lt.iterator(catalog['category_id']):
            print("Nombre:",i['name'],"--- Id:",i['id'])

    elif int(inputs[0]) == 2:
        #Req 1
        size=0
        category_name = input("Indique la categoría de los videos a consultar: ")
        country = input("Indique el país de los videos a consultar: ")
        
        filteredList = controller.filterVideos(catalog, ['category_id','country'],[category_name,country])

        while size<1 or size>lt.size(filteredList['videos']):
            size = int(input("Indique el número de videos a listar: "))

        print("Ordenando datos...\n")
        result = controller.sortVideos(filteredList, size, 'views')

        print('Videos top {} para {} bajo la categoría {}:\n'.format(size,country,category_name))

        print("trending_date | title | channel_title | publish_time | views | likes | dislikes")
        for i in lt.iterator(result):
            print(i['trending_date'],'|',i['title'],'|',i['channel_title'],'|',
            i['publish_time'],'|',i['views'],'|',i['likes'],'|',i['dislikes'])

    elif int(inputs[0]) == 3:
        #Req 2
        size=1
        country = input("Indique el país de los videos a consultar: ")
        
        filteredList = controller.filterVideos(catalog, ['country'],[country])

        print("Ordenando datos...\n")
        organizedList = controller.sortVideos(filteredList, None, 'title')

        result = controller.getTopVideoByTrendingDate(organizedList)

        print('El video top trending para {} es:\n'.format(country))
        
        print("title | channel_title | country | Días")
        print(result[0]['title'],'|',result[0]['channel_title'],'|',result[0]['country'],'|',result[1])

    elif int(inputs[0]) == 4:
        #Req 3

        category = input("Categoría: ")
        print("Cargando...")
        result = controller.trendingByCategory(catalog,category)
        if(result == None):
            print("error")
        else:
            print("title | channel_title | Category ID | Días")
            print(result[0]['title'],'|',result[0]['channel_title'],'|',result[0]['category_id'],'|',result[1])

    elif int(inputs[0]) == 5:
        #Req 4
        #Buscar por un tag especifico
        country = input("Pais: ")
        videos = int(input("Cuantos videos: "))
        tag = input("Tag: ")
        print("Cargando...")
        result = controller.searchByTag(catalog,videos,tag,country)
        print("done")
        print('Los {} video(s) con mas likes para {} tag en {} es:\n'.format(videos, tag, country))
        for i in result['elements']:
            print("title | channel_title | Dia de publicacion | views | likes | dislikes | tags")
            print(i['title'],'|',i['channel_title'],'|',i['publish_time'],'|',i['views'],'|', 
                  i['likes'],'|',i['dislikes'],'|',i['tags'].split('|'))

        #print(result['elements'])
    else:
        print("Adios!")
        sys.exit(0)
sys.exit(0)
