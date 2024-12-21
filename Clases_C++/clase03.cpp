/* WHILE
    --------------------------------------------------------------------------------------
    Es una estructura de control que permite repetir un bloque de código mientras una condición
    sea verdadera. Es útil cuando NO SABES CÚANTAS VECES NECESITAS REPETIR UN CONJUNTO, pero sabes
    que debe continuar mientras se cumpla una condición específica.

    Sintaxis básica while
    while(cindición){
        // Código se ejecutará
    }
*/

/* DO - WHILE
    --------------------------------------------------------------------------------------
    Es una estructura de control que garantiza que el bloque de código se ejecutará al menos una vez,
    independientemente de si la condición es verdadera o falsa en la primera interación

    Sintaxis básica de do-while
    do{
        // Código que se ejectura al menos una vez
    } while (condición){
        // Código while
    }

    - El bloque de código simepre se ejecuta al menos una vez antes de evualar la condición
    - Después de ejecutar el bloque, se evalúa la condicón:
        - Verdera repite
        - Falsa termina el bucle

    ASPECTO                     WHILE                                       DO-WHILE
    --------------------------------------------------------------------------------------
    Evaluación                  Evalua la condicion de inicio               Evalua la condición al final        
    Ejecución Mínima            Puede no ejecutar el bloque nunca           Seimpre ejecuta el bloque AL MENOS UNA VEZ!

    Ventajas DO - WHILE
    - Util cuando necesitas ejecutar el bloque de codigo almenos una vez.
    - Ideal para validaciones de datos
    - Mas intitivo que while para ciertas tareas, como reptir acciones basadas en el entrada del usuario
*/

/* FOR
    --------------------------------------------------------------------------------------
    Es una estructura de control que se utiliza para repetir un bloque de código un numero especifico
    de veces. Es ideal cuando conoces de antemano cuántas iteraciones necesitas realizar.

    Sintaxis básica del FOR
    for(inicializacion; condicon; actualizacion){
        // Código que se ejecutará en cada iteración
    }

    - Inicialización: Se ejecuta una vez al comienzo del bucle. AQUÍ se suele declar o inicializar una variable control
    - Condición: Se evalúa antes de cada iteración. Si es verdadera, el bucle contnua; si es falsa, el bucle temrina
    - Acutalización: Se ejecuta al final de cada iteración para modificar la variable control.
*/


#include <iostream>
using namespace std;

int main(){
    //Variables
    int contador = 1; // Inicilización
    int num;
    int a = 0;

    while (contador <= 5){ // Condición
        cout <<"Numero: "<< contador <<endl;
        contador++; // Actualización
    }

    cout << "-------------------------------------------------" <<endl;

    cout<<"Introduce un numero positivo: ";
    cin>>num;

    while(num < 0){ // Condición según el usuario
        cout <<"El numero no es positivo. Intenta nuevamente: ";
        cin>>num;
    }

    cout<<"Numero aceptado: "<<num<<endl;

    cout << "----------------WHILE TRUE - IF BREAK---------------------------------" <<endl;

    while(true){
        int x;
        cout<<"Introduce un numero (0 para salir): ";
        cin>>x;
        if(x == 0){
            break;
        }
    }

    cout << "------------------WHILE TRUE - IF CONTINUE-------------------------------" <<endl;

    while(a < 10){
        a++;
        if (a % 2 == 0){
            continue; // Salta el resto de esta iteración si a es
        }
        cout << "Numero impar: " <<a<<endl;
    }

    cout << "--------------------DO - WHILE-----------------------------" <<endl;

    int contador_do = 1;

    do{ // Bucle que se ejectua hasta terminada la condición
        cout<<"Numero"<<contador_do<<endl;
        contador_do++; // Actualización
    } while(contador <= 5); // Condición

    cout << "-------------------DO - SWITCH - WHILE------------------------------" <<endl;

    int opcion;

    do{
        cout<<"Menu: "<<endl;
        cout<<"1. Hola: "<<endl;
        cout<<"2. Adios: "<<endl;
        cout<<"3. Salir: "<<endl;
        cout<<"Elige una opcion: "<<endl;
        cin>>opcion;

        switch(opcion){
            case 1:
                cout<<"HOLA :D"<<endl;
                break;
            case 2:
                cout<<"ADIOS :_:"<<endl;
                break;
            case 3:
                cout<<"Salir del programa..."<<endl;
                break;
            default: //Opcional
                cout<<"Opcion no valida. Intentalo de nuevo."<<endl;
        }
    } while (opcion != 3);


    cout << "-------------------------------------------------" <<endl;

    for(int i = 1; i <= 10; i++){ // Inicialización (i), condicion (i<=10), actualización(i++)
        cout<<"Iteracion: "<<i<<endl;
    }

    for(int i = 10; i >= 0; i--){ // Inicialización (i), condicion (i>=0), actualización(i--)
        cout<<"Cuenta regresiva: "<<i<<endl;
    }

    cout << "------------------CONDICIÓN MÚILTPLE-------------------------------" <<endl;

    for(int i = 1, j = 5; i <= 5 && j >= 1; i++, j--){ // Dos variables de control
        cout<<"i: "<< i << ", j: "<<j <<endl;
    }

    int numeros[] = {1, 2, 3, 4, 5}; // Arreglos

    for(int k = 0; k < 5; k++){
        cout<<"Elemento del arreglo "<< k <<": "<<numeros[k]<<endl;
    }

    cout << "-----------------FOR ANIDADO--------------------------------" <<endl;

    int matriz[3][3] = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
        };

        for(int i = 0; i < 3; i++){ // FILA
            for(int j = 0; j < 3; j++){ // COLUMNA
                cout <<matriz[i][j]<< " ";
            }
            cout << endl; // Salto de línea al final de cada fila
        }

    return 0;
}

