/*
    Recursividad
    Una funcion es recursiva cuando se llama a sí misma. Siempre necesita dos partes:
        1. Caso base: la condición que detiene la recursión.
        2. Caso recursivo: la llamada que reduce el problema hacia el caso base.
*/

int factorial(int n){
    if (n <= 1) return 1; // Caso base
    return n * factorial (n - 1); // Caso recursivo
}

/* 
    ¿Qué pasa en memoria? 
    Cada llamada crea un marco en la pila(stack frame). Así se ve el factorial(4)

    factorial(4) -> 4 * factirial(3)
                            -> 3 * factorial(2)
                                        -> 2 * factorial(1)
                                                    -> 1        (caso base, empieza a regresar)
                    = 4 * 3 * 2 * 1 = 24
    Si no hay caso base, o nunca se alcanza, se produce un stack overflow
*/

#include <iostream>
using namespace std;

typedef unsigned long long ull;

// Imprime la secuencia de Collatz desde n hasta llegar a 1.
// Devuelve el número de pasos necesarios. Actualiza 'maximo' con el valor más alto alcanzado.
int collatz(ull n, ull &maximo) {
    cout << n;
    if (n > maximo) maximo = n;

    // Caso base: al llegar a 1 la secuencia termina
    if (n == 1) {
        cout << endl;
        return 0;
    }

    cout << " -> ";

    // Caso recursivo:
    //  - si n es par   -> n / 2
    //  - si n es impar -> 3n + 1
    if (n % 2 == 0)
        return 1 + collatz(n / 2, maximo);
    else
        return 1 + collatz(3 * n + 1, maximo);
}

int main() {
    ull n;
    cout << "=== Conjetura de Collatz (3n + 1) ===" << endl;
    cout << "Ingresa un numero entero positivo: ";
    cin >> n;

    if (!cin || n == 0) {
        cout << "Error: debes ingresar un entero mayor que 0." << endl;
        return 1;
    }

    ull maximo = 0;
    cout << "\nSecuencia:\n";
    int pasos = collatz(n, maximo);

    cout << "\nPasos para llegar a 1: " << pasos << endl;
    cout << "Valor maximo alcanzado: " << maximo << endl;

    return 0;
}