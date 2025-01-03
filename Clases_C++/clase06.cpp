/* Función en C++ 
    --------------------------------------------------------------------------------------------------------------------------
    Las funciones son bloque de código que realizan tareas especícicas estas tiene varios tipos (void, int, bool, float).
    Son fundamentales para estructurar programas, reducir redundancias y mejorar la legibilidad del código

    Tipos de funciones y el uso de return

    Tipo                                       Descipcion                                   Necesita return
    void                                       No devulevo ni un valor                      No
    Función con tipo de retorno                Devuelven el valor como int, double,
                                                string, bool, etc.alignas                   Sí (debe coincidir con el tipo)
    Función recursiva                           Se llama a sí mismas, devuleve un valor
                                                si no es void                               Depende del tipo de la función
    Función de sobrecarga                       Mismo nombre, diferente lista de parametros Depende del tipo
    Función Lambda                              Definida directamente en un expresión       Depende del tipo de la función

    Sintaxis Básica de la función
    tipo_retorno nombre_funcion (tipo_param1 param1, tipo_param2 param2...){
    // Código
    return valor; // (OPCIONAL dependiendo del tipo de retorno)
    }

    Funciones recursivas
    - una funcióin que se llama a sí misma. Útil para problemas como factoriales, fibonacci, ect.

    Funciones en espacios de nombre (namespaces)
    - Organizar funciones para evitar conflictos de nombre

    PASO DE PARÁMETROS
    --------------------------------------------------------------------------------------------------------------------------
    - Por valor: Crear un copia del argumento. Los cambios no afectan la variable original
    - Por referencia: Se pasa la dirección del argumento, permitiendo modificar la variable original
    - Por puntero: Similar a la referencia, pero explícito con punteros. 

    Buenas practicas
    --------------------------------------------------------------------------------------------------------------------------
    - Mantener la funciones pequeñas y especificas
    - Usar nombres descriptivos
    - Agrupar funciones relacionadas en clases o namespaces
    - Evitar efectos secundario: Las funciones deben modificar solo lo necesario
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;


void saludar(){
        std::cout<<"Hola Mundo"<<std::endl;
} // No necesita un return ya que la función es tipo vacia (VOID)

int sumar(int a, int b){
    return a + b;
} // Si necesita un return para regresar el valor de la suma de A y B

void imprimirMensaje(std::string mensaje = "Mensaje por defecto"){
    std::cout<<mensaje<<std::endl;
} //Funciones con parámetros predeterminados

int calcular(int a, int b){
    return a + b;
}

double calcular(double a, double b){
    return a * b;
} // Sobrecargar funciones, permiten usar el mismo nombre de la función (calcular) pero con diferentes listas de parámetros

void modificar(int x){
    x = 10;
} // Por valor

void modificar(int &x){
    x = 10; 
} // Por referencia

void modificar(int *x){
    *x = 10;
} // Por puntero

int factorial(int n){
    if(n <= 1) return 1;
    return n * factorial(n - 1);
}

namespace Matematicas{
    int sumar(int a, int b){
        return a + b;
    }
    int restar(int a, int b){
        return a - b;
    }
    int multiplicar(int a, int b){
        return a * b;
    }
    double dividir(double a, double b){
        return a / b;
    }
}

class Producto{ // CLASE PADRE
    private:
        int id;
        std::string nombre;
        int cantidad;
        double precio;
    
    public:
        // Constructor
        Producto(int _id, std::string _nombre, int _cantidad, double _precio)
            : id(_id), nombre(_nombre), cantidad(_cantidad), precio(_precio){}

        // Getters
        int getId() const{return id;}
        std::string getNombre() const{return nombre;}
        int getCantidad() const{return cantidad;} // Int = sin punto decimal 9
        double getPrecio() const{return precio;} // Double = punto decimal 9.80

        // Setter
        void setCantidad(int _cantidad) {cantidad = _cantidad;}

        // Mostrar información del producto (MÉTODO)
        void mostrarInfo() const{
            std::cout <<"ID: "<<id
                    << "| Nombre: "<<nombre
                    << "| Cantidad: "<<cantidad
                    << "| Precio $: "<<precio <<std::endl;
        }
};

class Inventario{
    private:
        std::vector<Producto> productos;

    public:
        // Agregar un productor al invetario
        void agregarProducto(int id, const std::string nombre, int cantidad, double precio){
            productos.emplace_back(id, nombre, cantidad, precio);
        }

    /* CRUD
    --------------------------------------------------------------------------------------------------------------------------
    C: Create
    R: Read
    U: Update
    D: Delete
    */

    // Listar todo los productos
    void listarProductos() const{
        if(productos.empty()){
            std::cout<<"El Inventario esta vacio.\n";
            return;
        }
        std::cout<<"Lista de productos:\n";
        for(const auto& producto : productos){
            producto.mostrarInfo();
        }
    }

    // Buscar producto por ID
    void buscarProductoPorId(int id) const{
        for(const auto& producto : productos){
            if(producto.getId() == id){
                std::cout<<"Producto encontrado: \n";
                producto.mostrarInfo();
                return;
            }
        }
        std::cout<<"No se encontro ningun producto con ID: "<<id<<std::endl;
    }
};


int main(){

    Inventario inventario; // Objeto
    int opcion;

    do{
        std::cout<<"\n--- Menu de inventario ---\n";
        std::cout<<" 1. Agregar producto \n";
        std::cout<<" 2. Listar productos\n";
        std::cout<<" 3. Buscar productor por ID\n";
        std::cout<<" 4. Salir\n";
        std::cout<<" Seleccione una opcion: ";
        std::cin >> opcion;

        switch(opcion){
            case 1:{
                int id, cantidad;
                double precio;
                std::string nombre;

                std::cout<<"Ingrese el ID del producto: ";
                std::cin >>id; 
                std::cin.ignore(); // Limpiar el buffer de datos
                std::cout<<"Ingrese el nombre del producto: ";
                std::getline(std::cin, nombre);
                std::cout<<"Ingrese la cantidad: ";
                std::cin>>cantidad; 
                std::cout<<"Ingrese el precio: ";
                std::cin>>precio;

                inventario.agregarProducto(id, nombre, cantidad, precio);
                std::cout<<"Producto agregado correctamente. \n";
                break;
            }
            case 2:
                inventario.listarProductos();
                break;
            case 3:
                int id;
                std::cout<<"Ingrese el ID del producto a buscar: ";
                std::cin >> id;
                inventario.buscarProductoPorId(id);
                break;
            case 4:
                std::cout<<"Saliendo del programa...\n";
                break;
            default:
                std::cout<<"Opcion no calida. Intente de nuevo. \n";
                break;
        }
    } while(opcion != 4);
    return 0;
}