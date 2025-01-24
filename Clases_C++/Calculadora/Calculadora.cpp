#include "Calculadora.h"
#include <stdexcept>


// Constructor por defecto
Calculadora::Calculadora(): operando1(0), operando2(0){}

// Setter para los operandos
void Calculadora::setOperando1(double valor){
    operando1.setValor(valor);
}

void Calculadora::setOperando2(double valor){
    operando2.setValor(valor);
}

// Getter para los operandos
double Calculadora::getOperando1() const{
    return operando1.getValor();
}

double Calculadora::getOperando2() const{
    return operando2.getValor();
}

// Métodos de cálculo
double Calculadora::sumar() const{
    return operando1.getValor() + operando2.getValor();
}

double Calculadora::restar() const{
    return operando1.getValor() - operando2.getValor();
}

double Calculadora::multiplicar() const{
    return operando1.getValor() * operando2.getValor();
}

double Calculadora::dividir() const{
    if(operando2.getValor() == 0){
        throw std::runtime_error("Error: Division entre Cero");
    }
    return operando1.getValor() / operando2.getValor();
}