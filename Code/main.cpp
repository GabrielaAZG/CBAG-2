#include "main.hpp"
// Para calcular el tiempo de ejecución
#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int32_t main(int argc, char **argv)
{
    string fileName = argv[1];
    int b = strtol(argv[2], NULL, 10);
    // Agregado
    int populationSize = strtol(argv[3], NULL, 10);
    int numberGenerations = strtol(argv[4], NULL, 10);
    vector<int> optSolution;

    Solver G1(fileName, b, populationSize, numberGenerations);

    auto inicioReloj = high_resolution_clock::now();

    vector<int> solution = G1.solve();

    auto finReloj = high_resolution_clock::now();

    duration<double> duracionEjecucion = (finReloj - inicioReloj);
    cout << "Tiempo de ejecución: " << duracionEjecucion.count() << "\n";

    // Esto imprime la solucion larga
    for (auto node : solution)
        cout << node << " ";
    cout << endl;

    Checker checkG1(fileName);
    if (checkG1.check(solution, 1))
    { // Si la solucion larga es valida
        cout << BOLD(FGRN("Verified!")) << endl;
        for (int i = 0; i <solution.size(); i++)
        {
            optSolution.push_back(solution[i]);
            if (checkG1.check(optSolution, 0))
            {      
                //cout << BOLD(FGRN("Verified!")) << endl;
                break;
            }
        }
        // Imprimimos la secuencia de quemado y el burning number
        cout << "Burning sequence:" << "\n";
        for (auto number : optSolution)
        {
            cout << number << " ";  
        }
        cout << "\n"
        << "Burning number:" << "\n";
        cout << optSolution.size() << "\n";
    }
    else
    {
        cout << BOLD(FRED("NOT Verified!")) << endl;
    }

    

    /*//Guardar valores en un archivo
    ofstream archivo("Dimension30.txt");

    // Verificar si se pudo abrir el archivo
    if (archivo.is_open()) {
        // Iterar sobre el vector e imprimir cada elemento en el archivo
        for (double elemento : bNumberSave) {
            archivo << elemento << " ";
        }

    // Cerrar el archivo
        archivo.close();

        cout << "Valores escritos en el archivo" << endl;
    } else {
        cout << "No se pudo abrir el archivo." << endl;
    }*/

    /*vector<int> tempo = {6930, 3494, 4546, 3271, 2215, 2215};
    if (checkG1.check(tempo, 1)){
        cout << BOLD(FGRN("Verified! ")) << endl;

    }else{
        cout << BOLD(FRED("NOT Verified!")) << endl;
    }*/
}
