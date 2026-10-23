/*
    Una fila es una estructura FIFO se inserta por el final y se saca por el frente.

        sale <- frente                 final <- entra
          [10] [20] [30] [40]
        dequeue()                      enqueue(50)
    
    El problema de la fila con arreglo simple
    Si se usa un arreglo y se avanza frente con cada dequeue, el espacio del inicio queda desperdiciado y la fila "se llena" aunque tenga huecos. Recorrer todos los elementos a la izquierda en cada dequeue lo arregla, pero cuesta O(n). La solución es la fila circular: los índices dan la vuelta con el operador módulo.

    CAP = 5, frente = 3, final = 1, cantidad = 3
    indice:  0    1    2    3    4
       [40] [  ] [  ] [20] [30]
              ^         ^
            final     frente     siguiente posición = (i + 1) % CAP
*/

#include <iostream>
#include <stdexcept>
using namespace std;

class FilaCircular{
    static const int CAP = 5;
    int datos[CAP];
    int frente = 0; // índice del primer elemento
    int final_ = 0; // índice donde se insertará del siguiente
    int cantidad = 0; // distingue "vacia" de "llena"

public:
    bool vacia() const {return cantidad == 0;}
    bool llena() const {return cantidad == CAP;}

    void enqueue(int v){
        if(llena()) throw overflow_error("Fila llena");
        datos[final_] = v;
        final_ = (final_ + 1 ) % CAP; // da la vuelta
        // final_ = (final_ + 1) % CAP == frente;
        cantidad++;
    }

    int dequeue(){
        if(vacia()) throw underflow_error("Fila vacia");
        int v = datos[frente];
        frente = (frente + 1) % CAP;
        cantidad--;
        return v;
    }

    int front() const{
        if(vacia()) throw underflow_error("Fila vacia");
        return datos[frente];
    }
};


/*
    En una fila priorizada cada elemento tiene una prioridad y siempre sale primero el de mayor prioridad, sin importar cuándo llegó. A igual prioridad, normalmente se respeta el orden de llegada (FIFO).

    Analogía: la sala de urgencias de un hospital; un paciente grave pasa antes que uno con un resfriado aunque haya llegado después. Aplicaciones: planificación de procesos por prioridad, algoritmo de Dijkstra, codificación de Huffman, simulación de eventos y atención de tickets por severidad.

    Implementación              Insertar                    Sacar de el mayor prioridad
    Lista sin ordenar           O(1)                        O(n)
    Lista ordenada              O(n)                        O(1)
    Heap binario(montículo)     O(log n)                    O(log n)

    Versión 1: con lista ordenada por prioridad
    Es la versión natural después de la lista ordenada y la más fácil de explicar. El nodo de mayor prioridad siempre es la cabeza; el > estricto hace que a igual prioridad el nuevo quede detrás (FIFO).
*/

#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

class FilaPrioridad{
    struct Nodo 
    {
        string dato; int prioridad; Nodo* sig;
    };
    Nodo* frente = nullptr;

public:
    FilaPrioridad() = default;
    FilaPrioridad(const FilaPrioridad&) = default;
    FilaPrioridad& operator=(const FilaPrioridad&) = delete;
    ~FilaPrioridad() { while (!vacia()) dequeue(); }

    bool vacia() const { return frente == nullptr; }

    void enqueue(const string& d, int prio){ // mayor número = más urgente
        Nodo* n = new Nodo{d, prio, nullptr};
        if(vacia() || prio > frente->prioridad){
            n->sig = frente;
            frente = n;
            return;
        }
        Nodo* p = frente;
        while( p->sig != nullptr && p->sig->prioridad >= prio)
            p = p->sig;
            n->sig = p->sig;
            p->sig = n;
    }

    string dequeue(){
        if(vacia()) throw underflow_error("Fila vacia");
        Nodo* t = frente;
        string d = t->dato;
        frente = frente->sig;
        delete t;
        return d;
    }
};

int main(){
    FilaPrioridad urg;
    urg.enqueue("Resfriado", 1);
    urg.enqueue("Fractura", 3);
    urg.enqueue("Infarto", 5);
    urg.enqueue("Esguince", 3);
    while(!urg.vacia()) cout << urg.dequeue() << "\n";
    // Infarto, Fractura, Esguince, Resfriado
}

/*
    Versión 2: heap binario (concepto)
    Un max-heap es un árbol binario completo guardado en un arreglo, donde cada padre es mayor o igual que sus hijos. Aunque es un árbol, se almacena de forma lineal, así que encaja como cierre del tema:
    • Hijos del índice i: 2*i + 1 y 2*i + 2; padre: (i - 1) / 2.
    • Insertar: se coloca al final y "sube" intercambiándose con su padre mientras sea mayor (O(log n)).
    • Sacar: se toma la raíz [0], se pone el último en su lugar y "baja" intercambiándose con el hijo mayor (O(log n)).
*/

#include <vector>
#include <utility>

class MaxHeap{
    vector<int> h;

    void subir(int i){
        while(i > 0 && h[(i - 1) / 2] < h[i]){
            swap(h[i], h[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    void bajar(int i){
        int n = h.size();
        while(true){
            int mayor = i, izq = 2 * i + 1, der = 2 * i + 2;
            if(izq < n && h[izq] > h[mayor]) {
                mayor = izq;
            }
            if(der < n && h[der] > h[mayor]) {
                mayor = der;
            }
            if(mayor == i) {
                break;
            }
            swap(h[i], h[mayor]);
            i = mayor;
        }
    }
public:
    bool vacia() const { return h.empty(); }
    void push(int v) { h.push_back(v); subir(h.size() - 1); }
    int top() const { return h.at(0); }
    void pop(){
        h[0] = h.back();
        h.pop_back();
        if(!h.empty()) bajar(0);
    }
};