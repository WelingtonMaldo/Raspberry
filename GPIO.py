#Se importan dos librerias
# 1a libreria  = para configurar los pines GPIO
# 2a libreria para hacer delays

from RPi import GPIO
#import RPi.GPIO as GPIO
import time
import sys, select
from os import system

system('clear')    #Limpiar la terminal 

#Se configura los pines de la raspberry
GPIO.setmode(GPIO.BOARD)                           #Esto es para poder llamar a los Pines conforme estan numerado "fisicamente" en la raspberry 
GPIO.setup(7, GPIO.OUT)
Contador = 0
Resto = 0
Continuar = True
Temporizador = 3

while Continuar == True:
    Contador = Contador+1
    Resto = Contador%5
    #print('Contador = ',Contador,'\n')

    GPIO.output(7,True)
    time.sleep(0.2)
    GPIO.output(7,False)
    
    
    time.sleep(0.25)
    if Resto ==  0:
        i = 0
        print('Temporizador: %d segundos para responder'%Temporizador)
        print("¿Se desea parar la ejecución? (Y/N)\n")
        
        i, o, e = select.select( [sys.stdin], [], [], Temporizador)

        if (i):
            Respuesta = sys.stdin.readline().strip()
            print('\nLa respuesta es...',Respuesta )
        else:
            Respuesta = 'N'
            print("No se obtuvo respuesta del usuario\n")

        if Respuesta.upper() == 'Y':
            print("Se finaliza la ejecución\n")
            Continuar=False
           # sys.exit()
    





