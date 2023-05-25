from claseFacultad import Facultad

import csv

class ManejadorFacultad:
    __lista = []
    
    def __init__(self):
        self.__lista = []
    
    def agregarFacultad(self, unaFacultad):
        self.__lista.append(unaFacultad)
    
    def testFacultad(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter = ',')
        cod=0
        facu= True
        for i in reader:
            if (facu):
                #entra facultades
                unaFacultad = Facultad(int(i[0]), i[1], i[2], i[3], i[4])
                self.agregarFacultad(unaFacultad)
                cod = int(i[0])
                facu= False
            elif cod == (int(i[0])):
                #entran las carreras
                unaFacultad.agregarCarrera(int(i[1]), i[2], i[3], i[4], i[5])
            else: 
                #nueva facultad
                unaFacultad = Facultad(int(i[0]), i[1], i[2], i[3], i[4])
                self.agregarFacultad(unaFacultad)
                cod = int(i[0])
                
    
    def buscarFacultad(self):
        codigo = int(input('Ingrese codigo de la facultad: '))
        i=0
        while (i < len(self.__lista)) and (codigo != self.__lista[i].getCodigo()) :
            i += 1
            
        if i < len(self.__lista):
            print(f'\nNombre facultad: {self.__lista[i].getNombre()}')
            for carrera in self.__lista[i].getCarrera():
                print(f'\nNombre carrera: {carrera.getNombre()}')
                print(f'Duracion carrera: {carrera.getDuracion()}')
        else:
            print('El código ingresado es incorrecto.')

    def buscarCarrera(self):
        carrera_buscada= input('Ingresar nombre de la carrera: ')
        band = False
        i=0
        #print(f'lista {len(self.__lista)}')
        while(i < len(self.__lista)) and (band == False) :
            #print('entra')
            carreras = self.__lista[i].getCarrera()
            j=0
            while (j < len(carreras)) and (carrera_buscada != carreras[j].getNombre()):
                #print(j)
                #print(carrera_buscada)
                #print(carreras[j].getNombre())
                j += 1
           
            
            if j < len(carreras):
                #print(f'buscada {carrera_buscada}')
                #print(f'supuesta {carreras[j].getNombre()}')
                #print('se encontro')
                encontrada = carreras[j]
                band = True
            
            i += 1
        
        if band == True:
            print(f'\nCodigo carrera: {i} {encontrada.getCodigo()}')
            print(f'Nombre facultad: {self.__lista[i-1].getNombre()}')
            print(f'Localidad facultad: {self.__lista[i-1].getLocalidad()}')
        else:
            print ('La carrera ingresada no se encuentra registrada.')
            
        
        
        