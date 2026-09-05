/*
    Paradigma estructurado al orientado a objetos (POO)
    La POO no es un "una forma más elegenta de escribir código". Es una respuesta a estos "dolores de cabeza" a la hora de programar/escalar sistemas

    La idea central:
    Un objeto agrupa lo datos y el comportamiento que los manipula, y controla quien puede tocarlos.


    Concepto    Definición                              Analogia
    Clase       El molde, la plantilla                  El plano de una casa
    Objeto      Una instancia concreta del modelo       La casa contruida en la calle X
    Atributo    Dato que describe el estado             Número de habitaciones
    Método      Operación que el objeto sabe hacer      Abrir una puerta

    Una clase se escribe una vez; los objetos se crean cuantas veces hagan falta y cada uno tiene su propio estado.

    Los cuatro pilaes de POO
    1. Encapsulamiento - Ocultar el estado interno y exponer solo una interfaz controlada.
                         Beneficio: el objeto garantiza sus propias reglas (invatiantes). Un solario nunca podrá ser negativo porque el único camino para cambiarlo pasa por una validación.
    2. Abstracción - Exponer qué hace un objeto, no cómo lo hace.
                     Beneficio: puedes cambiar la implmentación sin romper a quien use la clase
    3. Herencia - una clase puede especializarse a partir de otra reutilizando sus comportamiento.
                  Beneficio: modelas relaciones "en un" sin duplicar código
    4. Polimorfismo - Un mismo mensaje produce compotamientos distintos según el tipo real del objeto.
                      Beneficio: el código cliente deja de tener cadenas de if/else por tipo
*/
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>

struct Empleado{
    private:                    // nadie fuera de la clase puede tocar esto!!!
        std::string nombre;
        double salario;
        int añosServicio;

    public:
        Empleado(const std::string& nombre, double salario, int años)
        : nombre(nombre), salario(salario), añosServicio(años){
            if (salario < 0){
                throw std::invalid_argument("El salario no pueder negativo");
            }
        }

        double calularBono() const{      // el comportamiento vive con el dato
            return salario * 0.10 * añosServicio;
        }

        void amuntarSalario(double porcentaje){
            if (porcentaje <= 0) return; // la regla se cumple siempre
            salario *= (1.0 + porcentaje / 100.00);
        }

        std::string getNombre() const {return nombre;}
        double getSalario() const {return salario;}
};

int main(){
    Empleado e{"Arturo", 25000.0, 3};
    // Arturo.salario = -5000 // ERROE de compilación:  es privado
    e.amuntarSalario(10);
    std::cout <<e.getNombre() << " gana " << e.getSalario() << " y su bono es " << e.calularBono() << "\n";
}
 

/*
    Código que no cumple la paradgima de programción orientada a objetos

#include <iostream>
#include <string>
#include <vector>

struct Empleado {
    std::string nombre;
    double salario;
    int aniosServicio;
};

double calcularBono(const Empleado& e) {
    return e.salario * 0.10 * e.aniosServicio;
}

void imprimir(const Empleado& e) {
    std::cout << e.nombre << ": " << e.salario << "\n";
}

int main() {
    Empleado e{"Arturo", 25000.0, 3};
    e.salario = -5000;          // (1) nada lo impide
    e.aniosServicio = 900;      // (2) tampoco esto
    std::cout << calcularBono(e) << "\n";
}
*/