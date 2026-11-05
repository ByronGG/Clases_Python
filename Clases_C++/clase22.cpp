/*
    La memoria dinámica permite decidir en tiempo de ejecución cuánta memoria usar; el puntero es la única forma de llegar a ella, porque los bloques del heap no tienen nombre. Esta sección amplía la de la pestaña principal con los casos que más aparecen en exámenes y en código real.

    Modelo mental: dirección, valor y lo apuntado
    Enseña a dibujar cada variable como una caja con dirección (dónde vive) y valor (qué contiene). Un puntero es una caja cuyo valor es la dirección de otra caja.

    int x = 7;
    int* p = &x;
    int** pp = &p;

    Dirección       Nombre      Valor       Zona
    0x1000          x           7           stack
    0x1008          p           0x1000      stack
    0x1010          pp          0x1008      stack

    *p == 7     (sigo 1 flecha)
    **pp == 7   (sigo 2 flechas)
    *pp ==  0x1000 (el valor de p)

    Dirección RAM = 0x1110 => arreglo = [0,1,2,3,4,5];
    Puntar al arreglo = arr* dirección_de_mi_arreglo = &arreglo;
*/

#include <iostream>
#include <algorithm> //std:copy
using namespace std;

class ArregloDinamico{
    int* datos = nullptr;
    int tam = 0;        // elementos usados
    int cap = 0;        // espacios reservados

    void crecer(){
        int nuevaCap = (cap == 0) ? 1 : cap * 2;        // duplicar => push 0(1)
        int* nuevo = new int[nuevaCap];
        copy(datos, datos + tam, nuevo);    // copias lo viejo
        delete[] datos;                     // liberar lo viejo
        datos = nuevo;
        cap = nuevaCap;
    }
/*
    arreglo_normal = [0,1,2,3,4,5]
    arreglo_dinamico = [] # estado 1
    arreglo_dinamico = [5] # estado 2
    arreglo_dinamico = [5,x] # estado 1
    arreglo_dinamico = [5,5] # estado 1
    arreglo_dinamico = [5,4,x] # estado 1
    arreglo_dinamico = [5,4,4] # estado 1
    arreglo_dinamico = [5,4,10] # estado 1
    arreglo_dinamico = [5,4,10,x] # estado 1
*/

public:
    ArregloDinamico() = default;
    ArregloDinamico(const ArregloDinamico&) = delete;
    ArregloDinamico& operator=(const ArregloDinamico&) = delete;
    ~ArregloDinamico() { delete[] datos; }

    void push_back(int v){
        if (tam == cap) crecer();
        datos[tam++] = v;
    }
    int& operator[](int i) {return datos[i]; }
    int size() const { return tam; }
    int capacity() const { return cap; }
};

int main(){
    ArregloDinamico a;
    for (int i = 0; i < 10; i++){
        a.push_back(i);
        cout << "tam=" << a.size() << " cap=" <<a.capacity() << "\n";
    } 
}

/*
    OPERACIONES CRÍTICAS EN LISTAS ENLAZADAS!!!

    Una operación es "crítica" cuando un solo enlace mal actualizado pierde nodos, deja fugas o rompe la lista. Todas comparten un principio: primero se conectan los enlaces nuevos y al final se rompen o liberan los viejos.
*/

#include <iostream>
using namespace std;

struct Nodo
{
    int dato;
    Nodo* sig;
};

void imprimir(Nodo* c){
    for(; c; c = c->sig) cout << c->dato << " -> ";
    cout << "nullptr\n";
}

// 1 Insertar despúes de un nodo : Primero conceto el nodo nuevo con el resto de la lista y después enlázalo desde p:
void insertarDespues(Nodo* p, int valor){
    if(!p) return;
    Nodo* nuevo = new Nodo{ valor, p->sig}; //1. Conecta el enlace nuevo
    p->sig = nuevo;                         //2. Reemplaza el enlace viejo

    /*
    Si invierte el orden, pierdes el acceso al resto de la lista

    p->sig = nuevo;             // Se pierde la dirección del esto de la lista
    nuevo->sig = p->sig;        // nuevo apunta a sí mismo: ciclo y fuga de memoria
    */
}

/*
    COMPLEJIDAD ALGORÍTMICA

    La complejidad algorítmica mide cómo crece el trabajo (tiempo) o la memoria (espacio) de un algoritmo cuando crece el tamaño de la entrada n. No mide segundos: los segundos dependen de la computadora, el compilador y la carga del sistema; el crecimiento no.

    Analogía: buscar un nombre en una lista desordenada de 1,000 personas vs. en un directorio alfabético. En la primera, duplicar la lista duplica el trabajo (lineal); en la segunda, duplicarla agrega apenas un paso más (logarítmico).
*/

int suma(int arr[], int n) {
    int s = 0;                    // 1 vez
    for (int i = 0; i < n; i++)   // la comparación se hace n + 1 veces
        s += arr[i];              // n veces
    return s;                     // 1 vez
}
// T(n) ≈ 2n + 3  ->  se queda solo el término que domina  ->  O(n)

/*
    Definición formal del Big O:
    
    Reglas para calcularla sin contar todo
    1. Se eliminan constantes: O(3n) = O(n); O(500) = O(1).
    2. Se queda el término dominante: O(n² + 5n + 10) = O(n²).
    3. Bloques en secuencia se suman: un ciclo O(n) seguido de otro O(n²) da O(n + n²) = O(n²).
    4. Ciclos anidados se multiplican: un ciclo de n dentro de otro de n da O(n²).
    5. Condicionales: se toma la rama más cara (para el peor caso).
    6. Dividir el problema a la mitad en cada paso da log n: búsqueda binaria, árboles balanceados.
    7. Entradas distintas, variables distintas: recorrer un arreglo de tamaño n y otro de tamaño m es O(n + m), no O(n).
*/

// (a) O(1): no depende de n (Constante)
int primero(int arr[]) { return arr[0]; }

// (b) O(n): un recorrido (Lineal)
bool contiene(Nodo* c, int v) {
    for (; c; c = c->sig) if (c->dato == v) return true;
    return false;
}

// (c) O(n²): ciclos anidados, cada uno hasta n (Cuadrática)
void pares(int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cout << i << "," << j << "\n";
}

// (d) También O(n²): j empieza en i, pero n + (n-1) + ... + 1 = n(n+1)/2 (Cuadrática)
void paresSinRepetir(int n) {
    for (int i = 0; i < n; i++)
        for (int j = i; j < n; j++)
            cout << i << "," << j << "\n";
}

// (e) O(log n): i se duplica en cada vuelta (Logatímica)
void potencias(int n) {
    for (int i = 1; i < n; i *= 2) cout << i << " ";
}

// (f) O(n log n): ciclo de n con un ciclo logarítmico dentro (Linal-Logaritmica)
void mezcla(int n) {
    for (int i = 0; i < n; i++)
        for (int j = 1; j < n; j *= 2) { /* O(1) */ }
}

// (g) O(log n): búsqueda binaria en arreglo ORDENADO (Linal-Logaritmica)
int binaria(int arr[], int n, int v) {
    int izq = 0, der = n - 1;
    while (izq <= der) {
        int mid = izq + (der - izq) / 2;   // evita desbordamiento de (izq + der)
        if (arr[mid] == v) return mid;
        if (arr[mid] < v) izq = mid + 1; else der = mid - 1;
    }
    return -1;
}

// (h) O(2ⁿ): cada llamada genera dos llamadas más (Exponecial)
long long fib(int n) {
    return n < 2 ? n : fib(n - 1) + fib(n - 2);
}
// Con memoización (guardar resultados ya calculados) baja a O(n).