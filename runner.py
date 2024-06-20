import subprocess
import os

bNumberList = []

for i in range(30):
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
        print("Burning Number: "+bNumber)

    #EJECUTAMOS GENETIC CON BNUMBER DE BFF

    dir_genetic = "/mnt/c/Users/Gabriela Alva/OneDrive - Instituto Tecnológico Superior de Purísima del Rincón/Documents/Tesis/repos/CBAG"
    ruta_genetic = os.path.join(dir_genetic, "CBAG")
    instance = "government.csv"
    popSize = "30"
    genNumb = "0"

    # Ejecutar el programa compilado
    ejecucion2 = subprocess.run([ruta_genetic, instance, bNumber, popSize, genNumb], capture_output=True, text=True, cwd=dir_genetic)

    # Verificar si la ejecución fue exitosa
    if ejecucion2.returncode != 0:
        print("Error en la ejecución de Genetic:")
        print(ejecucion2.stderr)
    else:
        print("Salida del programa Genetic:")
        #print(ejecucion2.stdout)
        output_genetic = ejecucion2.stdout.splitlines()
        #secuencia = output_genetic[3] #secuencia es un String
        #secuenciaDividida = secuencia.split() #secuenciaDividida lista de subcadenas

        print(output_genetic[3]) #Linea de tiempo de ejecucion
        #Agregar condicion que imprima cuando sea verified
        print(output_genetic[10]) #Linea de burning sequence
        print(output_genetic[12]) #Linea de burning number
        bNumberList.append(output_genetic[12])

        #secuenciaList = []
        """for i in range(len(secuenciaDividida)-1):
            if(secuenciaDividida[i] == secuenciaDividida[i+1]):
                print(secuenciaDividida[i])
                #secuenciaList.append(secuenciaDividida(i))
                break
            else:
                print(secuenciaDividida[i])
                #secuenciaList.append(secuenciaDividida(i))"""

with open('Dimension 30.txt', 'w') as file:
    for i in range(len(bNumberList)):
        # Escribir valores en el archivo
        file.write(f"{bNumberList[i] }")
    
        

                




    








