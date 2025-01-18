/* Algoritmos de Ordenamiento
    ---------------------------------------------------------------------------------------------------------------------------
    Un algoritmo de ordenamiento organiza los elementos de una colección (como un arreglo) en un orden específico, generalmente ascendente o descendente. Hay varios algoritmos de ordenamiento, como:
    Ordenamiento por Inserción (Insertion Sort)
    Ordenamiento por Selección (Selection Sort)
    Ordenamiento Burbuja (Bubble Sort)
    Merge Sort
    Quick Sort
    Heap Sort, entre otros.

    Insertion Sort
    Organiza los elementos comparádolos con lso ya ordenados y los inserta en su posición correcta, (Es como ordenaras cartas en tu mano)
    - Comieza con el segundo elementos posición = 1 (el primero ya se consera ordenado posición = 0)
    - toma el segundo elemento y compara con el primero (pos 0 > 1 o 0 < 1 )
    - Avanzar al tercer elemento y comprarlos con lso anteriores ([0][1][2])
    - Repite hacia la derecha de los elementos que sean mayores que este hasta encontrar su posicion correcta

*/

#include <iostream>
#include <vector>

using namespace std;

void printArray (const std::vector<int>& arr){
    for (int num: arr){
        std::cout<<num<<" ";
    }
    std::cout<<std::endl;
}

void insertionSort(std::vector<int>& arr){
    int n = arr.size();
    for(int i = 1; i < n; i++){
        int key = arr[i]; // Elemento actual
        int j = i - 1;
        // Iteraciones
        std::cout <<"Iretacion "<< i << ", elemento a insertar: " << key << std::endl;
        while(j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j];
            j--;
        // Imprimir
        std::cout << "Intercambio: ";
        printArray(arr);
        }
        // Insertar el elemento en la posición correcta
        arr[j+1] = key;
        // Imprimir el estado del arreglo desúes de la inserción
        std::cout << "Despues de insertar: ";
        printArray(arr);
        std::cout << "--------------------" <<std::endl;
    }
}

/* Algoritmo Insercion puro 
void insertionSort(std::vector<int>& arr){
    int n = arr.size();
    for(int i = 1; i < n; i++){
        int key = arr[i]; // Elemento actual
        int j = i - 1;
        while(j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j];
            j--;
        }
        // Insertar el elemento en la posición correcta
        arr[j+1] = key;
    }
}
*/

int main(){
    std::cout<<"Arreglo antes de ordenarlo: ";
    std::vector<int> arr = {8, 4, 6, 2, 9, 1, 5, 3, 0};
    printArray(arr);

    insertionSort(arr);
    std::cout<<"Arreglo ordenado: ";
    printArray(arr);

    return 0;
}