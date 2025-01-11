/* Entrada de usuario std::cin
    --------------------------------------------------------------------------------------
    Si es necesario caputar un linea de texto, se utiliza std::getline en lugar del std::cin
    - Si el usuario ingresa un dato inválida, se puede manejarlo limpiando el flujo de entrada
*/

/* IF / ELSE / ELSE IF
    --------------------------------------------------------------------------------------
    El bloque if se usa para ejecutar un conjunto de instrucciones solo si una condición se evalúa
    como verdadera
    
    Sintaxis básica del IF
    if(condición){
    // Código a ejecutar si la condición es verdadera
    }

    El bloque else se usa para ejecutar instruccion si la condición del if es false

    Sintaxis básica del IF/ELSE
    if(condición){
    // Código a ejecutar si la condición es verdadera
    } else {
    // Código si la condición es falsa
    }

    Si hay varias condiciones, puedes usar else if para evaluarlas una por una

    Sintaxis básica del ELSE IF
    if(condición){
    // Código a ejecutar si la condición es verdadera
    } else if (condición2){
    // Código si condición2 es verdad
    } else {
    // Código si NINGUA condición es verdara
    }
*/

/* Condiciones compuestas o Operadores logicos (Computación booleana)
    --------------------------------------------------------------------------------------
    && (AND): Todas las condiciones deben ser verdaderas.
    || (OR): Al menos una condición debe ser verdadera.
    ! (NOT): Niega una condición.
*/

/* Operadores de compración
    --------------------------------------------------------------------------------------
    == : igual a                  a == b                  false
    != : Distinto que             a != b                  true
    < : Menor que                 a < b                   false
    > : Mayor que                 a > b                   true
    <= : Menor o igual que        a <= b                  false
    >= : Mayor o igual que        a >= b                  true
*/

/* Operador ternario
    --------------------------------------------------------------------------------------
    El operador ternario en C++ es una forma compacta de escribir una condición simple
    en una sola línea. Se utiliza para evaluar una condición

    Sintaxis del operador ternario
    condición ? valor_verdadero : valor_falso;

    - condición: Una expresión que se evalua como verdadera (true) o falsa (false).
    - valor_verdadero: El valor que se devuelve si es true.
    - valor_falso: El valor que se devuelve si es falso.

    Comparación VENTAJAS
    if - else: Fácil de leer y adecuado para condiciones complejas
    Operador Ternario: Compacto y para asignaciones simples

    Compración DESVENTAJAS
    if - else: Puede ser más largo condiciones simples
    Operador Ternario: Difícil de leer si hay anidamiento o lógica compleja
*/

/* SWITCH
    --------------------------------------------------------------------------------------
    El switch evalúa una expresión y ejecuta el bloque de código asociado al caso que coincida.
    Si no hay condicidencia, ejecuta el bloque default (opcional).

    Sintaxis básica del switch
    switch(expresión){
    case valor1:
        // Código
        break;
    case valor2:
        // Código
        break;
    case valor3:
        // Código
        break;
    // Más casos...
    default:
        // Código sin ningún caso coincide (opcional)
    }

    - expresión: Debe ser un tipo integral o enumerado como int, char o enum
    - case valor: Compara la expresión con valor. Si coinciden, se ejecuta el bloque de código
    - break: Detiene la ejecuciín dentro del swtich
    - default: Es opcional y se ejecuta si nungún case coincide
*/

#include <iostream>
#include <string> //Para usar std::string
using namespace std;

int main(){
    string texto;
    int numero, numero_2;
    int numero_3;
    int edad;
    char op;
    bool esEstudiante = false;

    cout << "ingresa linea de texto: ";
    getline(cin, texto);
    cout <<"El texto que ingresaste es: \"" <<texto << "\"" <<endl;
    
    cout << "-------------------------------------------------" <<endl;

    cout <<"Ingresa un numero: ";

    if(cin >> numero){
        cout << "El numero que ingresate es: " <<numero <<endl;
    } else {
        cout <<"Error: Debes ingresar un numero valido"<<endl;
        cin.clear(); // Limpia el estado del flujo
        cin.ignore(1000, '\n'); //Ignorar caracteres adicionales
    }

    cout << "-------------------------------------------------" <<endl;

    cout << "Ingresa otro numero: "<<endl;
    cin >> numero;

    if(numero > 0){
        cout <<"El numero es positvo." <<endl;
    } else if (numero < 0){
        cout <<"El numero es negativo" <<endl;
    } else {
        cout <<"El numero es cero" <<endl;
    }

    cout << "-------------------------------------------------" <<endl;

    cout<<"Ingresa tu edad: ";
    cin >> edad;

    if (edad >= 18 && edad <= 70){
        cout <<"Eres un adulto" <<endl;
    } else if(edad < 18){
        cout <<"Eres menor de edad." <<endl;
    } else{
        cout <<"Estas en la tercera edad" <<endl;
    }

    cout << "-------------------------------------------------" <<endl;

    if(!esEstudiante){
        cout<<"No es estudiante"<<endl; // Condición verdadera al inicializar en false
    } else{
        cout<<"Es estudiante"<<endl; // falsa
    }

    cout << "-------------------------------------------------" <<endl;


    cout<<"Ingresa tu edad (Operador Ternario)"<<endl;
    cin >> edad;

    /*
    if (edad >= 18){
        cout<<"Eres mayor de edad"<<endl;
    } else {
        cout<<"Eres menor de edad"<<endl;
    }
    */

    // Usando operador ternario
    string resultado = (edad >= 18) ? "Eres mayor de edad." : "Eres menor de edad.";
    cout << resultado <<endl;

    cout<<"Ingrea un numero (Operador Ternario)"<<endl;
    cin >>numero_2;

    string resultado_2 = (numero_2 % 2 == 0) ? "Par" : "Impar";
    cout<<"El numero es: "<< resultado_2 <<endl;

    cout << "--------------------EJEMPLO ANIDADO-----------------------------" <<endl;

    // Operador ternario anidado
    string resultado_3 = (numero_3 > 0) ? "Positivo" :
                        (numero_3 < 0) ? "Negativo" : "Cero";

    cout<<"El numero es: "<< resultado<<endl;

    cout << "---------------------EJEMPLO SWITCH----------------------------" <<endl;

    cout<<"Selecciona una opcion (a, b, c): ";
    cin >> op;

    switch (op){
        case 'a':
            cout<<"Seleccionaste a"<<endl;
            break;
        case 'b':
            cout<<"Seleccionaste b"<<endl;
            break;
        case 'c':
            cout<<"Seleccionaste c"<<endl;
            break;
        default:
            cout<<"Fin del programa"<<endl;
    }


    return 0;
}

