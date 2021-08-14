print("\t\t\tProyecto Final EDA - I")

'''
Elaborado por MEDRANO MIRANDA, DANIEL ULISES
Materia: EDA - I
Grupo: 15
'''

import os
os.system("cls")
print("A continuación se presenta un indicador del semáforo epidemiológico de COVID\n\n")

archivo=open("Datos_Proyecto_Final.csv",'r')       #Abrir base de datos
lectura=archivo.readlines()
archivo.close()

indicadoresCOVID=[]     #Lista para guardar los indicadores COVID
indicadoresCOVID2=[]
edades=[]               #Lista para guardar las edades de las personas
edades2=[]

for i in lectura:
    pc=i.find(",")                                  #Permite encontrar la primer coma ','
    ps=i.find(",",pc+1)                             #Permite encontar la segunda coma ',' que es el final de la base de datos
    edades.append(int(i[0:pc]))                     #Guarda las edades en la lista edades[] como números enteros
    indicadoresCOVID.append(float((i[pc+1:ps])))    #Guarda los indicadores COVID en la lista indicadoresCOVID[] como números reales

def entrevistados():
    acumulador=0
    incremento=0
    for i in edades:                                    #El ciclo permite contar cuantos datos se tienen
        acumulador=int(acumulador)+1                    #Acumulador cuentaa cuántas personas se registaron
        incremento=incremento+i
    print("Se tienen "+str(acumulador)+" personas registradas")   #Da el número de personas registradas

def contagiados():
    contagios=0
    for i in indicadoresCOVID:                                    #El ciclo permite contar cuantas personas estan contagiadas
        if i < 0.8:
            del edades[contagios:contagios+1]                     #Si no está contagiada entonces no se cuenta
        else:
            contagios=contagios+1                                 #Si está contagiada se suma
    print("La gente con COVID es de "+str(contagios)+" personas") #Da el número de personas contagiadas
    
def promedio():
    acumulador2=0
    incremento2=0
    contagios2=0
    for i in indicadoresCOVID2:                                    #El ciclo permite contar cuantas personas estan contagiadas
        if i < 0.8:
            del edades[contagios2:contagios2+1]                     #Si no está contagiada entonces no se cuenta
        else:
            contagios2=contagios2+1                                 #Si está contagiada se suma

    for i in edades:                                      #El ciclo permite contar cuantos datos se tienen
        acumulador2=int(acumulador2)+1                    #Acumulador cuentaa cuántas personas se registaron
        incremento2=incremento2+i
    promedad=incremento2/acumulador2                                #Cálculo del promedio de gente contagiada
    print("El promedio de edad de la gente con COVID es: "+str(promedad)+ " años")      #Promedio de edad

def semaforo():
    contagios=0
    for i in indicadoresCOVID:                                    #El ciclo permite contar cuantas personas estan contagiadas
        if i < 0.8:
            del edades[contagios:contagios+1]                     #Si no está contagiada entonces no se cuenta
        else:
            contagios=contagios+1                                 #Si está contagiada se suma
            
    if int(contagios==0):                                              #Semáforo epidemiológico
        print("El semaforo epidemiológico se encuentra en color VERDE ya que no hay contagios")
    elif contagios>0 and contagios<=30:
        print("El semaforo epidemiológico se encuentra en color AMARILLO ya que hay 30 contagios o menos")
    elif contagios>30 and contagios<=70:
        print("El semaforo epidemiológico se encuentra en color NARANJA ya que hay entre 31 - 70 contagios")
    else:
        print("El semaforo epidemiológico se encuentra en color ROJO ya que hay más de 71 contagios")

cola=[]                 #Inicializa una lista que funcionará como cola
dato=0
print("Los datos posibles que puedes pedir son:")
print("1) ¿Cuántas personas fueron entrevistadas?")
print("2) ¿Cuántas personas están contagiadas?")
print("3) ¿Cuál es el color del semáforo epidemiológico?")
print("4) ¿Cuál es el promedio de edad de la gente? \n")
eleccion=int(input("¿Cuantos datos necesitas saber? "))         #Pide al usuario la cantidad de datos a solicitar
print("Escribe el número del dato que deseas conocer seguido de presionar 'Enter'")
for i in range(eleccion):                       #El ciclo pide el numero del dato de acuerdo a cuantos datos necesita el usuario
        dato=int(input("Dato #: "))
        cola.append(dato)
for i in range(eleccion):               #El ciclo revisa el numero de dato que se pidio para imprimirlo en la pantalla 
    if cola[0] == 1:
        entrevistados()
    elif cola[0] == 2:
        contagiados()
    elif cola[0] == 3:
        semaforo()
    elif cola[0] == 4:
        promedio()
    else:
        print("Slección no válida")
    cola.pop(0)                         #Elimina el primer elemeno de la lista (cola) para pasar al siguiente



    
