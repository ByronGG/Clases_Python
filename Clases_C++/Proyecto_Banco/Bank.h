/* Archivos .h
    --------------------------------------------------------------------------------------
    Los archivos .h (también llamados archivos de encabezado o header files) son una parte fundamental en la programación en C y C++. Estos archivos generalmente contienen declaraciones, es decir, la definición de clases, funciones, constantes, macros y otros elementos que serán usados en uno o más archivos .cpp.

    Que contiene un archivo .h 
    - Clases y sus atributos se declara en archivos .h 
    - Solo se declaran, no se implementan los métodos. 
    - Las funciones se declara (solo se define su firma) para que otros archivos puedan saber que existen. 
    - Permite declara tipos personalizados compartidos. 
    - Se pueden definir valor constantes o macros que se usan en múltiples lugares. 

    EL ARCHIVO .h, DECLARAMOS "QUE HACE LAS CALSES O FUNCIONES"
    EL ARCHIVO .cpp, IMPLEMENTAMOS "COMO LO HACE"

    El uso de #ifndef, junto con #define y #endif, es una técnica llamada guarda de inclusión o include guard. Esta se utiliza en los archivos de encabezado (.h) en C y C++ para evitar que el mismo archivo sea incluido varias veces en un proyecto durante la compilación.

    ¿Por qué es necesario?
    Cuando un archivo de encabezado (.h) es incluido múltiples veces, directa o indirectamente, puede causar errores de compilación debido a la redefinición de clases, funciones o variables. Esto sucede porque el preprocesador copia el contenido del archivo de encabezado donde sea que se incluya con #include.

    Por ejemplo: Si incluyes un archivo de encabezado en varios archivos .cpp, el compilador intentará procesar las mismas declaraciones varias veces.

    Sintaxis basica
    #ifndef NOMBRE_UNICO
    #define NOMBRE_UNICO

    // Declaraciones y definiciones del archivo de encabezado

    #endif

    Paso a paso:
    #ifndef (If Not Defined):
    Verifica si una macro con un nombre único (en este caso, NOMBRE_UNICO) ya ha sido definida.

    Si no está definida, ejecuta el código que sigue (el contenido del archivo de encabezado).
    #define:
    Si la macro no existía, se define con el nombre único (NOMBRE_UNICO).

    #endif:
    Marca el final del bloque que debe ejecutarse si la macro no estaba definida.

    En esencia, el preprocesador incluye el contenido del archivo solo una vez, porque la segunda vez que se intenta incluir, la macro ya estará definida.
    */

#ifndef BANK_H
#define BANK_H

#include <string>
#include <vector>
#include "Customer.h"

class Bank{
    private:
        int bankId;
        std::string name;
        std::string location;
        std::vector<Customer> customers;

    public:
        Bank(int id, const std::string& name, const std::string& location);

        int getBankid() const;
        std::string getName() const;
        std::string getLocation() const;

        void addCustomer(const Customer& customer);
        void displayCustomer()const;
};

#endif