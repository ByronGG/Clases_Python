/*
    Complejidad algorítmica
    Mide cómo crece el tiempo (o la memoria) de un algoritmo cuando crece el tamaño de la entrada n, Se usa la notación Big O, que describe el peor caso e ignora constantes.

    Notación            Nombre              Ejemplo
    O(1)                Contante            Acceder a arr[i]
    O(log n)            Logarítmica         Búsqueda binaria
    O(n)                Lineal              Búsqueda lineal, reccorer un arreglo
    O(n log n)          Lineal-logarítmica  Merge sort, quicksort(promedio)
    O(n^2)              Cuadrática          Burbuja, selección, inserción
    O(2^n)              Exponecial          Fibonacci recursivo ingenuo

    De mejor a peor: O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)
*/

// Como calcularla
// un cliclo simple -> O(n)
for (int i = 0; i < n; i++) { ... }

// Ciclos anidados -> O(n^2)
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) { ... }

// La variable se divide a la mitad cada vez... -> O(log n)
for (int i = n; i > 1; i /= 2) { ... }

/*
    Las reglas práticas son estas: se eliminan las contantes (O(3n) = O(n)). se conrva el término domiante (O(n^2+n)= O(n^2)), los ciclos anidados se multiplican y los consercutivos se suman!!!

    Mejor, promedio y peor caso: en búsqueda lineal, el mejor caso es O(1) (elemento está al inicio) y el peor es O(n) (está al final o no existe).

    Complejidad espacial: mide la moeria extra. Un algoritmo recursivo con profundidad n usa O(n) de espacio en la pila
*/

// Búsqueda lineal: O(n): Recorre elemento por elemento. Funciona con datos desordenados
template <typename T>
int busquedaLineal(const T arr[], int n, T objetivo){
    for (int i = 0; i < n; i++)
        if (arr[i] == objetivo) return i;
    return -1; // no encontrado
}

// Búsqueda binaria: O(log n): Requiere que el arreglo esté ordenado. Compara con el elemento de medio y descarta la mitdad cada paso

template <typename T>
int busquedaBinaria(const T arr[], int n, T objetivo){
    int izq = 0, der = n - 1;
    while(izq <= der){
        int mid = izq + (der - izq) / 2; //evita desbordamiento
        if(arr[mid] == objetivo) return mid;
        if(arr[mid] < objetivo) izq = mid + 1;
        else der = mid - 1;
    }
    return -1;
}