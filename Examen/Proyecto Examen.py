print("\t\t\tExámen / Proyecto Final Python")

'''
Elaborado por MEDRANO MIRANDA, DANIEL ULISES
Materia: EDA - I
Grupo: 15
'''

import os
os.system("cls")
print("A continuación se presenta un indicador del semáforo epidemiológico de COVID\n\n") 
indicadoresCOVID=[]     #Lista para guardar los indicadores COVID
edades=[]               #Lista para guardar las edades de las personas
acumulador=0
incremento=0
contagios=0
maxindicador=0.8

archivo=open("Datos_Examen_Proyecto.csv",'r')       #Abrir base de datos
lectura=archivo.readlines()
archivo.close()

for i in lectura:
    pc=i.find(",")                                  #Permite encontrar la primer coma ','
    ps=i.find(",",pc+1)                             #Permite encontar la segunda coma ',' que es el final de la base de datos
    edades.append(int(i[0:pc]))                     #Guarda las edades en la lista edades[] como números enteros
    indicadoresCOVID.append(float((i[pc+1:ps])))    #Guarda los indicadores COVID en la lista indicadoresCOVID[] como números reales

'''print(edades)
print("\n")
print(indicadoresCOVID)
print("\n")'''

for i in edades:                                    #El ciclo permite contar cuantos datos se tienen
    incremento=incremento+i
    acumulador=int(acumulador)+1                    #Acumulador cuentaa cuántas personas se registaron

print(incremento)
print("Se tienen "+str(acumulador)+" personas registradas")

for i in indicadoresCOVID:                                    #El ciclo permite contar cuantas personas estan contagiadas
    if i < 0.8:
        del edades[contagios:contagios+1]                     #Si no está contagiada entonces no se cuenta
    else:
        contagios=contagios+1                                 #Si está contagiada se suma
    
promedad=incremento/acumulador                                #Cálculo del promedio de gente contagiada

print("La gente con COVID es de "+str(contagios)+" personas")
if incremento==0:
    print("El semaforo epidemiológico se encuentra en color VERDE ya que no hay contagios\n")
elif incremento<=incremento<=30:
    print("El semaforo epidemiológico se encuentra en color AMARILLO ya que hay 30 contagios o menos\n")
elif incremento<=incremento<=70:
    print("El semaforo epidemiológico se encuentra en color AMARILLO ya que hay entre 31 - 70 contagios\n")
else:
    print("El semaforo epidemiológico se encuentra en color ROJO ya que hay más de 71 contagios\n")

print("El promedio de edad de la gente con COVID es: "+str(promedad)+ " años")




    
