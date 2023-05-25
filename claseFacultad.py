from claseCarrera import Carrera

class Facultad :
    __codigo=0
    __nombre=''
    __direccion= ''
    __localidad= ''
    __telefono= ''
    __carreras = []
    
    def __init__(self, cod, nom, dire, loc, tel):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dire
        self.__localidad = loc
        self.__telefono = tel
        self.__carreras = []
    
    def agregarCarrera(self, cod, nom, ini, dur, tit):
        self.__carreras.append(Carrera(cod, nom, ini, dur, tit))
    
    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo
    
    def getCarrera(self):
        return self.__carreras
    
    def getLocalidad(self):
        return self.__localidad