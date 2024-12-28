/* VECTORES
    --------------------------------------------------------------------------------------
    Un vector es un contenedor dinámico en C++ que puede cambiar el tamaño automáticamente cuando se agregan o elimina elementos.
    Los elementos del vector están almacenados de amenra contigua en memoria, lo que permite acceso aleateorio
    Se encuentra ene le encabezado <vector>

    - Crecimiento dinámico: Adiferencia de los arreglos estáticos, los vectores pueden cambiar de tamaño.
    - Acceso aleterio: Se puede acceder los elementos usando índices.
    - Método útilines: push_back, pop_back.
    - Plantillas: Pueden almacenar cualquier tidpo de datos, incluso objetos.

    - Modos de crear un vector
    std::vector<int> vec;                   // Vector vacío
    std::vector<int> vec(10);               // Vector con 10 elementos (inicializados en 0)
    std::vector<int> vec(5, 100);           // Vector con 5 elementos (inicializados en 100)
    std::vector<int> vec{1,2,3,4,5};        // Vector inicizalicado como lista

    - Métodos de los vectores 
    push_back(value): Agrega un elementos al final.
    pop_back(): Elimina el último elemento.
    vec[i] o vec.at(i): Accede a los elementos de la posicion i
    size(): Retorna el número de elementos
    capacity(): Retorna la capacidad del vector
    resize(n): Cambia el tamaño del vector
    clear(): Borra TODOS los elementos
    empty(): Retorna true si el vector esta vacio
    front(): Retorna el primer elemento
    back(): Retorna el ultimo elemento
    end(): Retorna un iterador al final
    insert(pos, val): Inserta un elemento (val) en la posicion (pos) 
    erase(pos): Elimina el elemento en la posicion (pos) especificada
    swap(other): Intercambia el contenido de dos vectores (other)
*/

/* MAP
    --------------------------------------------------------------------------------------
    Un map es un contenedor que almacena elementos en pares (clave-valor). Cada vlace es única y se asocia
    asocia a exactamente un valor.

    - Las vlaces están ordenadas automáticamente usando un criterio(por defecto, orden ascendente)
    - Los elementos del map están implementados como un árbol binario balanceado (normalmente un árbol rojo-negro)
    Se ecuentra en el encabezado <map>

    Características principales
    - Asociación clave-valor: Cada clave única ésta asociada a un valor.
    - Ordenado: Los elementos se almacenan en orden creciente (puedes usar un criterio personalizado)
    - Eficiente: Inserciones, búsquedas y eliminación tiene complejidad O(log n)
    - Clave única: No puede haber claces duplicadas (usando multimap si es necesario)

    Métodos principales del map
    - Crear un map
    std::map<int, std::string> myMap;                                           // Mapa vacío
    std::map<int, std::string> myMap{{1, "A"}, {2, "B"}, {3, "C"}};             // Mapa incializado

    - Insertar elementos usando []:
    myMap[4] = "D";

    - Insertar elementos usando insert:
    myMap.insert({5, "E"});

    - Acceso a elementos usando []:
    std::cout<<myMap[1];            // Accede al VALOR asociado a clave 1

    - Acceso usando at(lanza excepción si la clave no existe):
    std::cout<<myMap.at(1);

    - Tamaño y vaciado
    size(): Devuelve el numero de elementos
    empty(): Retorna treu si está vacío
    std::cout << "Tamaño: " << myMap.size();
    std::cout << "¿Vacío? " << (myMap.empty() ? "Sí" : "No");

    - Buscar elementos
    find(key): Retorna un iterador al elemento con la clave dada, o end() si no existe
    auto it = myMap.find(2);
    if (it != myMap.end()) {
        std::cout << "Clave 2 encontrada con valor: " << it->second;
    } else {
        std::cout << "Clave 2 no encontrada";
    }

*/


#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    std::vector<int> vec_1; // Crear un vector de enteros vacío

    // Agregar elementos
    vec_1.push_back(10); // Índice 0
    vec_1.push_back(20); // Índice 1
    vec_1.push_back(30); // Índice 2
    vec_1.push_back(40); // Índice 3
    vec_1.push_back(50); // Índice 4
    vec_1.push_back(60); // Índice 5
    vec_1.push_back(70); // Índice 6

    // Acceso por índice.
    std::cout <<"Elemento en la posocion 1: "<<vec_1[3] <<std::endl;

    // Imprimir todos los elementos.
    for(int i = 0; i < vec_1.size(); i++){
        std::cout<<vec_1[i]<<std::endl;
    }


    cout << "-------------------VECTOR PUSH-BACK-CLEAR-FRONT-BACK------------------------------" <<endl;

    // Crear un vector y agregar elementos
    std::vector<int> vec_2 = {10, 20, 30, 40, 50};

    // Agregar un elemento al final
    vec_2.push_back(60); // {10,20,30,40,50,60}

    // Eleminar el último elemento.
    vec_2.pop_back(); // {10,20,30,40,50}

    // Acceder al primer y último elemento
    std::cout<<"Primer elemento: "<<vec_2.front()<<std::endl;
    std::cout<<"Ultimo elemento: "<<vec_2.back()<<std::endl;

    // Imprimir elelemto usando for
    std::cout<<"Elementos del vector: ";
    for(int value: vec_2){
        std::cout<<value<<" ";
    }

    // Eliminar todos los elementos
    vec_2.clear();
    std::cout<<"\nTamanio despues del clear: "<<vec_2.size()<<std::endl;

    cout << "---------------------METODOS VECTORES----------------------------" <<endl;

    // Crear un vector vacio
    std::vector<int> vec;
    
    //1. push_back(value)
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);
    vec.push_back(40);
    std::cout<<"Despues del push_back: ";
    for (int v: vec) std::cout<<v<<" ";
    std::cout<<std::endl;

    //2. pop_back()
    vec.pop_back(); // Elimima el ultimo elemento
    std::cout<<"Despues del pop_back: ";
    for(int v: vec) std::cout<<v<<" ";
    std::cout<<std::endl;

    //3. size()
    std::cout <<"Tamanio actual (size): "<<vec.size()<<std::endl;

    //4. capacity()
    std::cout<<"Capacidad actual (capacity): "<<vec.capacity()<<std::endl;

    //5. resize(n)
    vec.resize(5, 100); // Cambiar el tamaño de 5 y llena con 100 nuevos elementos
    std::cout<<"Despues del resize(5, 100): ";
    for(int v: vec)std::cout<<v<<" ";
    std::cout<<std::endl;

    //6. empty()
    std::cout<<"El vector esta vacio? (empty): "<<(vec.empty() ? "Si" : "No")<<std::endl;

    //7. clear()
    vec.clear(); // Borrar todos los elementos
    std::cout << "Despues del clear, tamanio: "<<vec.size()<<std::endl;

    // Volver a llenar porque le pasamos el clear xd
    vec = {1,2,3,4,5,6,7,8,9};

    //8. at(index)
    std::cout<<"Elemento en la posicion 4 (at): "<<vec.at(4)<<std::endl;

    //9. front()
    std::cout<<"Primer elemento (front): "<<vec.front()<<std::endl;

    //10. back()
    std::cout<<"Ultimo elemento (back): "<<vec.back()<<std::endl;

    //11. begin() y end()
    std::cout <<"Elementos usando iteradores (begin y end): ";
    for(auto it = vec.begin(); it != vec.end(); ++it){
        std::cout<< *it<<" ";
    }
    std::cout<<std::endl;

    //12. insert(pos, value)
    vec.insert(vec.begin() + 2, 42); //Inserta 42 en la posicion 2.
    std::cout<<"Despues del insert(2, 42): ";
    for(int v: vec) std::cout<<v<<" ";
    std::cout<<std::endl;

    //13. erase(pos)
    vec.erase(vec.begin() + 2); // Elimina el elemento en la poscion 2
    std::cout<<"Depues del erase(2): ";
    for(int v: vec) std::cout<<v<<" ";
    std::cout<<std::endl;

    //14. spaw(other)
    std::vector<int> other = {100, 200, 300};
    vec.swap(other);
    std::cout<<"Despues de sawp con otro vector (vec): ";
    for(int v: vec) std::cout<<v<<" ";
    std::cout<<std::endl;
    std::cout<<"Despues del sawp con otro vector (other): ";
    for(int v: other)std::cout<<v<<" ";
    std::cout<<std::endl;


    cout << "--------------------MAP-----------------------------" <<endl;

    std::map<int, std::string> mMap;

    // Insertar pares clase-valor
    mMap[1] = "Uno";
    mMap[2] = "Dos";
    mMap[3] = "Tres";
    mMap[4] = "Cuatro";
    mMap[5] = "Cinco";

    // Acceder a un valor usando su clave
    std::cout <<"Clave 2 tiene el valor: "<<mMap[2]<<std::endl;

    // Iterar sobre el mapa
    for(const auto& pair: mMap){
        std::cout<<"Clase: "<<pair.first<<", Valor: "<<pair.second<<std::endl;
    }

    cout << "--------------------METODOS MAP-----------------------------" <<endl;

    // Crear un mapa e inicilizalo.
    std::map<int, std::string> myMap{{1, "A"}, {2, "B"}, {3, "C"}}; 

    // Insertar elementos.
    myMap[4] = "D";
    myMap.insert({5, "E"});

    // Mostrar el tamaño
    std::cout<<"Tamanio: "<<myMap.size()<<std::endl;

    // Acceso a elementos
    std::cout<<"Contenido del mapa: "<<std::endl;
    for(const auto& pair: myMap){
        std::cout<<"Clase: "<<pair.first<<", Valor: "<<pair.second<<std::endl;
    }

    // Buscar un elemento.
    auto it = myMap.find(4);
    if (it != myMap.end()) {
        std::cout << "Elemento encontrado - Clave: " << it->first << ", Valor: " << it->second << std::endl;
    } else {
        std::cout << "Clave no encontrada" << std::endl;
    }

    // Eliminar un elemento
    myMap.erase(3);
    std::cout<<"Depues de eliminar la clave 3: "<<std::endl;

    for(const auto& pair: myMap){
        std::cout<<"Clase: "<<pair.first<<", Valor: "<<pair.second<<std::endl;
    }

    // Limpiar el mapa
    myMap.clear();
    std::cout<<"Depues de limpiar, tamanio: "<<myMap.size()<<std::endl;

    return 0;
}