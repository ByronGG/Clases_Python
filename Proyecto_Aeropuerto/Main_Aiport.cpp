#include <iostream>
#include "Airport.cpp"
using namespace std;

int main() {
    // Crear una hora local
    LocalTime time1;
    time1.set_time(10, 30); // 10:30 AM

    // Crear un vuelo
    Flight flight1("ABC123", "New York", "Gate 5", "Check-In 1", time1);
    flight1.set_comment("departure");

    // Crear un aeropuerto
    Airport airport("International Airport");
    airport.schedule(flight1);

    // Agregar comentarios y retrasar el vuelo
    airport.comment("ABC123", "Delayed due to weather");
    airport.delay("ABC123", 60); // Retrasar 1 hora

    // Imprimir información del aeropuerto
    airport.print();

    return 0;
}
