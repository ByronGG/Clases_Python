/*
    Plantillas (Templates)
    Una plantilla permite escribir código genérico, que funciona con cualquier tipo de dato.
    El compilador genera una versión concreta para cada tipo que uses. A este proceso se le
    llama instanciación y ocurre en tiempo de compilación. Existen dos tipos de plantillas:
        * Plantilla de función
        * Plantilla de clase
*/

#include <iostream>
#include <string>
#include <utility>

// Plantilla de función
template <typename T>
T maximo(T a, T b) {
    return (a > b) ? a : b;
}

// Plantilla de clase
template <typename C>
class Caja {
    C valor;
public:
    Caja(C v) : valor(v) {}
    C obtener() const { return valor; }
};

// Especialización: comportamiento distinto para un tipo en particular
template <>
class Caja<bool> {
    // implementación especial para valores booleanos
};

// Plantillas con arreglos (útil para búsqueda y ordenamiento)
template <typename A>
void imprimirArreglo(const A arr[], int n) {
    for (int i = 0; i < n; i++)
        std::cout << arr[i] << " ";
    std::cout << "\n";
}

template <typename A>
void burbuja(A arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    // Plantilla de función
    std::cout << maximo(3, 7) << "\n";          // T = int (deducido)
    std::cout << maximo(2.5, 1.2) << "\n";      // T = double
    std::cout << maximo<char>('a', 'z') << "\n"; // T = char (explícito)

    // Plantilla de clase
    Caja<int> c1(10);
    Caja<std::string> c2("hola");
    std::cout << c1.obtener() << " " << c2.obtener() << "\n";

    // Plantillas con arreglos
    int lista[] = {5, 2, 9, 1};
    std::string nombres[] = {"Arturo", "Luis", "Ana", "Carlos"};

    burbuja(lista, 4);
    burbuja(nombres, 4);

    imprimirArreglo(lista, 4);    // 1 2 5 9
    imprimirArreglo(nombres, 4);  // Ana Arturo Carlos Luis
}