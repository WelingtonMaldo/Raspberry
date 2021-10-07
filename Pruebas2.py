# IMPORTAR ARCHIVOS NECESARIOS PARA EJECUTAR EL CÓDIGO

from os import readlink
from os import system
from time import sleep

#VACIAR LA TERMINAL

#system('cls')                  Este comando sirve en Windows
system('clear')                 #Este comando sirve en Linux y Mac

#MENSAJES INICIALES

Titulo = "Water tunnel measurement and visualisation system design"
print("                                            ",Titulo.upper(),"\n\n")
print("*************************************************************************************************************************************************************\n")
print("Bienvenidos al proyecto del sistema de medicion del tunel de agua\n")
print('A partir de este sistema se va a poder obtener los valores de la componente de la velocidad'
 'de la corriente uniforme que pasa a traves de la seccion de test\n')

print("Vx, Vy, Vz\n")
print("Además, se va a exportar el valor de la temperatura y del número de Reynolds\n")

print("T, Re\n")
print("*************************************************************************************************************************************************************\n")

Vx = 6.05                       #Se almacena en memoria la componente de la velocidad Vx en [m/s]
Vy = 10.05                      #Se almacena en memoria la componente de la velocidad Vx en [m/s]
Vz = 20.006                     #Se almacena en memoria la componente de la velocidad Vx en [m/s]
Temperatura = 20.05             #Se almacena en memoria el valor de la temperatura del agua en [ºC, Grados Celsius]
Reinolds = 1500.793                 
'''Se almacena en memoria el valor del Reynolds, el valor de dicho numero debe ser menor
                                a 2300, esto se debe a que el flujo que existe en la region de test es un flujo laminar
'''
print('A continuación se va a mostrar en pantalla los valores de las variables que definen las propiedades del flujo del'
 'agua dentro de la región de test\n')

print("*************************************************************************************************************************************************************\n")

print("Vx = ",Vx,"[m/s]\n")
print("Vy = ",Vy,"[m/s]\n")
print("Vz = ",Vz,"[m/s]\n")
print("Temperatura = ",Temperatura,"ºC\n")
print("Reinolds = ",Reinolds,"\n")


