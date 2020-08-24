"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import pytest
import config as cf
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

lst_moviesdetails = lt.newList(list_type)
lst_moviescasting = lt.newList(list_type)

moviesdetailsfile = cf.data_dir + 'Data/SmallMoviesDetailsCleaned.csv'
moviescastingfile = cf.data_dir + 'MoviesCastingRaw-small.csv'

def setUp():
    print('Loading movies')
    loadCSVFile(moviesdetailsfile, lst_moviesdetails)
    loadCSVFile(moviescastingfile, lst_moviescasting)
    print(lst_moviesdetails["size"])
    print(lst_moviescasting["size"])


def tearDown():
       pass


def loadCSVFile(file, lst):
    input_file = csv.DictReader(open(file, encoding = "utf-8"))
    for row in input_file:
        lt.addLast(lst, row)

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['id'])

def less(element1, element2):
    if int(element1['id']) < int(element2['id']):
        return True
    return False

def greater(element1, element2):
    if int(element1['id']) > int(element2['id']):
        return True
    return False

def test_sort_details():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_moviesdetails, less)

def test_sort_casting():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_moviescasting, less)

def test_loading_CSV_y_ordenamiento_details():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_moviesdetails,less)
    while not (lt.isEmpty(lst_moviesdetails)):
        x = int(lt.removeLast(lst_moviesdetails)['id'])
        if not (lt.isEmpty(lst_moviesdetails)):
            y = int(lt.lastElement(lst_moviesdetails)['id'])
        else:
            break
        assert x > y

def test_loading_CSV_y_ordenamiento_casting():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_moviescasting),less)
    while not (lt.isEmpty(lst_moviescasting)):
        x = int(lt.removeLast(lst_moviescasting)))['id'])
        if not (lt.isEmpty(lst_moviescasting))):
            y = int(lt.lastElement(lst_moviescasting))['id'])
        else:
            break
        assert x > y