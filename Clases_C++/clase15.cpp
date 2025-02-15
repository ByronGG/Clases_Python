/* Funciones Lambda
    -------------------------------------------------------------------------------------------------
    Las expresiones lambda y funciones anónimas en C++ son herramientas muy potentes que te permiten definir funciones "sobre la marcha" sin necesidad de darles un nombre. Se introdujeron en C++11 y desde entonces se han convertido en una parte esencial para escribir código conciso y legible, especialmente al trabajar con algoritmos de la STL.

    Son funciones sin nombre definidas de forma local en lugar donde se necesitan. Su sintaxis básica es:

    [captura](parámetros) -> tipo_de_retorno (opcional) { código };

    auto suma = [](int a, int b) -> int{
        // LOGICA -> int
        return a + b; 
    };

    int resultado = suma(3, 4);
    cout << resultado << endl;

    - Captura: Especifica qué variables del entorno local se deben capturar (por valor, referencia, etc.)
    - parametros: Lista de parámetros que recibe la lambda, similar a una función normal. 
    - -> tipo_de_retorno: (Opcional): Especifica el tipo de retorno; a menudo se puede omitir y dejar que el compilador lo deduzca.
    - cuerpo: Bloque de código

    - Funciones Locales Y Temporales: Son ideales para funciones que se utilizan en un contexto muy específico y no se reutilizan en otros lugares
    - STL Y Algortimos: Muchas veces se usuan como argumentos para algortimos de la STL (como ejemplo std::sort, std::for_each, etc.) para definir criterios de ordaminetos, filtros o transformaciones.
    - Callbacks Y Eventos: Se usan para definir comportamientos en respuesta a ciertos eventos sin tener que declarar una función separada

    ------------------------------------------------------------------------------------------------------------------------------
    [caputa]: Especifica qué variables del entorno circundante queremos usuando dentro de la lambda y cómo: 
        - Por valor [x] copia la variblae x  dentro de la lambda
        - Por referencia [&x] permite acceder a x por referencia, pudiendo modificar la variable original
        - Captura por defecto: 
            [=]: captura todas la variables que se usan en la lambda por valor. 
            [&]: captura todas las variables que se usan en la lambda por referencia.
        - Mezcla de capturas: Por ejemplo, [=, &y] captura las variables por valor, excpeto y, que se captura por referencia. 
    (parametros): Se compota igual que los parámetros de cualquier función
    ->: puede especificar el tipo de retorno
    { cuerpo }: Es el bloque de código que se ejecutrá cuando invoques la lambda. 

    QUE OCURRE INTERNAMIENTE?
    Cuando escribe un lambda, el compilador genera una clase anónima con:
        - Un operador de función (operator()) sobrecargado, ques, es el que invoca cuando llamas a la lmabda. 
        - Miembros que almacenan las varialbes capturadas. 

    LAMBDA
        auto suma = [](int a, int b) -> int {return a + b; };
    
    Intermente el lambda según el compilador se veria algo así.... 

    class LambdaSuma{
    public:
        int operator()(int a, int b) const {return a+b;}
    };

    Captura y sus matices
    Por valor ([=] o [x]): Se hace una copia de la variable. Cualquier modificación en la lambda afecta solo a la copia
    Por referencia([&] o [&x]): La lambda trabaja directamente con la variable original, pudiendo modificarla

    Lambda Genéricas (C++ 14)
    puedes usar auto en la lista de parámetros para crear lambdas genéricas

    Captura del puntero this en métodos de clases
    Cuando es´tas dentro de un método de una clase, puedes capturar el puntero 'this' para acceder a los miembros de la clase
*/

#include <iostream>
#include <vector>
#include <algorithm> //Para usar a std::sort()

class MiClase{
public:
    int valor = 50;
    void mostrarValor(){
        auto lambda = [this](){ //Aquí, [this] caputa el puntero a la instacial acutial, permitiendo usar 'valor' dentro de la lambda
            std::cout <<"Valor de la clase: " << valor << "\n";
        };
        lambda();
    }
};


int main(){

    // Crear una instacia
    MiClase objecto;

    std::vector<int> numeros = {5,2,8,1,3};

    // Ordenamos de forma ascendente usando un lambda
    std::sort(numeros.begin(), numeros.end(), [](int a, int b){
        return a < b;
    });

    // Imprimir el vector
    std::for_each(numeros.begin(), numeros.end(), [](int n){
        std::cout << n << " ";
    });

    int contador = 0;

    auto incrementarPorValor = [contador]() mutable {
        // 'mutable' permite modificar la copia interna de 'contador'
        ++contador; // Prefijo
        return contador;
    };

    auto incrementarPorReferencia = [&contador](){
        // Sin la palabra clave mutable, una lambda que caputra por valor no permite modificar la copia interna de la varialbes capturadas
        ++contador;
        return contador;
    };

    std::cout <<"Por valor: " <<incrementarPorValor() << "\n"; // alt+92
    std::cout <<"Por valor: " <<incrementarPorValor() << "\n"; 
    std::cout <<"Por referencia: "<< incrementarPorReferencia() << "\n"; 
    std::cout <<"Por referencia: "<< incrementarPorReferencia() << "\n"; 
    std::cout <<"Por referencia: "<< incrementarPorReferencia() << "\n"; 
    std::cout <<"Por referencia: "<< incrementarPorReferencia() << "\n"; 
    std::cout <<"Por referencia: "<< incrementarPorReferencia() << "\n"; 
    std::cout <<"Valor original: "<< contador << "\n"; // Si se usó por referencia, 'contador'


    // Lambda Genéricas
    auto suma = [](auto a, auto b){return a+b;};

    std::cout << suma(5, 5) << "\n";  // int => 10
    std::cout << suma(3.5, 2.5) << "\n"; // double => 6.0
    std::cout << suma(6.28534167, 9) << "\n"; // double => 6.0

    objecto.mostrarValor();

    return 0;
}


/*
nombre = "Arturo" // Python => string "asbduyabsdua"
string nombre = "Arturo" // C++ => string
auto x = 5; // El compilador deduce que x es tipo int
auto y = 3.1416; // double
auto z = "Hola" // string
*/