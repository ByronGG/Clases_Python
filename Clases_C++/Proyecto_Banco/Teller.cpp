#include "Teller.h"
#include <iostream>

// Constructor
Teller::Teller(int id, const std::string& name)
    : id(id), name(name) {}

// Métodos
int Teller::getId() const {
    return id;
}

std::string Teller::getName() const {
    return name;
}

void Teller::collectMoney() {
    std::cout << "Collecting money...\n";
}

void Teller::openAccount() {
    std::cout << "Opening account...\n";
}

void Teller::closeAccount() {
    std::cout << "Closing account...\n";
}

void Teller::loanRequest() {
    std::cout << "Processing loan request...\n";
}

void Teller::provideInfo() {
    std::cout << "Providing information...\n";
}

void Teller::issueCard() {
    std::cout << "Issuing card...\n";
}
