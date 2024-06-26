import subprocess
import os
import math

bNumberList = []

#Abrimos el archivo (instancia-x) para leer todas las lineas del archivo
with open('/mnt/c/Users/Gabriela Alva/OneDrive - Instituto Tecnológico Superior de Purísima del Rincón/Documents/Tesis/repos/CBAG/Data/government.csv', 'r') as file:
        # Lee todas las líneas del archivo
        lineas_archivo = file.readlines()

#Obtenemos el numeros de nodos de la instancia-x para calcular el Burning Number   
segunda_linea = lineas_archivo[1].strip()
valores = segunda_linea.split()
bNumber = int(math.sqrt(int(valores[0])))
print("Burn N: "+str(bNumber))

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
    

#EJECUTAMOS GENETIC CON BNUMBER DE BFF

dir_genetic = "/mnt/c/Users/Gabriela Alva/OneDrive - Instituto Tecnológico Superior de Purísima del Rincón/Documents/Tesis/repos/CBAG"
ruta_genetic = os.path.join(dir_genetic, "CBAG")
instance = "crocodile.csv"
popSize = "50"
genNumb = "0"
indices = []

# Ejecutar el programa compilado
ejecucion2 = subprocess.run([ruta_genetic, instance, str(bNumber), popSize, genNumb], capture_output=True, text=True, cwd=dir_genetic)

# Verificar si la ejecución fue exitosa
if ejecucion2.returncode != 0:
    print("Error en la ejecución de Genetic:")
    print(ejecucion2.stderr)
else:
    for indice, contenido_linea in enumerate (ejecucion2.stdout.splitlines(), 0): #Para saber en que lineas del archivo se encuentra lo que se quiere imprimir
         if ("Population burning numbers:" in contenido_linea or "Execution time:" in contenido_linea or "Burning sequence:" in contenido_linea or "Burning number:" in contenido_linea):
              indices.append(indice)
                       
    print("Salida del programa Genetic:")
    output_genetic = ejecucion2.stdout.splitlines()

    print(output_genetic[indices[0]])#Para imprimir population burning numbers
    for i in range(indices[0]+1, indices[1]):
         linea_burningNumbers = output_genetic[i].split()
         linea_burningNumbers = [int(num) for num in linea_burningNumbers]
         bNumberList.extend(linea_burningNumbers)
         print(output_genetic[i])

    print(output_genetic[indices[1]])#Para imprimir execution time
    print(output_genetic[indices[1]+1])
    print(output_genetic[indices[2]]) #Para imprimir burning sequence
    print(output_genetic[indices[2]+1])
    print(output_genetic[indices[3]]) #Para imprimir burning number
    print(output_genetic[indices[3]+1])
    
    

with open('crocodile.txt', 'w') as file:
    for i in range(len(bNumberList)):
        # Escribir valores en el archivo
        file.write(f"{bNumberList[i]} ")
    
        

                




    








