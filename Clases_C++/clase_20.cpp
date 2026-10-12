/*
    LISTA ORDENADA
    Una lista ordenada mantiene sus elementos siempre en orden (ascendente en este ejemplo): no hay "insertar al inicio" ni "al final", solo insertar en su lugar. Ordenar al insertar cuesta O(n) por inserción, pero a cambio la lista nunca necesita ordenarse completa.
    
    * Analogía: acomodar cartas en la mano; cada carta nueva se desliza hasta su posición correcta.
    * Ventaja en búsquedas: la búsqueda puede detenerse en cuanto encuentra un valor mayor al buscado. Sigue siendo O(n) en el peor caso (en una lista enlazada no se puede hacer búsqueda binaria porque no hay acceso por índice), pero en promedio recorre menos.
*/

#include <iostream>
using namespace std;

struct Nodo{
    int valor;
    Nodo* sig;
};

class ListaOrdenada{
    Nodo* cabeza = nullptr;

public:
    ListaOrdenada() = default;
    ListaOrdenada(const ListaOrdenada&) = delete;
    ListaOrdenada& operator = (const ListaOrdenada&) = delete;
    ~ListaOrdenada(){
        while(cabeza) { Nodo* t = cabeza; cabeza = cabeza->sig; delete t; }
    }

    void insetar(int v){
        // Caso 1: lista vacía o v va antes de la cebeza
        if(cabeza == nullptr || v < cabeza->valor){
            cabeza = new Nodo{v, cabeza};
            return;
        }
        // Caso 2: buscar el último nodo cuyo dato sea <= v
        Nodo* p = cabeza;
        while(p->sig != nullptr && p->sig->valor <= v)
            p = p->sig;
        p->sig = new Nodo{v, p->sig};       
    }

    bool buscar(int v) const{
        Nodo* p = cabeza;
        while(p != nullptr && p->valor < v) // Se detiene al pasarse
            p = p->sig;
        return p != nullptr && p->valor == v;
    }

    bool eliminar(int v){
        Nodo* ant = nullptr;
        Nodo* act = cabeza;
        while(act != nullptr && act->valor < v){
            ant = act; act = act->sig;
        }
        if(act == nullptr || act->valor != v) return false;
        (ant ? ant->sig : cabeza) = act->sig;
        delete act;
        return true; 
    }

    // Ele recorrido siempre sale en orden, sin ordenar nada
    void imprimr() const{
        for (Nodo* p = cabeza; p; p = p->sig) cout << p->valor << " ";
        cout << "\n";
    }
};

int main(){
    ListaOrdenada o;
    for( int v : {40, 10, 30, 20, 10}) o.insetar(v);
    o.imprimr();
    cout << o.buscar(25) << "\n";
    o.eliminar(30);
    o.imprimr();
}


/*
    Una pila es una estructura LIFO (Last In, First Out): solo se inserta y se saca por un extremo llamado tope. Todas sus operaciones básicas son O(1).

    push(30)      pop() -> 30
      |              ^
      v              |
    +----+         +----+
    | 30 | <- tope | 20 | <- tope
    | 20 |         | 10 |
    | 10 |         +----+
    +----+

    Analogía: una pila de platos o de libros; solo se toma el de arriba. 
    Aplicaciones: la pila de llamadas a funciones (recursión), deshacer (Ctrl+Z), botón "atrás", validar paréntesis balanceados, evaluar expresiones en notación postfija y búsqueda en profundidad (DFS).
*/

#include <iostream>
#include <stdexcept>
using namespace std;

class PilaArreglo{
    static const int CAP = 100;
    int datos[CAP];
    int tope = -1; // -1 significa vacia

public:
    bool vacia() const { return tope == -1;}
    bool llena() const { return tope == CAP - 1;}

    void push(int v){
        if (llena()) throw overflow_error("Pilla llena");
        datos[++tope] = v;
    }
    int pop(){
        if(vacia()) throw underflow_error("Pilla vacia");
        return datos[--tope];
    }
    int peek() const{
        if(vacia()) throw underflow_error("Pilla vacia");
        return datos[tope];
    }
};

/*
    Imprimetación con Nodos
    El tope es la cabeza de una lista simple: push = insertar al inicio y pop = eliminar al incio. No tiene límite de tamaño.
*/

class PilaNodos{
    struct Nodo { int dato; Nodo* sig; };
    Nodo* tope = nullptr;
    int tam = 0;


public:
    PilaNodos() = default;
    PilaNodos(const PilaNodos&) = delete;
    PilaNodos& operator=(const PilaNodos&) = delete;
    ~PilaNodos() {while (!vacia()) pop(); }

    bool vacia() const { return tope == nullptr; }
    int size() const { return tam; }

    void push(int v) { tope = new Nodo{v, tope}; tam++; }

    int pop(){
        if(vacia()) throw underflow_error("Pila vacia");
        Nodo* t = tope; // Limite ejemplo 30
        int v = t->dato; // Pasamo valor al tope
        tope = tope->sig; // El tope apunta al siguiente de la pila
        delete t; // Borramos el tope
        tam--;  // Reducir el tamaño al tope
        return v; // Y regresamos el ultimo valor
    }

    int peek() const{
        if(vacia()) throw underflow_error("Pila vacia");
        return tope->dato;
    }
};

/* 
    NOTA: En la STL:std::stack
    #include <stack>
    stack<int> s;
    s.push(1); s.push(2);
    cout << s.top();          // 2
    s.pop();                 // ojo!!!! pop() NO REGRESA EL VALOR, ES VOID
    
    std::stack es un adaptador: porque dentro usa un std::deque (o el contenedor que se le indique) y solo expone las operaciones de la pila!!!!
*/

// TAREA: CON LA LIBRERIA STACK: PARÉNTESIS BALANCEADOS!!!
#include <stack>
#include <string>


/*
    Ejemplo evaluar "3 4 + 2 *" (postfija). Cada número se apila; al leer un operador se sacan dos, se opera y se aplica el retultado. Resultado es: 14.

    Pistas!!!
        VER VIDEO SOBRE: JERARQUIA DE OPERACIONES, BALANCEO DE PARENTESIS, ORDEN PREFIJO, POSTFIJO E INFIJO
*/