﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from datetime import datetime
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(tipo_lista):
    """
    Inicializa el catálogo de videos.
    """
    catalog = {'videos': None,
               'category_id': None}

    catalog['videos'] = lt.newList(tipo_lista,
                            cmpfunction=cmpVideosByViews)
    catalog['category_id'] = lt.newList(tipo_lista)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona un video a la lista de videos
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    """
    Adiciona una categoria a la lista de categorias
    """
    category_fixed=category['id\tname'].replace('\t','').split(" ",1)
    c = newCategory(category_fixed[1], category_fixed[0])
    lt.addLast(catalog['category_id'], c)

# Funciones para creacion de datos

def newCategory(name, id):
    """
    Esta estructura almancena las categorias utilizados para marcar videos.
    """
    category = {'name': '', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    """ Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    return (int(video1['views']) > int(video2['views']))

def cmpVideosByTitle(video1, video2):
    """ Devuelve verdadero (True) si los 'title' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'title'
        video2: informacion del segundo video que incluye su valor 'title'
    """
    return (video1['title']) < (video2['title'])

def cmpVideosByLikes(video1, video2):
    """ Devuelve verdadero (True) si los 'likes' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'likes'
        video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1['likes']) > int(video2['likes']))

#Funciones de filtración

def findCatIDbyName (catalog,fields, criterias):
    for i in range(len(fields)):
        if fields[i]=='category_id':
            for category in lt.iterator(catalog['category_id']):
                if category['name']==criterias[i]:
                    criterias[i]=category['id']
                    break
    
    return

def filterVideos(catalog, fields, criterias):
    """ Filtra los videos basados en sus campos y en los valores aceptados por los mismos.
    Si fields es (field1, field2) y criterias es (criteria1, criteria2) entonces la función retornará
    una lista en la que sólo field1 tenga el valor criteria1, y así sucesivamente.
    Args:
        fields(list): campos usados para la filtración
        criterias(list): valores posibles para los campos
    """

    newCatalog = {'videos': None}

    newCatalog['videos'] = lt.newList('ARRAY_LIST',
                            cmpfunction=cmpVideosByViews)

    findCatIDbyName(catalog, fields, criterias)

    for video in lt.iterator(catalog['videos']):
        add=True
        for i in range(len(fields)):
            if video[fields[i]] != criterias[i]:
                add=False
                break
        if add:
            lt.addLast(newCatalog['videos'], video)

    return newCatalog

# Funciones de ordenamiento

def getTopVideoByTrendingDate(catalog):
    tempElement=lt.firstElement(catalog)
    topElemento=None
    contTopElement=0
    contador=0
    
    for elemento in lt.iterator(catalog):
        if elemento['video_id']==tempElement['video_id']:
            contador+=1
        else:
            if contador>contTopElement:
                topElemento=tempElement
                contTopElement=contador
            contador=1
            tempElement=elemento
    
    if contador>contTopElement:
        topElemento=tempElement
        contTopElement=contador

    return (topElemento,contTopElement)

def sortVideos(catalog, size, criteria):

    if criteria=='views':
        sorted_list = ms.sort(catalog['videos'], cmpVideosByViews)
    elif criteria=='title':
        sorted_list = ms.sort(catalog['videos'], cmpVideosByTitle)
    elif criteria == 'likes':
        sorted_list = ms.sort(catalog['videos'], cmpVideosByLikes)

    if criteria=='views' or criteria=='likes':
        sorted_list = lt.subList(sorted_list, 1, size)

    return sorted_list

def categoryToId(catalog,category):
    '''
    Convierte del nombre de la categoria al category_id
    '''
    id = None
    category = category.title()
    for i in lt.iterator(catalog['category_id']):
        if(i['name'] == category):
            id = i['id']
            break
    return id

def trendingByCategory(catalog, category):
    '''
    Busca el video que mas ha sido trending en una categoria
    '''
    filteredList = filterVideos(catalog, ['category_id'],[category])
    orderedList = sortVideos(filteredList, None, 'title')
    if(orderedList['size'] == 0):
        #para manejar una lista vacia
        print("Empty list")
        return None
    topVid = getTopVideoByTrendingDate(orderedList)
    return topVid

def searchByTagAndCountry (catalog, tag, country):
    '''
    Igual que filteredList pero para tags
    '''
    newCatalog = {'videos': None}

    newCatalog['videos'] = lt.newList('ARRAY_LIST',
                            cmpfunction=cmpVideosByViews)

    for video in lt.iterator(catalog['videos']):
        if ((tag in video['tags']) and (video['country'] == country)):
            lt.addLast(newCatalog['videos'], video)
    
    return newCatalog
            