#include <iostream>
#include <string>

/*
    Operadores aritméticos básicos
    --------------------------------------------------------------------------------------
    Operador    Descripción         Ejemplo      Resultado
        +          Sumar             5 + 5          10
        -          Resta             5 - 3           2
        *       Multiplicación       2 * 4           8
        /          Division          10 / 2          5
        %       Módulo (resto)       10 % 3          1
*/

/*
    Operadores aritmeticos avanzados
    --------------------------------------------------------------------------------------
    ++ -> incrementa el valor de la variable en 1
    -- -> decrementa el valor de la variable en 1

    Prefijo: ++a o --a ->El valor se incrementa/drementa antes de ser usado
    Postfijo: a++ o a-- -> el valor original se usa primero, y luego se incrementa/decrementa
*/

/*
    Prioridad de los operadores aritmeticos
    --------------------------------------------------------------------------------------
    1 Paréntesis ()
    2 Multiplicacion, división y módulos (*, /, %)
    3 Suma y resta (+, -)
*/

/*
    Conversion de tipos
    --------------------------------------------------------------------------------------
    Conversión implícita: (implicit type conversion o type promotion): Ocurre automáticamente
    cuando C++ transforma un típo más pequeño o menos preciso en un más grande o más preciso.

    char -> int
    int -> float o double
    float -> double

    Conversión explícita: (explicit type casting o type casting): Especificada por el programor
    cuando se necesita cambiar manualmente el tipo de dato.

    Sintaxis básica de type casting
    C(antiguo): (tipo) valor
    C++(moderno y recomendado)
    -> static_casting<tipo>(valor) 
    -> dynamic_cast<tipo>(valor) :(para punteros y clases)
    -> const_cast<tipo>(valor) :para cambiar la caulidad const
    -> reinterpret_cast<tipo>(valor) :para reintepratar bit de datos

    C++ no permite convertir directamente entre cadenas(std::string) y números.
    Para estos, puedes usar funciones de la biblioteca estandar

    std::stoi y std::stod

    ->std::stoi: Convierte una cadena a aun entero (int)
    ->std::stod: Convierte un entero a cadena(double/float)
*/

using namespace std;


int main(){
    int a = 10, b = 3;
    int x = 5;
    float c = 3.0f;

    cout<< "Suma: "<< a + b <<endl;
    cout<< "Resta: "<< a - b<<endl;
    cout<< "Multiplicacion: "<< a * b <<endl; //Casteo implicito
    cout<< "Division: "<< a / c <<endl;
    cout<< "Modulo: "<< a % b <<endl;

    cout<<"-----------------------------------------"<< endl;

    cout<< "Valor inicial: "<< x <<endl;
    cout<< "Prefijo (++x): "<< ++x <<endl;
    cout<< "Postfijo (x++): "<< x++ <<endl;
    cout<< "Despues del posfijo: "<< x <<endl;

    cout<<"-----------------------------------------"<< endl;

    int resultado = 10 + 5 * 2;
    cout<<"Resultado sin parentesis es: "<<resultado <<endl;

    int result = (10 + 5) * 2;
    cout<<"Resultado con parentesis es: "<<result <<endl;

    cout<<"-----------------------------------------"<< endl;

    int d = 5;
    float e = 2.5f;
    float respuesta = d + e; // a (int) se convierte en float

    cout<< "Resultado: "<< respuesta <<endl;

    cout<<"-----------------------------------------"<< endl;

    string strNum = "18"; //Esto es un string porque esta entre comillas ""
    int num = stoi(strNum);

    cout<<"Cadena: "<<strNum <<endl;
    cout<<"Entero: "<<num <<endl;

    cout<<"-----------------------------------------"<< endl;

    int numeros = 123;
    string strNumero = to_string(numeros);

    cout<<"Entero: "<<numeros <<endl;
    cout<<"Cadena: "<<strNumero <<endl;

    return 0;
}