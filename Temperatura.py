#En esta parte se importan las librerias necesarias para ejecutar el codigo

import os
import glob
import time

#En esta seccion se llaman a los comandos necesarios para obtener la informacion de los pines GPIO de la raspberry
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

Direccion = '/sys/bus/w1/devices'
Dispositivo_folder = glob.glob(Direccion+'28*')[0]
Dispositivo_Path = Dispositivo_folder+'/w1_slave'

def Leer_Temperatura():
    f = open(Dispositivo_Path, 'r')
    lineas = f.readlines()
    f.close
    return lineas

def Determinar_valores():
    lineas = Leer_Temperatura()
    while lineas [0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lineas = Leer_Temperatura()
    Igual_pos = lineas[1].find('t=')
    if Igual_pos != -1:
        temp_string = lineas[1][Igual_pos+2:]
        Temperatura_Celsius = float(temp_string)/1000.0
        Temperatura_Fahrenheit = Temperatura_Celsius*9.0/5.0+32.0
        return Temperatura_Celsius, Temperatura_Fahrenheit
while True:
    print('Centigrados Fahrenheit\n')
    print(Determinar_valores())
    time.sleep(1)
