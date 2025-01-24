#include <iostream>
#include "Calculadora.h"

int main(){
    Calculadora calc;
    double num1, num2;

    std::cout<<"Bienvenidos a la calculadora"<<std::endl;

    // Entrada
    std::cout<<"intrudoce el primer numero: ";
    std::cin >> num1;
    calc.setOperando1(num1);

    std::cout<<"introduce el segundo numero: ";
    std::cin >> num2;
    calc.setOperando2(num2);

    // Mostrar resultados
    std::cout <<"\nResultados de la operaciones:\n";
    std::cout <<"Suma: "<<calc.sumar()<<std::endl;
    std::cout <<"Restar: "<<calc.restar()<<std::endl;
    std::cout <<"Multiplicacion: "<<calc.multiplicar()<<std::endl;

    try{
        std::cout <<"Division: "<<calc.dividir()<<std::endl;
    } catch (const std::runtime_error& e){
        std::cout<<e.what()<<std::endl; // Manejo de error en división por cero.
    }

    return 0;
}

