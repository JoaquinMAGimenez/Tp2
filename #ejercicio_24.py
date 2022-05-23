#ejercicio_24.py

from secrets import choice
from pila import Pila

class personajesdePeliculas():
    nombre, participacion_en_peliculas, posicion_en_la_pila  = None, None, None

dic = {'nombre:' 'Groot' , 'participacion en peliculas:' ' 4  ' , 'posicion en la pila:' '4'}

dic=['nombre']

pila1= Pila()

nombre = ['viuda negra','Rocket Raccoon', 'Tony Stark', 'Groot', 'Capitan America', 'Doc.Streng']
participacion_en_peliculas = [10, 4, 8, 4, 10, 5 ]
posicion_en_la_pila= [ 1, 2, 3, 4, 5, 6, 7, 8, 9]


for i in range(len(nombre)):
    dato = personajesdePeliculas()
    dato.nombre = nombre[i]
    dato.participacion_en_peliculas = participacion_en_peliculas[i]
    dato.posicion_en_la_pila = posicion_en_la_pila[i]
    dic = {'nombre': nombre [i], 'participacion en peliculas': participacion_en_peliculas[i], 'posicion en la pila': posicion_en_la_pila [i]}
    print(dato.nombre, dato.participacion_en_peliculas, dato.posicion_en_la_pila)
    pila1.apilar(dato)
print()

insertar = True
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
     #A
    if(dato.nombre=='Groot'):
        print('la posicion en la que aparece Groot en la pila es:', dato.posicion_en_la_pila)
    if(dato.nombre=='Rocket Raccoon'):
        print('la posicion en la que aparece Rocket Raccoon en la pila es:', dato.posicion_en_la_pila)
       
     #B
    if(dato.participacion_en_peliculas>=5):
        print('los personajes que aparecieron en mas de 5 peliculas son:',dato.nombre)

     #C
    if(dato.nombre == 'viuda negra'):
        print('la cantidad de peliculas en las que participo la viuda negra fue:', dato.participacion_en_peliculas) 
     #D
    if((dato.nombre[0] == 'C') or (dato.nombre[0] == 'D') or (dato.nombre[0]=='G')):
        print ('los personajes con nombres con C d y g son:', dato.nombre)
    
