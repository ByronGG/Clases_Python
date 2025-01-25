/* ARRAYS
    -------------------------------------------------------------------------------------------------------------------------
    Un array es una coleeción de elementos del mismo tipo almacenados en ubicaciones de memoria contiguas. Se usa para
    almacenar múltiples valores bajo un único nombre.

    - Array unidimensionales: Un array contiene una sola fila de elemento, el índice del array comenza en 0, el tamaño del array
    del fijo y se debe especificar en el momento de la declaración. 

    - Array bidimensionales: Un array que almacena datos en forma de filas y columnas

    - Array Tridimensionales: Un array que alamacena dos datos en tres dimensiones. 

    A) Declaración e inicialización simultánea
        int numeros[5] = {1,2,3,4,5};

    B) Inicialización sin asginar todos los valores
        int numeros[5] = {1,2}; // El resto serán 0 por defecto

    C) Inicialización automática del tamaño
        int numeros[] = {1,2,3,4,5}; // El tamaño se calcula automáticamente (5 elementos)

    Limitacipnes de los arrays
    Tamaño fijo: No puedes cambiar el tamaño de un array después de su declaración
    No hay control de límites: Acceder a índices fuera del rango puede causar errores de memoria

    Pasar un arraya a un función
    Los arrays se pasan por refencia (se pasa la dirección de memoria del primer elemento)

    En C++, puedes usar la calse std::array de la biblioteca estándar para trabajar cona rray de forma más segura. 
    Recorrer un arraya usando for-each (C++ 11 o posterir)
        for(int valor : array){
            cout<<valor<<" ";
        }

    Libreria <algorithm>
    sort(arr, arr + 5); // Orden ascendente
    sort(arr, arr + 5, great<int>()); // Orden descendente
*/

#include <iostream>
#include <array> // Libreria de array
#include <algorithm> // Libreria para algoritmos básicos
using namespace std;

void imprimirArray(int arr[], int size){
    for(int i = 0; i < size; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int numero[5] = {1,2,3,4,5}; // Array de 5 elementos, declarados en el corchete [5] Unidimencional
    int matriz[2][3] = {{1,2,3}, {4,5,6}}; // Matriz de 2x3 Bidimencional
    int cubo[2][2][2] = {
        {{1,2}, {3,4}},
        {{5,6}, {7,8}}
    };
    array<int, 5> digitos = {1,2,3,4,5}; // Declaración de un arrray usando la libreria <array>
    int arr[5] = {3,5,2,9,7};

    int numeros[10] = {10,20,30,40,50,60,70,80,90,100};

    imprimirArray(numeros, 10); // Llamamos a imprimirArray con los parametros declarados (array y tamaño)

    // Acceso a los elementos
    for(int i = 0; i < 5; i++){
        cout <<"Elemento "<<i<<": "<<numero[i]<<endl;
    }

    // Acceso a los elementos de la matriz 2x3
    for(int i= 0; i < 2; i++){
        for(int j = 0; j < 3; j++){
            cout<<"Elemento [" <<i<<"]["<<j<<"]: "<<matriz[i][j]<<endl;
        }
    }

    // Acceso a los elementos de la matriz de tres dimensiones
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            for(int k = 0; k < 2; k++){
                cout<<"Elemento ["<<i<<"]["<<j<<"]["<<k<<"]: "<<cubo[i][j][k]<<endl;
            }
        }
    }

    cout << "-------------------------------------------------" <<endl;
    int n;
    cout<<"Tamanio del array: ";
    cin >> n;

    // Asiganción dinámica
    int* array = new int[n];
    // Asignar valores
    for(int i = 0; i < n; i++){
        array[i] = i*10;
    }
    //Imprimir valores
    for(int i = 0; i < n; i++){
        cout<<array[i]<<" ";
    }

    for(int i = 0; i < digitos.size(); i++){
        cout<< digitos[i] <<endl;
    }

    cout << "-------------------------------------------------" <<endl;

    int i = 0;
    while (i < 3){
        cout<<arr[i]<<endl;
        i++;
    }

    cout << "-------------------------------------------------" <<endl;

    int max = arr[0];
    for(int i = 1; i < 5; i++){
        if(arr[i]> max){
            max = arr[i];
        }
    }
    cout<<"Maximo: "<<max<<endl;

    int min = arr[0];
    for(int i = 1; i < 5; i++){
        if(arr[i]<min){
            min = arr[i];
        }
    }
    cout<<"Minimo: "<<min<<endl;

    int suma = 0;
    for(int i = 0; i < 5; i++){
        suma += arr[i];
    }
    float promedio = (float)suma / 5;
    cout <<"Promedio: "<<promedio<<endl;

    cout << "-------------------------------------------------" <<endl;

    int buscar = 20;
    bool encontrado = false;
    for(int i = 0; i < 5; i++){
        if(arr[i] == buscar){
            encontrado = true;
            cout <<"Elemento encontrado en el indice: "<< i <<endl;
            break;
        }
    }
    if(!encontrado){
        cout<<"Elemento no encontrado!"<<endl;
    }

    cout << "-------------------------------------------------" <<endl;

    cout<<"Array inicial: ";
    for(int i = 0; i < 5; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    // Ordena ascendente burbuja
    for(int i = 0; i < 5 - 1; i++){
        cout <<"iretacion " << i + 1 <<": "<<endl;
        for(int j = 0; j < 5 - i - 1; j++){
            if(arr[j] > arr[j + 1]){
                // Intercambio
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                // Imprimir el array despues del intercambio
                cout<<" Cambio arr["<<j<<"] y arr[" <<j+1<<"]: ";
                for(int k = 0; k < 5; k++){
                    cout<<arr[k]<<" ";
                }
                cout<<endl;
            }
        }
    }

    // ALGORITMO BURBUJA SIN IMPRECIONES
    // for(int i = 0; i < 5 - 1; i++){
    //     for(int j = 0; j < 5 - i - 1; j++){
    //         if(arr[j] > arr[j + 1]){
    //             int temp = arr[j];
    //             arr[j] = arr[j + 1];
    //             arr[j + 1] = temp;
    //         }
    //     }
    // }

    cout<<"Array ordenado con burbuja: ";
    for(int i = 0; i < 5; i++){
        cout <<arr[i]<<" ";
    }
    cout <<endl;

    return 0;
}