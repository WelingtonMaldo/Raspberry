#Se importan dos librerias
# 1a libreria  = para configurar los pines GPIO
# 2a libreria para hacer delays

#git config --global user.email "welington.maldo@gmail.com" 
#git config --global user.name "WelingtonMaldo"
#git branch -M main
#git push -u origin main


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
Pin_1 = 11
Pin_2 = 13
Contador = 0
Resto = 0
Continuar = True
Temporizador = 3.5
Delay_1 = 0.1
Delay_2 = 0.2
Divisor = 10

GPIO.setup(Pin_1, GPIO.OUT, initial = 0)
GPIO.setup(Pin_2, GPIO.OUT, initial = 0)


while Continuar == True:
    Contador = Contador+1
    Resto = Contador%Divisor
    #print('Contador = ',Contador,'\n')

    GPIO.output(Pin_1,True)
    GPIO.output(Pin_2,True)
    time.sleep(Delay_1)
    GPIO.output(Pin_1,False)
    GPIO.output(Pin_2,True)
    time.sleep(Delay_1)
    GPIO.output(Pin_1,True)
    GPIO.output(Pin_2,False)
    time.sleep(Delay_1)
    GPIO.output(Pin_1,False)
    GPIO.output(Pin_2,True)
    time.sleep(Delay_1)
    GPIO.output(Pin_1,True)
    GPIO.output(Pin_2,False)
    GPIO.output(Pin_1,False)
    
    time.sleep(Delay_2)
    if Resto ==  0:
        
        print('Temporizador: %g segundos para responder'%Temporizador)
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
           # sys.exit()                         Esta linea termina la ejecucion completa
    
