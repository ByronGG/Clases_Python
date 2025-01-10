#include "Savings.h"
#include <iostream>

// Constructor
Savings::Savings(int id, int customerId)
    : Account(id, customerId) {}

// Métodos
void Savings::addInterest() {
    std::cout << "Adding interest to savings account...\n";
}
