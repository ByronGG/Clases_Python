#include "Checking.h"
#include <iostream>

// Constructor
Checking::Checking(int id, int customerId)
    : Account(id, customerId) {}

// Métodos
void Checking::writeCheck() {
    std::cout << "Writing a check...\n";
}
