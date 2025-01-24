#ifndef OPERANDO_H
#define OPERANDO_H

class Operando{
private:
    double valor; // Atributo privado (El cual necesita GETTER y/o SETTER)

public:
    Operando();     // Costructor por vació (por defecto)
    Operando(double valorIncial); // Contructor con valor incial => valor = 0

    // Getter
    double getValor() const;

    // Setter
    void setValor(double nuevoValor);
};

#endif