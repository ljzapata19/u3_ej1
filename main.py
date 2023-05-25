from ManejadorFacultad import ManejadorFacultad

if __name__ == '__main__':
    
    facultades = ManejadorFacultad()
    facultades.testFacultad()
    
    print('Menu: ')
    print('1. Ingresar el código de una facultad y mostrar nombre de la facultad, nombre y duración de cada una de las carreras que se dictan en esa facultad')
    print('2. Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.')
    print('0. Finalizar')
    op=int(input('\nIngrese opcion: '))
    while op != 0 :
        if op == 1:
            facultades.buscarFacultad()
        elif op == 2:
            facultades.buscarCarrera()
        else:
            print('Opcion Incorrecta')
        print('\n\nMenu: ')
        print('1. Ingresar el código de una facultad y mostrar nombre de la facultad, nombre y duración de cada una de las carreras que se dictan en esa facultad')
        print('2. Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.')
        print('0. Finalizar')
        op=int(input('\nIngrese opcion: '))