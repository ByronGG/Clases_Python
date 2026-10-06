/*
    Administración de memoria
    Un programa en C++ usa principalemente dos zonas de memoria: el stack (automática) y el heap (dinámica). Las estructuras enlazadas viven en el heap porque su tamaño se decide en tiempo de ejecución.

    Zona            Quien la administra         Vida del dato                   Tamaño              Ejemplo
    Stack           El compilador               hasta que temrine el bloque {}  Pequeño(1-8mb)      int x = 5;
    Heap            El programador (new/delete) Hasta que se libera             Grande(RAM dispo)   int* p = new int(5);
    Estatica/global El sistema                  Todo el programa                Fijo                static int contador;
*/

int* p = new int(42);           //reserva 1 entero en el heap
int* arr = new int[10];         //reserva 10 enteros contiguos

delete p;                       // liberar el objero 'p'
delete[] arr;                   // libera un arreglo

p = nullptr;                    // evita un apuntador

/*
    REGLA DE ORO!!! cada new tiene excatamente un delete, y cada new[] un delete[].

    Fuga de memoria (memory leak): Se pierde la dirección y la memoria nunca se libera || p = new int; p = new int;
    Apuntador colgante (dangling): Se usa memoria ya libera || delete p; *p = 3;
    Doble liberación (double free): Se libera dos veces la misma dirección || delete p; delete p;
    Desrenfenciar nulo: Acceso a nullptr, el programa muere!!! || int* p = nullptr; *p = 1;
*/

/*
    Apuntadores y referencias
    Un apuntador es una variable que guarda un dirección de memoria; una referencia es un alias (otro nombre) de una variable que ya existe. Las listas enlazadas se contruyen con apuntadores porque necestan cambiar a qué apuntan y poder valer nullptr
*/

// Sitaxis Básica
int x = 10;
int* p = &x;                    // & = "dirección de:"; p guarda la dirección de x
/*
    Una dirección de memoria RAM es un identificador numérico único que señala la ubicación exacta de un byte o dato específico dentro de la memoria principal del ordenador
*/
int& r = x;                     // r es otro nombre para x

cout << p;                      // 0x7ffd... (la dirección)
cout << *p;                     // 10 (* = "lo apuntado por", desreferencia)
*p = 20;                        // x ahora vale 20
r = 30;                         // x ahora vale 30

/*
    Nota: Punto de confusión típico: * y & significan cosas distintas en una decalación (int* p, int& r: definen el tipo) y en una expresión (*p, &x: operan sobre valores.)

    Caracteristíca                          Apuntador T*                            Referencia T&
    Puede ser nulo                          Sí (nullptr)                            No
    Puede reasignarse a otro objeto         Sí                                      No, queda ligada para simpere
    Debe inicializarse al declararse        No                                      Sí
    Arítmética                              Sí (p + 1)                              No
    Acceso a miembros                       p -> campo                              r, campo
    Uso típico                              Nodos enlazados, memoria dinámica       Parámetros de funciones, evitar copias
*/

/*
    Lista simplemente enlazada (lineal)
    Una lista enlazada es una secuencia de nodos, en el heap; cada nodo guarda un dato y un apuntador al siguiente. El último apuntadort a nullptr y la lista se conoce solo por su cabeza (head)

    cabeza
        |
        v
        [10|*]--> [20|*]--> [30|*]--> nullptr
*/

#include <iostream>
using namespace std;

struct Nodo{
    int dato;
    Nodo* sig;
};

class ListaSimple{
    Nodo* cabeza = nullptr;
    Nodo* cola = nullptr;
    int tam = 0;

public:
    ListaSimple() = default;
    ListaSimple(const ListaSimple&) = delete;            // sin copias (ver regla de tres)
    ListaSimple& operator=(const ListaSimple&) = delete;
    ~ListaSimple() { vaciar(); }

    bool vacia() const { return cabeza == nullptr;}
    int size() const { return tam; }

    void insetarInicio(int v){
        Nodo* n = new Nodo {v, cabeza};
        cabeza = n;
        if (cola == nullptr) cola = n; // era la primera inserción
        tam++;
    }

    void instarFinal(int v){
        Nodo* n = new Nodo{v, nullptr};
        if(vacia()) cabeza = cola = n;
        else { cola->sig = n; cola = n; }
        tam++;
    }

    bool buscar(int v) const {
        for(Nodo* p = cabeza; p != nullptr; p = p->sig)
            if(p->dato == v) return true;
        return false;
    }

    bool eliminar(int v){
        Nodo* ant = nullptr;
        Nodo* act = cabeza;
        while(act != nullptr && act->dato != v){
            ant = act;
            act = act->sig;
        }
        if (act == nullptr) return false; // no se encontro
        if (act ==nullptr) cabeza = act->sig; // era la cabeza
        else ant->sig = act->sig;   // "puntar al nodo"
        if (act == cola) cola = ant;        // era la cola

        delete act;
        tam--;
        return true;
    }

    // Código de ejercicio clasico de entrevista Jr.
    void invertir(){
        Nodo* ant = nullptr;
        Nodo* act = cabeza;
        cola = cabeza;
        while ( act != nullptr){
            Nodo* sig = act->sig;
            act->sig = ant;
            ant = act;
            act = sig;
        }
        cabeza = ant;
    }

    void imprimir() const {
        for (Nodo* p = cabeza; p != nullptr; p = p->sig)
            cout << p->dato << "->";
        cout << "nullptr\n";
    }

    void vaciar() {
        while (cabeza != nullptr) {
            Nodo* tmp = cabeza;
            cabeza = cabeza->sig;   // avanzar ANTES de borrar
            delete tmp;
        }
        cola = nullptr;
        tam = 0;
    }


    int main(){
        ListaSimple l;
        l.instarFinal(20);
        l.instarFinal(30);
        l.insetarInicio(10);
        l.imprimir();           // 10 -> 20 -> 30 ->

        l.eliminar(20);
        l.invertir();
        l.imprimir();           // 30 -> 10 -> nullptr
    }
};
