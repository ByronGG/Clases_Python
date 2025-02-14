/* Merge Sort
    -------------------------------------------------------------------------------------------------------------------------------
    Merge Sort es un algoritmo de ordenamiento eficiente y estable que sigue el paradigma "divide y vencerás". Esto significa que divide el problema en subproblemas más pequeños, los resuelve recursivamente y luego combina las soluciones para obtener el resultado final.

    Es un algoritmo de ordenamiento comparativo, lo que significa que compara elementos para determinar su orden. Además, es un algoritmo estable, lo que garantiza que el orden relativo de elementos iguales se mantenga.
    Características principales de Merge Sort
    Eficiencia en tiempo:

    - Tiempo promedio y peor caso: O(n log n). Esto lo hace mucho más eficiente que algoritmos como Bubble Sort o Insertion Sort, que tienen un tiempo promedio de O(n²).

    - Uso de memoria: Merge Sort requiere memoria adicional para almacenar los subarreglos durante el proceso de mezcla. Su complejidad de espacio es O(n).

    - Estabilidad: Mantiene el orden relativo de elementos iguales, lo que es útil en aplicaciones donde el orden inicial importa.

    - Adecuado para grandes conjuntos de datos: Debido a su eficiencia en tiempo, es ideal para ordenar grandes volúmenes de datos.

    --- Funcionamiento de Merge Sort ---
    El algoritmo se divide en dos fases principales: división y mezcla.
    1. Fase de División: El arreglo original se divide recursivamente en dos mitades hasta que cada subarreglo contenga solo un elemento (o ninguno). Esto se logra dividiendo el arreglo en mitades una y otra vez.

    2. Fase de Mezcla (Merge): Una vez que los subarreglos están divididos, comienza el proceso de mezcla. Los subarreglos se combinan de dos en dos, comparando sus elementos y ordenándolos en un nuevo arreglo. Este proceso se repite recursivamente hasta que todo el arreglo esté completamente ordenado.

    Ventajas de Merge Sort
    - Eficiencia: Su tiempo de ejecución es O(n log n), lo que lo hace adecuado para grandes conjuntos de datos.
    - Estabilidad: Mantiene el orden relativo de elementos iguales.
    - Predecible: Su rendimiento es consistente, sin casos extremos que lo hagan lento.

    Desventajas de Merge Sort
    - Uso de memoria adicional: Requiere espacio adicional proporcional al tamaño del arreglo (O(n)).
    - No in-place: A diferencia de algoritmos como Quick Sort, Merge Sort no ordena los elementos en el mismo arreglo sin usar memoria adicional.

    Aplicaciones de Merge Sort
    - Ordenamiento de grandes conjuntos de datos.
    - Implementación en sistemas donde la estabilidad es importante (por ejemplo, bases de datos).
    - Como base para otros algoritmos más complejos.

    Ejemplo: 
    [38, 27, 43, 3, 9, 82, 10]

    1. División: 
        [38, 27, 43] [3, 9, 82, 10]
        Cada mitad se divide nuevamente hasta obtener subarreglos de un solo elemento
        [38] [27] [43] [3] [9] [82] [10]
    2.  Mezcla
        Se combinan los subarreglos para ordenalos
        - Primero [27, 38] y [3, 43] => [3, 27, 38, 43]
        - Segundo [9, 82] y [10] => [9, 10, 82]
        - Finalmente [3, 27, 38, 43] y [9, 10, 82] => [3, 9, 10, 27, 38, 43, 82]
*/

#include <iostream>
#include <vector>
using namespace std;


/*
vector<int> vec => 1010101101 <== & vector<int> vec_nuevo 1010101101
*/


// Funcion para mezclar dos subarreglor y ordenarlos
void merge(vector<int>& arr, int left, int mid, int right){
    int n1 = mid - left + 1; // Tamaño del subarreglo izquirdo
    int n2 = right - mid; // Tamaño del subarreglo derecho

    // Crear arreglos temporales (aux)
    vector<int> L(n1), R(n2); // L(n1) [] - R(n2) []

    // Copiar datos a los arreglos temporales
    for(int i = 0; i < n1; i++)
        L[i] = arr[left + i]; // [38, 27, 43]
    for(int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j]; // [3, 9, 82, 10]

    // Mazclar los arreglos temporales en el arreglo original
    int i = 0, j = 0, k = left; // Variables aux
    while(i < n1 && j < n2) {
        if(L[i] <= R[j]){
            arr[k] = L[i]; // L Si es menor o igual a R
            i++; // <- Actualiza la posición si se cumple la condición
        } else {
            arr[k] = R[j]; // R es menor o igual a L
            j++; // <- Actualiza la posición si se cumple la condición
        }
        k++;
    }
    /*
    L => [38, 27, 43]
          0    1   2   <== Indices que es lo que lleva el contexto del bucle
    R => [3, 9, 82, 10]
          0  1   2   3  <== Indices
    K => [3, 9, 38, 27, 43, 82, 10]
          0  1   2   3
    */

    // Copiar los elementos restantes de L (si los hay)
    while (i < n1){
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copiar los elementos restantes de R (si lo hay)
    while(j < n2){
        arr[k] = R[j];
        j++;
        k++;
    }

    // Imprimir el estado del arreglo despues de la mezcla
    cout << "Mezclado: ";
    for (int i = left; i <= right; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Funcion principal del MERGE SORT
void mergeSort(vector<int>& arr, int left, int right){
    if(left < right){
        int mid = left + (right - left) / 2; // Punto medio

        // Imprimir la división actual
        cout << "Dividiendo: ";
        for(int i = left; i <= right; i++){
            cout << arr[i] << " ";
        }
        cout << endl;

        // Ordenar la primera y segunda mitad
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Mezclar las dos mitades ordenadas
        merge(arr, left, mid, right);
    }
}


int main(){
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};

    cout << "Arreglo original: ";
    for(int num : arr){
        cout << num << " ";
    }
    cout << endl << endl;

    // Llamar a Merge Sort
    mergeSort(arr, 0, arr.size() - 1);

    cout << endl << "Arreglo ordenado: ";
    for(int num : arr){
        cout << num << " ";
    }
    cout << endl;
    return 0;
}

/*
    Explicación del código
    - Función merge:
    Combina dos subarreglos ordenados (L y R) en un solo arreglo ordenado.
    Imprime el estado del arreglo después de cada mezcla.
    - Función mergeSort:
    Divide el arreglo en mitades recursivamente hasta que cada subarreglo tenga un solo elemento.
    Imprime el estado del arreglo durante cada división.
    Llama a la función merge para combinar los subarreglos ordenados.
    - Función main:
    Inicializa el arreglo y llama a mergeSort para ordenarlo.
    Imprime el arreglo original y el arreglo ordenado.
*/