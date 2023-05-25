class Carrera:
    __codigo=0
    __nombre=''
    __fechainicio=''
    __duracion=0
    __titulo=''
    
    def __init__(self, cod, nom, ini, dur, tit):
        self.__codigo = cod
        self.__nombre = nom
        self.__fechainicio = ini
        self.__duracion = dur
        self.__titulo = tit
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getFecha(self):
        return self.__fechainicio
    
    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo
    