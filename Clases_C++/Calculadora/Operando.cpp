#include "Operando.h"

// Constructor por defecto
Operando::Operando(): valor(0){}

// Constructor con valor inicial
Operando::Operando(double valorIncial) : valor(valorIncial){}

// Getter
double Operando::getValor() const{
    return valor;
}

// Setter
void Operando::setValor(double nuevoValor){
    valor = nuevoValor;
}

