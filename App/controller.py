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
 """

from os import stat_result
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def initCatalog(tipo_lista):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tipo_lista)
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategory(catalog)


def loadVideos(catalog):
    """
    Carga los videos del archivo.
    """
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategory(catalog):
    """
    Carga las categorias de videos y los agrega a la lista de categorías
    """
    categoryfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))
    for category in input_file:
        model.addCategory(catalog, category)

#Funciones de filtración

def filterVideos(catalog, fields, criterias):
    """
    Filtra los videos basados en un criterio para cada campo
    """
    return model.filterVideos(catalog, fields,criterias)


# Funciones de ordenamiento

def sortVideos(catalog, size, criteria):
    """
    Ordena los libros por average_rating
    """
    return model.sortVideos(catalog, size, criteria)

def getTopVideoByTrendingDate(catalog):
    """
    Ordena los libros por average_rating
    """
    return model.getTopVideoByTrendingDate(catalog)

def trendingByCategory(catalog, category):
    '''
    Retorna el video mas trending en una categoria
    '''
    category_id = model.categoryToId(catalog,category)
    if(category_id == None):
        return None
    return model.trendingByCategory(catalog,category_id)

def searchByTag(catalog, videos, tag, country):
    '''
    Busca N videos con un tag especifico en un pais
    '''
    tag = '"'+tag+'"'
    vids = model.searchByTagAndCountry(catalog, tag, country)
    result = model.sortVideos(vids,videos,'likes')
    return result