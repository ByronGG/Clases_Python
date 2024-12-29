#include <iostream>
#include <string>
#include "LocalTime.cpp"
using namespace std;

class Flight {
private:
    string code;        // Código del vuelo
    string destination; // Destino
    string gate;        // Puerta de embarque
    string checkIn;     // Punto de registro
    string comment;     // Comentario
    LocalTime expected; // Hora esperada del vuelo

public:
    // Constructor
    Flight(string code, string destination, string gate, string checkIn, LocalTime expected)
        : code(code), destination(destination), gate(gate), checkIn(checkIn), expected(expected) {}

    // Destructor
    ~Flight() {}

    // Métodos getters
    string get_code() const { return code; }
    string get_destination() const { return destination; }
    string get_gate() const { return gate; }
    string get_checkIn() const { return checkIn; }
    string get_comment() const { return comment; }
    LocalTime get_expected() const { return expected; }

    // Métodos setters
    void set_comment(string newComment) { comment = newComment; }
    void set_expected(LocalTime newExpected) { expected = newExpected; }

    // Verificar si el vuelo es de llegada o salida
    bool is_arrival() const { return comment == "arrival"; }
    bool is_departure() const { return comment == "departure"; }

    // Imprimir detalles del vuelo
    void print() const {
        cout << "Vuelo: " << code << endl;
        cout << "Destino: " << destination << endl;
        cout << "Puerta: " << gate << endl;
        cout << "Check-In: " << checkIn << endl;
        cout << "Hora esperada: ";
        expected.print();
        cout << "Comentario: " << comment << endl;
    }
};
