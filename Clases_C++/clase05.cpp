/* CLASES
    --------------------------------------------------------------------------------------
    Una clase es un plano o platnilla que define las propiedades (ATRIBUTOS) y comportamientos,
    (MÉTODOS) de un objeto. Los objetos son instcias de las clases.

    GETTER & SETTER
    Los getter y stter son métodos de una clase utilizados para ACCEDER y MODIFICAR los atributos
    privados o protegidos. Ayudan a implemetar el principio de ENCAPSULAMIENTOS al controlar cómo se
    accede y manipulan los datos internos de una clase.

    - Control de acceso: Evitan el acceso directo a los atributos de la clase.
    - Validación: Permiten agregar validaciones antes de modificar los datos.
    - Ocultación de datos: Ocultan los detalles internos y exponene solo la interfaz publica

    Sintaxis básica
    getter:
        tipo getNombreAtributo(){
            return atributo;
        }
    setter:
        void setNombreAtributo(tipo nuevoValor){
        atributo = nuevoValor;
        }

    ENCAPSULAMIENTO
    Caracteriticas clave
    Encapsulamiento: Los datos están protegidos con modificadores de acceso como "private", "public" y "protected"

    - public: Los miembros públicos y protegidos del padre permanecen iguales en la clase hija
    - protected: Los miembros públicos y protegidos del padre se convierten en protegidos en la hija
    - private: Los miembros públicos y protegidos del padre se convierten en privados en la hija

    Constructores y destuctores:
    - El constructor inicializa los atributos cuando se crea un objeto
    - El destructor (~NombreClase) libera recursos (se llama automáticamente al destruir el objeto)

    HERENCIA
    - Herencia simple: Una clase hija hereda de una única clase padre
    - Herencia múltiple: Una clase hija hereda de múlples clase padres
    - Herencia jerárquica: Varias clases hijas heredan de una única clase padre
    - Sobrescritura de métodos: Una clase hija puede redefinir un método de la clase base

    class ClaseHija : public ClasePadre1, public ClasePadre2 {...};

    POLIMORFISMO
    El polimorfismo es la capacidad de un objeto de tomar múltiples formas. En términos simples, significa que un objeto
    de una clase derivada puede ser tratado como si fuera de la calse base, pero puede ejecutar su propia su propia implementación
    métodos.

    - Existen dos tipos principales de polimorfismo en C++:
    - Polimorfismo en tiempo de compilación (estático)
        Se logra madiante sobrecarga de funciones o de operadores
    - Polimorfismo en tiempo de ejecución (dinámico):
        Se logra utilizando funciones virtuales y punteros o referencias de la clase base.

    ABSTRACION
    Una clase abstracta es aquella que no puede ser instanciada directametne y está diseñada para ser heredada. Sirve
    como plantilla o base para otras clases. Contiene al menos una función virtual pura.

    Función virtual pura
    Se declara usando = 0 en su definición. Una función virutal pura obligada a las clases derivadas
    a proporcionar su propia implementacion

    Ventajas de la abstracción
    Oculta los detalles de implementación:
        Reduce la complejidad del programa al exponer solo las funcionalidades esenciales.
    Promueve la reutilización del código:
        Las clases abstractas proporcionan una base para que otras clases reutilicen sus funciones.
    Facilita el mantenimiento y la escalabilidad:
        Los cambios en la implementación no afectan el uso de la interfaz.

    DIFERENCIAS ENTRE ABSTRACCIÓN Y ENCAPSULACIÓN
    Abstracción                                                 Encapsulación
    --------------------------------------------------------------------------------------------------------------------------
    Se enfoca en que HACE un objeto                     |        Se enfoca en CÓMO PROTEGER los datos
    Se logra usando clases abstractas e interfaces      |        Se logra mentiante modificadores de accesso (public, private)
    Oculta la implementación interna                    |        Oculta los detalles de datos especificos
*/ 


#include <iostream>
using namespace std;

class Persona{ // Clase Padre
    private: // Atributos privados, solo accesibles dentro de la clase
    string nombre;
    int edad;

    public: // Método públicos, accesibles desde fuera de la clase
    // Constructor
    Persona(string _nombre, int _edad){
        nombre = _nombre;
        edad = _edad;
    }

    // Métodos
    void mostrarInformacion(){
        cout<<"Nombre: "<<nombre<<", Edad: "<<edad<<endl;
    }

    // Getter
    string getNombre(){
        return nombre;
    }

    // Setter
    void setNombre(string _nombre){
        nombre = _nombre;
    }
};

// Clase derivada (hija)
class Estudiante : public Persona{
private:
    string carrera;

public:
    Estudiante(string _nombre, int _edad, string _carrera)
        : Persona(_nombre, _edad), carrera(_carrera){}

    void mostrarInformacionEstudiante(){
        mostrarInformacion(); // Llamar al método de la clase base (Padre)
        cout <<"Carrera: "<<carrera<<endl;
    }
};

/* Sobre carga de funciones (estatico)
    La sobrecarga de funciones permite definir varias funciones con el mismo nombre,
    PERO con diferentes tipos o numeros de parámetros
*/
class Calculadora{
public:
    // Sobrecarga de funciones
    int suma(int a, int b){ // Enteros con 2 parametros
        return a + b;
    }

    double suma(double a, double b){ // Decimales con 2 parametros
        return a + b;
    }

    int suma(int a, int b, int c){ // Enteros con 3 parametros
        return a + b + c;
    }

    int suma(double a, double b, double c){
        return a + b + c;
    }

    int suma(int a, int b, int c, int d){
        return a + b + c + d;
    }
};

/* Sobrecarga de operadores(dinamica)
    Podemos redefinir operadores para trabajr con objetos personalizados
*/
class Complejo{
private:
    double real, imaginario;

public:
    Complejo(double r, double i): real(r), imaginario(i){}

    //Sobrecarga del operador +
    Complejo operator+(const Complejo& otro){
        return Complejo(real + otro.real, imaginario + otro.imaginario);
    }

    void mostrar(){
        cout<<real<<" + "<<imaginario<<"i"<<endl;
    }
};

//Clase abtracta
class Figura{
public:
    // Función virtual pura
    virtual void dibujar() = 0;

    // Función con implementación
    void mostrarMensaje(){
        cout<<"Soy un figura."<<endl;
    }
};

// Clase derivada 1
class Circulo : public Figura{
public:
    void dibujar() override{
        cout <<"Dibujando cn circulo. "<<endl;
    }
};

//Clase derivada 2
class Rectangulo : public Figura{
public:
    void dibujar()override{
        cout<<"Dibujando un rectangulo"<<endl;
    }
};

// Clase abstracta
class Vehiculo{
public:
    virtual void arrancar() = 0; // Método puro
    virtual void detener() = 0; // Método puro
};

// Clase derivada 1
class Carro : public Vehiculo{
public:
    void arrancar() override{
        cout<<"El carro esta arrancando."<<endl;
    }
    void detener() override{
        cout<<"El carro se detuvo."<<endl;
    }
};

// Clase derivada 2
class Motocicleta : public Vehiculo{
public:
    void arrancar() override{
        cout<<"La motocicleta esta arrancando."<<endl;
    }
    void detener() override{
        cout<<"La motocicleta se detuvo."<<endl;
    }
};


int main(){
    cout << "-------------------------------------------------" <<endl;
    // Crear un objeto de la clase Persona
    Persona persona1("Arturo", 18);
    persona1.mostrarInformacion();

    // Cambiar el nombre usnado un setter
    persona1.setNombre("Luis");
    persona1.mostrarInformacion();

    Estudiante estudiante1("Reyna", 23, "Ingenieria en sistemas computacionales");
    estudiante1.mostrarInformacionEstudiante();

    cout << "-------------------------------------------------" <<endl;
    Calculadora calc; // Crear el objeto calc de la clase Calculadora
    cout <<"Suma de enteros: "<<calc.suma(2, 3, 10, 8)<<endl;
    cout <<"Suma de dobles: "<<calc.suma(2.5, 3.5, 8.9)<<endl;
    cout <<"Suma de tres enteros: "<<calc.suma(2, 3, 5)<<endl;

    cout << "-------------------------------------------------" <<endl;
    Complejo c1(1.2, 3.4), c2(5.6, 7.8);
    Complejo c3 = c1 + c2;
    c3.mostrar();

    cout << "-------------------------------------------------" <<endl;
    Figura* figura1 = new Circulo();
    Figura* figura2 = new Rectangulo();

    figura1->dibujar(); // Llama a la implementación del Circulo
    figura2->dibujar(); // Llama a la implementación del Rectangulo

    figura1->mostrarMensaje();
    figura2->mostrarMensaje();

    // delete figura1;
    // delete figura2;

    cout << "-------------------------------------------------" <<endl;
    Vehiculo* vehiculo1 = new Carro();
    Vehiculo* vehiculo2 = new Motocicleta();

    vehiculo1->arrancar();
    vehiculo2->arrancar();

    vehiculo1->detener();
    vehiculo2->detener();


    return 0;
}