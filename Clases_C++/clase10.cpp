/* Getters y Setter
    -------------------------------------------------------------------------------------------------------------------------
    Son métodos utilizados para acceder y modificar los atributos privados de una clase. En C++, es una buena práctica declarar los atributos de una clase como privados para protegerlos de accesos o modificaciones indebidos desde fuera de la clase. Por eso, usamos getters y setters para interactuar con ellos.

    Get
    - Permite obtener un valor de un atributo privado
    - Devuelve el valor del atributo sin permitir modificarlo
    Set
    - Permite modificar el valor de un atributo privado.
    - Recibe un parámetro y lo asigna al atributo correspondiente.

    Archivo .h (Header Files)
    Son archivo de cabecera que contiene las DECLERACIONES DE CLASES, ATRIBUTOS Y METODOS. Actúan como la "interfaz" que otros
    archivo pueden usar.
    Operando.h Declarar la clase Operando, con atributos, valores, etc. (Privado), y los métodos públicos (getValor() - setValor())
    Calculadora.h declaramos la clase Calculadora, utilizar objetos de clase operando y método sumar() - restar() - multi()

    Archivo .cpp (C++)
    Son los archivo de implementación donde se define la lógica de las clases y los métodos declarado del archivo .h (Header)
    Operando.cpp: Implementar los métodos de la clase Operando declarados en Operando.h
    Calculadora.cpp : Implentar los métodos de la clase Claculdaora declarados en Calculadora.h (Logica)

    Relación entre .h y .cpp
    - Difine que atributos y metodos tiene la clase
    - Se incluye en los archivos .cpp
    Archivo .cpp (Implementación):
    - Define cómo funcionan los métodos

    * Escalabilidad:
        Si en el futuro queires agregar nuevas operaciones (potencia, raíces), puedes hacerlos fácilmente sin alterar la estructa ya establecida
    * Encapsulación:
        Los atributos son privados, y el acceso se arealiza mediante métodos públicos (get y set). Estos protegen los datos y permite agregar validaciones en los setter
    * Mantenimiento: 
        Las clases declaradas en .h pueden reutilizarse en otros proyectos o módulos.
    * Sepración (Responsabilidades):
        Delcaraciones (.h) y las implementaciones (.cpp) están separadas, haciendo el código más organizado y fácil de mantener

*/


#include <iostream>
using namespace std;

int main(){


    return 0;
}

