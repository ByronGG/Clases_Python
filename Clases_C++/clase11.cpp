/* Quicksort
    ------------------------------------------------------------------------------------------------------------------------
    Es un algoritmo de ordenamiento muy eficiente que utiliza la ténica de divide y vencerás

    ¿Cómo funciona?
    El quicksort funciona dividiendo un arreglo en sub-arreglos más pequeños, ordenandolos de forma recursiva
    - Eligir un pivote: Selecciona un elemento de arreglo, conocido como el "pivote". Puede ser el primer elemento, 
        el último, uno al azar o incluso el elemento central.
    - Particionar el arreglo: Reoganiza el arreglo de manera que todos los elementos menores que el pivote quedan a su izquierda
        todos los elementos mayores que el pivote queden a su derecha, el pivote se coloca en su posicion final
    - Aplicar recursividad: Aplica los mismo pasos al sub-arreglo izquierdo (elementos menores que el pivote), Aplica los mismos 
        pasos al sub-arreglo derecho (elementos mayores que el pivote).
    - Base del caso recursivo: Cuando el sub-arreglo tiene 0 a 1 elementos, ya está ordenado.

    Ventejas:
    - Algoritmos más rádipos en la práctica, con complejidad promedio O(n log n)
    - Funciona muy bien en arreglos grandes

    Desventajas:
    - En el peor de los casos (si el pivote es el más grande o el más pequeño en cada partición), si complejidad es O(n^2)
    - No es estable, es decir, no conserva el orden relativo de los elementos iguales

    ¿CUANDO NO USAR QUICKSORT?
    - Cuando el arreglo ya está casi ordenado o tiene pocos elementos
    - Cuando necesitas un algoritmo estable (en ese caso, Merge Sort es de lo mejor opcion en algoritmos estables)
    - Cuando el costo de tiempo en el peor de los casos es crítico (puedes implementar estrategias para mitigiar, como elegir 
    un mejor pivote)
*/

#include <iostream>
#include <vector>
using namespace std;

// Funcion para imprir el array
void printArray (const std::vector<int>& arr){
    for (int num: arr){
        cout<<num<<" ";
    }
    cout<<std::endl;
}

// Función para la partición
int partition(vector<int>& arr, int low, int high){
    int pivot = arr[high]; // Elegimos el valor como pivote (Es el ultimo = high)
    cout << "Pivote elegido: "<<pivot<<endl; // Impreción de que número será el pivote
    int i = low - 1; // Índice del elemento más pequeño
    
    for(int j = low; j < high; j++){
        cout <<"Comparando: "<<arr[j]<< " <= "<<pivot<<endl;
        if(arr[j] <= pivot){
            i++;
            swap(arr[i], arr[j]); // Coloca los elementos menores que el pivote a la izquierda
            cout<<"Intercambio: "<< arr[i] <<" con " <<arr[j] << " -> ";
            printArray(arr);
        }
    }
    // Colocar el pivote en su posicion correcta
    swap(arr[i + 1], arr[high]);
    cout << "Pivote: " << pivot <<" colocado en su posicion -> ";
    printArray(arr);
    return i + 1; // Retorno la posición del pivote 
}

// Funcion Quicksort revusiva
void quickSort(vector<int>& arr, int low, int high){
    if(low < high){
        cout <<"\nOrdenado entre indices ["<< low <<", "<< high <<"] -> ";
        printArray(arr);

        // Particionar el arreglo
        int pi = partition(arr, low, high); // variable que almacena el return de una función
        cout <<"Particion completa, indice del pivote: "<< pi <<endl;

        // Ordenar los sub-arreglos de forma revursiva
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main(){
    vector<int> arr = {5, 9, 13, 8, 7, 41, 23, 50, 59, 19, 1024, 11, 82, 76, 10};
    cout << "Arreglo incial: ";
    printArray(arr);

    quickSort(arr, 0, arr.size() - 1);
    cout << "\nArreglo ordenado: ";
    printArray(arr);

    return 0;
}


/* QuickSort - Algoritmo PURO
int partition(vector<int>& arr, int low, int high){
    int pivot = arr[high]; 
    int i = low - 1; 
    for(int j = low, j < high; j++){
        if(arr[j] <= pivot){
            i++;
            swap(arr[i], arr[j]); 
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1; 
}


void quickSort(vector<int>& arr, int low, int high){
    if(low < high){
        int pi = partition(arr, low, high); 
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
*/
