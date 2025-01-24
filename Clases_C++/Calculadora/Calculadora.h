#ifndef CALCULADORA_H
#define CALCULADORA_H

#include "Operando.h"

class Calculadora{
private:
    Operando operando1;
    Operando operando2;

public:
    Calculadora(); // Constructor por defecto.

    // Setter para los operados
    void setOperando1(double valor);
    void setOperando2(double valor);

    // Getter
    double getOperando1()const;
    double getOperando2()const;

    // Métodos de cálculo
    double sumar() const;
    double restar() const;
    double multiplicar() const;
    double dividir() const;
};

#endif