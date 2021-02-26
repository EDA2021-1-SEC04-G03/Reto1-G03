"""
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
    return (video1['views'] < video2['views'])

# Funciones de ordenamiento

def sortVideos(catalog, size, tipo_ord):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if tipo_ord=='selection':
        sorted_list = ss.sort(sub_list, cmpVideosByViews)
    elif tipo_ord=='insertion':
        sorted_list = si.sort(sub_list, cmpVideosByViews)
    elif tipo_ord=='shell':
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif tipo_ord=='merge':
        sorted_list = ms.sort(sub_list, cmpVideosByViews)
    elif tipo_ord=='quick':
        sorted_list = qs.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return elapsed_time_mseg, sorted_list