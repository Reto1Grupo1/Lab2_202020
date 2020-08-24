"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

#ADT y DataStructures se nombran lt, no sabemos si eso genera un error imprevisto en el codigo y arreglarlo es bastante dificil
#por alguna razon al imprimir el lista["first"] salen 2000 "}}}}}" llaves

import config as cf
import sys
import csv
from Sorting import insertionsort as sort
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def less(element1, element2):
    if int(element1['id']) < int(element2['id']):
        return True
    return False

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0

def orderElementsByCriteria(listadetails,less,maxvote,minvote,bestvote,worstvote):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    average=[]
    averagemax=[]
    averagemin=[]

    count=[]
    countmax=[]
    countmin=[]

    retorno={}

    for i in range(1,len(listadetails)):
        average.append(listadetails[i]["vote_average"])
        count.append(listadetails[i]["vote_count"])

    sort.insertionSort(average,less)
    sort.insertionSort(count,less)

    for i in range(0,10):
        averagemax.append(average[i])
        countmax.append(count[i])

    for i in range(0,10):
        averagemin.append((average)[i])
        countmin.append((count)[i])

    if maxvote==1:
        retorno["Mas_votadas"]=countmax
    if minvote==1:
        retorno["Menos_votadas"]=countmin
    if bestvote==1:
        retorno["Mejores_votadas"]=averagemax
    if worstvote==1:
        retorno["Mejore_votadas"]=averagemin

    return retorno

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                listadetails = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                listacasting = loadCSVFile("Data/MoviesCastingRaw-small.csv")
                print("Datos cargados details, ",listadetails['size']," elementos cargados")
                print("Datos cargados casting, ",listacasting['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if listadetails==None or listadetails['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")    
                else: print("La lista details tiene ",listadetails['size']," elementos")
                if listacasting==None or listacasting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")    
                else: print("La lista casting tiene ",listacasting['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                maxvote=int(input("Desea ver las peliculas mas votadas? 1: Si, 0: No: "))
                minvote=int(input("Desea ver las peliculas menos votadas? 1: Si, 0: No: "))
                bestvote=int(input("Desea ver las peliculas mejor votadas? 1: Si, 0: No: "))
                worstvote=int(input("Desea ver las peliculas peor votadas? 1: Si, 0: No: "))
                print(orderElementsByCriteria(listadetails,less,maxvote,minvote,bestvote,worstvote))
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()