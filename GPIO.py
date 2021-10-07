#Se importan dos librerias
# 1a libreria  = para configurar los pines GPIO
# 2a libreria para hacer delays

from RPi import GPIO
#import RPi.GPIO as GPIO
import time

#Se configura los pines de la raspberry
GPIO.setmode(GPIO.BOARD)                           #Esto es para poder llamar a los Pines conforme estan numerado "fisicamente" en la raspberry 
GPIO.setup(7, GPIO.out)

