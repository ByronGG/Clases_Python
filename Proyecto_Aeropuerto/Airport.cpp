#include <vector>
#include <string>
#include <iostream>
#include "Flight.cpp"

using namespace std;

class Airport {
private:
    string name;              // Nombre del aeropuerto
    vector<Flight> flights;   // Lista de vuelos programados

public:
    // Constructor
    Airport(string name) : name(name) {}

    // Destructor
    ~Airport() {}

    // Programar un vuelo
    void schedule(const Flight& flight) {
        flights.push_back(flight);
    }

    // Agregar comentario a un vuelo específico
    void comment(string flightCode, string newComment) {
        for (Flight& flight : flights) {
            if (flight.get_code() == flightCode) {
                flight.set_comment(newComment);
                return;
            }
        }
        cout << "Vuelo no encontrado: " << flightCode << endl;
    }

    // Retrasar un vuelo
    void delay(string flightCode, int delayMinutes) {
        for (Flight& flight : flights) {
            if (flight.get_code() == flightCode) {
                LocalTime delayedTime = flight.get_expected();
                delayedTime.set_time(delayedTime.get_hour(), delayedTime.get_minute() + delayMinutes);
                flight.set_expected(delayedTime);
                return;
            }
        }
        cout << "Vuelo no encontrado: " << flightCode << endl;
    }

    // Imprimir todos los vuelos del aeropuerto
    void print() const {
        cout << "Aeropuerto: " << name << endl;
        for (const Flight& flight : flights) {
            flight.print();
            cout << "-------------------" << endl;
        }
    }
};
