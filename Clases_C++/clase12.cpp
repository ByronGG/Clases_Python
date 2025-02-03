/*  Vectores
    --------------------------------------------------------------------------------------------------
    Los vectores en C++ son una de las estructuras de datos más útiles y versátiles de la STL (Standard Template Library). A diferencia de los arrays tradicionales, los vectores son dinámicos, lo que significa que pueden cambiar de tamaño durante la ejecución del programa.

    Un vector es una secuencia contigua de elementos que pueden cambiar de tamaño dinámicamente. Es similar a un array, pero con las siguientes ventajas:
    - Tamaño dinámico: Puedes agregar o eliminar elementos en tiempo de ejecución.
    - Gestión automática de memoria: No necesitas preocuparte por la asignación y liberación de memoria.
    - Funcionalidades integradas: La STL proporciona muchas funciones útiles para trabajar con vectores.

    Sintaxis Básica
    vector<tipo_dato> nombre_vector;
    tipo_dato: El tipo de los elementos que almacenará el vector (ejemplo int, double, string, etc)
    nombre_vector: El nombre de la variable que representa el vector.

    Ejemplo:
        vector<int> numeros; // Vector de enteros
        vector<double> precios; // Vector de números decimales
        vector<string> palabras; // Vector de cadenas de texto
    
    Inicilizar con tamaño inicial
    vector<int> lista_numeros[5]; // Inicia con el número 5 => vector = [5] 
    vector<int> lista_numeros(5); // Inicia con 5 valores => vector = [0][0][0][0][0]

    Inicia el tamaño y valor inical (tamaño 5 y todos los valores sean 10) => [10][10][10][10][10]
    vector<int> lista_numeros(5, 10); // lista_numeros => [10][10][10][10][10] NOTA: primer valor de parametros es el tamaño y el segundo son los valores a rellenar. 

    Inicia con una lista de valores (1 - 5)
    vector<int> lista_numeros = {1,2,3,4,5}; // lista_numeros => [1][1][1][1][1]

    vector() <== para pasarle parametros al vector
    vector = {} <== para pasarle una lista de valores al vector

    Recorrer un vector
    For: Recorrer los vectores con variables (i) para iterar entre el vector
        for(size_t i = 0; i<lista_numeros.size();i++){
        cout<<lista_numeros[i]<<" ";
    }
    For-Each: Solamente requiere 1 variable como iterador y la estructura de datos
        for (int num : lista_numeros){
        cout << num << " ";
        }

    Funciones principales de los vectores
    size(): Devuelce el número de los elementos del vector
    push_back(): Agrega un elemento al final del vector
    pop_back(): Elimina el ultimo elemento del vector
    empty(): Devuelve true si el vector ésta vacío, false en caso contrario
    clear(): Elimina TODOS los elementos del vector
    resize(): Cambia el tamaño del vector
    insert(): Insera un elemento en un posición específica
    erase(): Elimina un elemento o un rango de elementos

    Pasar vectores a funciones
    Puedes pasar un vector a una función por valor o por referencia. Usar referencias en más eficiente,
    ya que evita copiar el vector
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

// Función que pasa un vector y lo imprime
void imprimirVector(const vector<int>& vec){
    for(int num : vec){
        cout << num << endl;
    }
}

int main(){
    vector<int> lista_numeros = {1,2,3,4,5};

    for (int num : lista_numeros){
        cout << num <<endl;
        }

    cout << "-----------------------------SIZE------------------------------------"<<endl;
    cout << lista_numeros.size() <<endl;
    cout << "---------------------------PUSH BACK--------------------------------------"<<endl;

    lista_numeros.push_back(6); // Agregamos un 6 al final del vector
    for (int num : lista_numeros){
        cout << num <<endl;
        }

    cout << "-----------------------------POP BACK------------------------------------"<<endl;
    lista_numeros.pop_back();

    for (int num : lista_numeros){
        cout << num <<endl;
        }

    cout << "-----------------------------EMPTY------------------------------------"<<endl;
    if (!lista_numeros.empty()){
        cout << "El vector esta lleno"<<endl;
    }

    cout << "-----------------------------CLEAR------------------------------------"<<endl;
    lista_numeros.clear();
    for (int num : lista_numeros){
        cout << num <<endl;
        }
    if(lista_numeros.empty()){
        cout << "El vector esta vacio"<<endl;
    }

    cout << "-----------------------------RESIZE------------------------------------"<<endl;
    lista_numeros.resize(10); // Cambia el tamaño a 10 elementos
    for (int num : lista_numeros){
        cout << num <<endl;
        }

    cout << "-----------------------------INSERT------------------------------------"<<endl;
    lista_numeros.insert(lista_numeros.begin() + 2, 25); // Inserta 25 en la posición 2
    lista_numeros.insert(lista_numeros.begin() + 8, 16); // Inserta 16 en la posición 8
    lista_numeros.insert(lista_numeros.begin() + 6, 44); // Inserta 44 en la posición 6

    for (int num : lista_numeros){
        cout << num <<endl;
        }

    cout << "-----------------------------ERASE------------------------------------"<<endl;
    lista_numeros.erase(lista_numeros.begin() + 2); // Elimina el segundo elemento;

    for (int num : lista_numeros){
        cout << num <<endl;
        }

    cout << "-----------------------------MATRIZ------------------------------------"<<endl;
    // Matriz compuesta de un vector de vector (int)
    vector<vector<int>> matriz = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    cout << matriz[1][1]<<endl;

    cout << "-----------------------------FUNCION PASO POR REFENCIA------------------------------------"<<endl;

    // Paso por referencia
    vector<int> numeros = {1,2,3,4,5,6,7,8,9,10}; // VECTOR = F00AD1F <==> FUNCION = F00AD1F
    imprimirVector(numeros);
    
    // Paso por valor
    vector<int> original = {1,2,3}; // [1][2][3]
    vector<int> copia = original; // [1][2][3] Espacio de memoria es != a original
    

    cout << "-----------------------------EJEMPLO 1------------------------------------"<<endl;
    // Intercambiar dos vectores
    vector<int> a = {10,20,30};
    vector<int> b = {1,2,3};
    a.swap(b);

    for(int y : b){
        cout << y << endl;
    }

    cout << "-----------------------------EJEMPLO 2------------------------------------"<<endl;

    // Eliminar duplicados
    vector<int> c = {5,3,5,2,3,1};
    sort(c.begin(), c.end()); // Ordar el vector
    auto last = unique(c.begin(), c.end()); // Mueve duplicados al final
    c.erase(last, c.end()); // Elimina duplicados


    for(int y : c){
        cout << y << endl;
    }

    cout << "-----------------------------EJEMPLO 3------------------------------------"<<endl;
    // Invetir el orde de los elementos de un vector
    vector<int> d = {1,2,3,4,5};
    reverse(d.begin(), d.end());

    for(int y : d){
        cout << y << endl;
    }

    cout << "-----------------------------EJEMPLO 4------------------------------------"<<endl;
    // Sumar todos los elementos del vetor
    vector<int> e = {2, 4, 6, 8, 10};
    int suma = accumulate(e.begin(), e.end(), 0);

    cout << suma <<endl;

    return 0;
}

