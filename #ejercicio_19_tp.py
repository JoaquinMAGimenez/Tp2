#ejercicio_19_tp.py

from secrets import choice
from pila import Pila

class Peliculas():
    titulo, anio, estudio_cinematografico = None, None, None

dic = {'titulo:''El sorprendente hombre araña', 'añio:''2014', 'estudio cinematografico:''Marvel'}

dic=['titulo']

pila1= Pila()

contador=0

titulo = ['El sorprendente hombre araña','aquaman', 'X-Men La decicion final']
anio = ['2014','2018','2006']
estudio_cinematografico = ['Marvel', 'DC', 'Marvel']


for i in range(len(titulo)):
    dato = Peliculas()
    dato.titulo = titulo[i]
    dato.anio = anio[i]
    dato.estudio_cinematografico = estudio_cinematografico [i]
    dic = {'titulo': titulo [i], 'añio': anio[i], 'estudio cinematografico': choice(estudio_cinematografico)}
    print(dato.titulo, dato.anio, dato.estudio_cinematografico)
    pila1.apilar(dato)

print()

insertar = True
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    # !A
    if(dato.anio == '2014'):
        print('la pelicula estrenada en 2014 es', dato.titulo)
    # B 
    if(dato.anio == '2018'): 
        contador = contador + 1
   
    # C
    if(dato.estudio_cinematografico == 'Marvel'):
        if(dato.anio=='2006'):

         print('las pelicula estrenada en 2006 es', dato.titulo)

print('las peliculas estrenadas en 2018 son', contador)