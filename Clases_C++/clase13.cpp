/* Iteradores en Vectores
    ------------------------------------------------------------------------------------------------
    Iteradores en vectores y cómo implementar getters y setters para acceder y modificar los elementos de un vector.
    Los iteradores son objetos que permiten recorrer los elementos de un contenedor (como un vector) de manera eficiente. En el caso de los vectores, los iteradores se comportan como punteros a los elementos del vector.

    Tipos de iteradores:
        - begin(): Devolver un iterador primer elemento del vecto
        - end(): Devolver un iterador al "final" del vector
        - rbegin(): Devolver un iterador inversor "al último elemento" 
        - rend(): Devolver un iterador al "inicio" del vector (posición antes del primer elemento)

    Los getters y setters son métodos que permiten acceder (get) y modificar (set) los elementos de un vector de manera controlada. Esto es especialmente útil cuando trabajas con clases y quieres encapsular el acceso a los datos.

    Clase MiVector:
        * Encapsulamiento: vector de enteros(datos)
        * Proporciona métodos para acceder (get), modificar (set), agregar (agregar), imprimir(imprimir), y buscar(buscar) elementos CRUD
    Uso de iteradores:
        * En el método imprimr, se usa un iterador apra recorrer el vector
        * En el método buscar, se usan iteradores para buscar un valor especifico
    Getter y Setter:
        * get permitir acceder a un elemento en un posición especifica
        * set permitir modificar un elelmento en la posición especifica
*/

#include <iostream>
#include <vector>
using namespace std;


class MiVector{
private:
    vector<int> datos; // Vector privado

public:
    // Getter: Devuelve el valor en una posicioón espcifica
    int get(int indice) const{
        if(indice >= 0 && indice < datos.size()){
            return datos[indice];
        } else {
            throw out_of_range("Indice fuera de rango");
        }
    }

    // Setter: Modifica el valor en una posición especifica
    void set(int indice, int valor){
        if(indice >= 0 && indice < datos.size()){
            datos[indice] = valor; // [10] [20] [70] [40] [50]
        } else{
            throw out_of_range("Indice fuera de rango");
        }
    }

    // Método para agregar un elemento al final del vector
    void agregar(int valor){
        datos.push_back(valor); // Invocación de método build-in 
    }

    // Método para obtener el tamaño del vector
    size_t tamano() const{
        return datos.size();
    }

    // Método para imprimir el vector
    void imprimir() const{
        for(int num : datos){
            cout << num << " - ";
        }
        cout << endl;
    }

    // Buscar un elemento usando iteradores
    bool buscar(int valor) const{
        for(auto it = datos.begin(); it != datos.end(); it++){ // [begin][][][][][][][][end]
            if(*it == valor){ // [][][][][][*it][][][]
                return true; // [/][/][/][/][/][*][][][] => TRUE
            }
        }
        return false; // [/][/][/][/][/][/][/][/][/] => FALSE
    }
};


int main() {
    MiVector vec; // <- Crear un objeto es llamar a la clase (MiVector) y ponerle nombre (vec)

    // Agregar datos al vector
    vec.agregar(10);
    vec.agregar(20);
    vec.agregar(30);
    vec.agregar(40); // -> 100
    vec.agregar(50);
    vec.agregar(60);
    vec.agregar(70);
    
    // Imprimir el vector
    cout << "Vector inicial: ";
    vec.imprimir();

    // Usar el setter para modificar un elemento
    vec.set(0, 200);
    cout << "Vector despues de modificar: ";
    vec.imprimir();

    // Usar el getter para obtener un elemento
    cout << "Elemento en la posicion ??: " << vec.get(5) << endl;

    // Buscar un elemento
    int valor = 80; // variable con el valor a buscar (valor)
    if(vec.buscar(valor)){
        cout << "El valor: " << valor << " esta en el vector: " <<endl; // TRUE
    } else {
        cout << "El valor: " << valor << " no esta en el vector: " <<endl; // FALSE
    }

    return  0;
}


    // vector<int> numeros = {10, 20, 30, 40, 50};

    // // Recorrer el vector con iteradpres
    // cout << "Elementos del vector: ";
    // for(auto it = numeros.begin(); it != numeros.end(); it++){
    //     cout << *it << " "; // *it accede al valor del elemento
    // }
    // cout << endl;

    // // Recorrer el vector en orden inverso
    // cout << "Elemenetos en orden inverso: ";
    // for(auto it = numeros.rbegin(); it != numeros.rend(); it++){
    //     cout << *it << " ";
    // }
    // cout << endl;


