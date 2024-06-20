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
    // vector <int> bNumberSave;
    vector<int> bsequence;

    // for (int i = 0; i < 30; i++){

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

    int temp; // Variable para almacenar el ultimo valor que se quito del vector solution
    Checker checkG1(fileName);
    if (checkG1.check(solution, 1))
    { // Si la solucion larga es valida
        cout << BOLD(FGRN("Verified!")) << endl;
        for (int i = solution.size() - 1; i >= 0; i--)
        {
            temp = solution.back(); // Guardamos el ultimo valor del vector solution, se guarda en temp
            solution.pop_back();    // Eliminamos el ultimo valor del vector solution

            if (!checkG1.check(solution, 1))
            {                             // Si vector solution no tiene una secuencia valida
                solution.push_back(temp); // Se le agrega el ultimo valor que se habia quitado para tener el vector solution optimo
                break;                    // Rompemos el ciclo for ya que se ha encontrado la solucion optima
            }
        }
        // Imprimimos la secuencia de quemado y el burning number
        cout << "Burning sequence:" << "\n";
        for (auto number : solution)
        {
            if (number != 0)
            {
                bsequence.push_back(number);
                cout << number << " ";
            }
        }
        cout << "\n"
             << "Burning number:" << "\n";
        // bNumberSave.push_back(solution.size());
        // cout<<solution.size()<<"\n";
        cout << bsequence.size() << "\n";
    }
    else
    {
        cout << BOLD(FRED("NOT Verified!")) << endl;
    }

    //}

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

    // vector<int> tempo = {99, 198, 1, 142, 93, 59, 176, 145};
    /*if (checkG1.check(tempo, 1)){
        cout << BOLD(FGRN("Verified! ")) << endl;

    }else{
        cout << BOLD(FRED("NOT Verified!")) << endl;
    }*/
}
