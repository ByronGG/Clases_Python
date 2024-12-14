#include <iostream>

using namespace std;

/*
    Tipos de datos
    --------------------------------------------------------------------------------------
    char = 1 byte -> 8 bits (A - Z - 0 - 9 - # - !)
    int = 4 byte -> 32 bits (-2,150,000,000 - 2,150,000,000)
    float = 4 byte (f)-> 32 bits (-2,150,000,000.00f - 2,150,000,000.00f)
    double = 8 byte -> 64 bits (-2,150,000,000,000,000.00- 2,150,000,000,000,000.00)
    long double = 10, 12, 16 byte (L) -> (3.14159265878181895926532L)
    bool -> true, false
*/

/*
    Modificadores de tipo
    --------------------------------------------------------------------------------------
    signed: Permite valores positivos y negativos
    unsiged: Solo valores positivos
    short: Reduce el tamaño de alamacenamiento
    long: Aumenta el tamaño del almacenamiento

    unsiged int numero_positivo = 300; // Valor no puede reducir a negativo
    long long numero_long = 974975146816818318136813541313811684384867
    short numero_chiquito = 500;
*/

/*
    CONST
    --------------------------------------------------------------------------------------
    La palabara clave "const" define variables que no pueden cambiar su valor, despues de
    ser inicializadas

    cont int valor_maximo = 100; // Este entero nunca cambiara su valor 
    cont float IVA = 0.16f;
    cont float GRAVEDAD = -9.807f

    PUNTERO CONST
    --------------------------------------------------------------------------------------
    //Puntero de memoria CONST
    int a = 10, b = 20;
    int *const ptr = &a; //Dirección fija.abort
    ptr = &b; //Error.

    //Valor constatne al que apunte el puntero
    const int *ptr = &a; //El valor no puede modificarse
    *ptr = 15; //Error.
*/

/*
    Namespace
    --------------------------------------------------------------------------------------
    Un namespce es una forma de organizar y evitar conflictos entre nombres (funciones, variables
    clases, etc) en proyectos

    Declaración NAMESPACE
    namespace Math{ //Namespace esta encapsulado en este bloque
    const double PI = 3.141516;
    int add(int a, int b){
    return a + b;
        }
    int resta(int a, int b){
    return a - b;
        }
    }

    Namespace con operador de alcance (::)
    --------------------------------------------------------------------------------------
    El operador de alcance de un namespace
    int suma = Math::add(5, 5);
    int resta = Math::resta(10, 8);

    Namespace con directiva (using)
    --------------------------------------------------------------------------------------
    using namespace Math;
    int suma = add(5, 5);
    int resta = resta(10, 8);

    Namespace anonimos
    --------------------------------------------------------------------------------------
    Un namespace sin nombre se utiliza para encapsular elementos que solo deben
    ser accesibles dentro del archivo donde se declaran

    namespace {
        int valor_interno = 10;
    }
*/

namespace Geometry{
    const double PI = 3.14159;

    double areaCirculo(double radio){
        return PI * radio * radio;
    }
}

int main() {
    using namespace Geometry; // Usando el namespace Geomtry con directiva (using)
    using namespace std;
    const double radio = 5.0;

    std::cout << "El area del circulo es: "<<areaCirculo(radio) <<std::endl;

    // Tipos de datos básicos
    char letra = 'A';
    int edad = 18;
    float salario = 292.99f;
    double numero_largo = 1e10;
    long double numero_preciso_largo = 3.1415926516716381684184L;

    std::cout << "Letra es: " << letra <<", Edad: " << edad
            <<", Salario: "<< salario << ", Numero grande: " << numero_largo
            <<", numero presiso: " << numero_preciso_largo;

    return 0;
}