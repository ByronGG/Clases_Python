/*
    Algoritmo de ordenamiento basado en su notación
*/

// Selección (Selection Sort): O(n^2)
// Busca el mínimo del resto del arreglo y lo coloca en la posición actual.

#include<iostream>

void seleccion(int arr[], int n){
    for(int i = 0; i < n - 1; i++){
        int min = i; // AUX
        for(int j = i + 1; j < n; j++){
            if (arr[j] < arr[min]) min = j;
        std::swap(arr[i], arr[min]);
        }
    }
}

// Merge Sort: O(n log n) siempre
//Usa la estrategia de divide y vencerás: divide el arreglo a la mitad, ordena cada mitad recursivamente y luego mezcla las dos mitades
// Este ejemplo junta recursividad + memoria dinamica + complejidad, por eso aparece en muchos examanes!!!!

void merge(int arr[], int izq, int mid, int der){
    int n1 = mid - izq + 1, n2 = der - mid;
    int* L = new int[n1];
    int* R = new int[n2];
    for (int i = 0; i < n1; i++) L[i] = arr[izq + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = izq;
    while (i < n1 && j < n2){
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    delete[] L;
    delete[] R;
}

void mergeSort(int arr[], int izq, int der){
    if (izq >= der) return;
    int mid = izq + (der - izq) / 2;
    mergeSort(arr, izq, der);
    mergeSort(arr, mid + 1, der);
    merge(arr, izq, mid, der);
}


// Inserción (Insertion Sort): O(n^2), pero muy bueno con datos CASI ordenados
// Funciona como ordenar cartas en la mano; toma un elemento y lo interta en su lugar dentro de la parte ya ordenada

void insercion(int arr[], int n){
    for (int i = 1; i < n; i++){
        int clave = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > clave){
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = clave;
    }
}

// Quick sort: O(n log n) en un caso promedio, O(n^2) en el peor de los casos
// Elige un pivote, pone lo menores a su izquierda y los mayores a su derecha, y luego repiute el proceso en cada lado

int particion(int arr[], int bajo, int alto){
    int pivote = arr[alto];
    int i = bajo - 1;
    for (int j = bajo; j < alto; j++){
        if (arr[j] < pivote){
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[alto]);
    return i + 1;
}

void quickSort(int arr[], int bajo, int alto){
    if(bajo < alto){
        int p = particion(arr, bajo, alto); // Particiones del arreglo y swapeos
        quickSort(arr, bajo, p - 1); // Ordenamos bajo
        quickSort(arr, p + 1, alto); // Ordenamos alto
    }
}
