# -*- coding: utf-8 -*-
"""
Created on Wed May 17 23:55:19 2023

@author: ljzap
"""
import csv

archivo = open('Facultades.csv')
reader = csv.reader(archivo, delimiter = ',')
cod=0
facu= True


for i in reader:
    if (facu):
        #entran facultades
        #unaFacultad = Facultad(int(i[0]), i[1], i[2], i[3], i[4])
        #print(f'{unaFacultad.getNombre()}')
        print(f'{i[1]}')
        #self.agregarFacultad(unaFacultad)
        #print(f'\nNombre Facultad: {self.__facultades[self.__cantidad-1].getNombre()}')
        #print('entra facultad')
        cod = int(i[0])
        facu= False
    elif cod == (int(i[0])):
        #entran las carreras
        #unaCarrera=Carrera(int(i[1]), i[2], i[3], i[4], i[5])
        #self.__facultades[self.__cantidad-1].agregarCarrera(int(i[1]), i[2], i[3], i[4], i[5])
        #print(f'{self.__facultades[self.__cantidad-1].getCarrera(0)}')
        print(f'{i[1]}')
        #print('entra carrera')
        #print(f'Nombre Carrera: {self.__facultades[self.__cantidad-1].getNombreCarrera(int(i[1])-1)}')
    else: 
        #nueva facultad
        print(f'{i[1]}')
        #facu=True
        