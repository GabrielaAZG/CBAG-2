import subprocess
import os
import math

bNumberListG0 = []
bNumberListGF = []
LevDistancesG0 = []
LevDistancesGF = []

instance =  input("Instance: ")
popSize = input("Population size: ")
genNumb = input("Number of generations: ")

dir = '/mnt/c/Users/Gabriela Alva/OneDrive - Instituto Tecnológico Superior de Purísima del Rincón/Documents/Tesis/repos/CBAG/Data'
filename = f'{instance}.csv'
path = os.path.join(dir, filename)

#Abrimos el archivo (instancia-x) para leer todas las lineas del archivo
with open(path, 'r') as file:
        # Lee todas las líneas del archivo
        lineas_archivo = file.readlines()

#Obtenemos el numeros de nodos de la instancia-x para calcular el Burning Number   
segunda_linea = lineas_archivo[1].strip() #En la segunda linea esta el numero de nodo, usamos strip (para eliminar espacios en blanco)
valores = segunda_linea.split() #split separa la linea en subacdenas
bNumber = int(math.sqrt(int(valores[0]))) #La primer subcadena es el numero de nodos. Hacemos el calculo de raiz cuadrada a ese numero
print("Desired Burn N: "+str(bNumber)) #Imprimimos el burning number deseado

'''for i in range(30): 
    #OBTENEMOS BURNING NUMBER DEL BFF

    bNumber = ""

    #Ruta del ejecutable
    dir_bff = "/mnt/c/Users/Gabriela Alva/OneDrive - Instituto Tecnológico Superior de Purísima del Rincón/Documents/Tesis/repos/bff_alg"
    ruta_bff = os.path.join(dir_bff, "bff_alg")

    arg1 = "dataset/government.mtx"
    arg2 = "bff"

    # Ejecutar el programa compilado
    ejecucion = subprocess.run([ruta_bff, arg1, arg2], capture_output=True, text=True, cwd=dir_bff)

    # Verificar si la ejecución fue exitosa
    if ejecucion.returncode != 0:
        print("Error en la ejecución de BFF:")
        print(ejecucion.stderr)
    else:
        #print("Salida del programa:")
        #print(ejecucion.stdout)
        output_bff = ejecucion.stdout.splitlines() 
        bNumber = output_bff[3] #En la cuarta línea del output se encuentra el burning number
        print("Burning Number: "+bNumber)'''
    

#EJECUTAMOS GENETIC CON BNUMBER PREVIAMENTE CALCULADO

dir_genetic = "/mnt/c/Users/Gabriela Alva/OneDrive - Instituto Tecnológico Superior de Purísima del Rincón/Documents/Tesis/repos/CBAG"
ruta_genetic = os.path.join(dir_genetic, "CBAG")
#instance = "polblogs.csv"
#popSize = "100"
#genNumb = "500"


# Ejecutar el programa compilado
ejecucion2 = subprocess.run([ruta_genetic, instance+".csv", str(bNumber), popSize, genNumb], capture_output=True, text=True, cwd=dir_genetic)

# Verificar si la ejecución fue exitosa
if ejecucion2.returncode != 0: #Si la ejecucion no fue exitosa
    print("Error en la ejecución de Genetic:")
    print(ejecucion2.stderr)
else: #Si la ejecuciom fue exitosa              
    print("Salida del programa Genetic:")
    output_genetic = ejecucion2.stdout.splitlines()

    #Colocamos que lineas queremos que se impriman de la salida de Genetic
    for i in range(0,22):
        if i not in [0, 1, 2, 6, 12, 16, 17]:
            print(output_genetic[i])

    bNumberListG0.append(output_genetic[4]) 
    LevDistancesG0.append(output_genetic[6])
    bNumberListGF.append(output_genetic[10])
    LevDistancesGF.append(output_genetic[12])
    '''for i in range(0,12):
        if i not in [0, 1, 2, 6, 7]:
            print(output_genetic[i])

    bNumberListG0.append(output_genetic[4]) '''
    
#Burning number Generacion inicial
with open('tvshow100G0.txt', 'w') as file:
    for i in range(len(bNumberListG0)):
        # Escribir valores en el archivo
        file.write(f"{bNumberListG0[i]} ")

#Levenshtein Distances G0
with open('levtvshow100G0.txt', 'w') as file:
    for i in range(len(LevDistancesG0)):
        # Escribir valores en el archivo
        file.write(f"{LevDistancesG0[i]} ")

#Burning numbers Generacion final
with open('tvshow100GF.txt', 'w') as file:
    for i in range(len(bNumberListGF)):
        # Escribir valores en el archivo
        file.write(f"{bNumberListGF[i]} ")
    

#Levenshtein Distances GF
with open('levtvshow100GF.txt', 'w') as file:
    for i in range(len(LevDistancesGF)):
        # Escribir valores en el archivo
        file.write(f"{LevDistancesGF[i]} ")


        

                




    








