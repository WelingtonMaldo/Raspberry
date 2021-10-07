# LIMPIAR LA TERMINAL HACIENDO UNA FUNCION QUE RECONOZCA EL SISTEMA OPERATIVO QUE ESTÁ USANDO EL PC
# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

  
# print out some text
print('hello geeks\n'*10)
  
# sleep for 2 seconds after printing output
sleep(2)
  
# now call function we defined above
clear()
#'''
from os import system
from time import sleep
system('cls')
#print("comentar")

Saludo = "renfe"

def Var_Name(obj, namespace):
    return[name for name in namespace if namespace[name] is obj] 
   

print("La variable",Var_Name(Saludo, globals()), "es de tipo",type(Saludo)," y contiene el siguiente texto... ",Saludo,"\n")

# sleep for 2 seconds after printing output
sleep(2)

print ("FIN\n")