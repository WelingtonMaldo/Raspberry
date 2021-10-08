#Se importan dos librerias
# 1a libreria  = para configurar los pines GPIO
# 2a libreria para hacer delays

#from RPi import GPIO
import RPi.GPIO as GPIO
import time
import sys, select
from os import system

system('clear')    #Limpiar la terminal 

print('                     Secuencia de encendido y apagado del LED                    \n ')

#Se configura los pines de la raspberry
GPIO.setmode(GPIO.BOARD)

# GPIO 4
#BOARD --> GPIO.setup(7, GPIO.OUT)  --> Corresponde a la posición fisica en la placa Raspberry
#BCM   --> GPIO.setup(4, GPIO.OUT)  --> Corresponde al numero de GPIO que esta descrito en la memoria interna

GPIO.setup(7, GPIO.OUT, initial = 0)
GPIO.setup(11, GPIO.OUT, initial = 0)
Contador = 0
Resto = 0
Continuar = True
Temporizador = 1.5

while Continuar == True:
    Contador = Contador+1
    Resto = Contador%5
    #print('Contador = ',Contador,'\n')

    GPIO.output(7,True)
    GPIO.output(11,True)
    time.sleep(0.2)
    GPIO.output(7,False)
    GPIO.output(11,True)
    time.sleep(0.2)
    GPIO.output(7,True)
    GPIO.output(11,False)
    time.sleep(0.2)
    GPIO.output(7,False)
    GPIO.output(11,True)
    time.sleep(0.2)
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(7,False)
    
    time.sleep(0.25)
    if Resto ==  0:
        
        print('Temporizador: %g segundos para responder'%Temporizador)
        print("¿Se desea parar la ejecución? (Y/N)\n")

        i, o, e = select.select( [sys.stdin], [], [], Temporizador)
        
        if (i):
            Respuesta = sys.stdin.readline().strip()
            print('\nLa respuesta es...',Respuesta )
            Respuesta = ''
        else:
            Respuesta = 'N'
            print("No se obtuvo respuesta del usuario\n")

        if Respuesta.upper() == 'Y':
            print("Se finaliza la ejecución\n")
            Continuar=False
           # sys.exit()
    





