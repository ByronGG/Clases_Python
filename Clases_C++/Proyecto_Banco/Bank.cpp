#include "Bank.h"
#include <iostream>

// Constructor
Bank::Bank(int id, const std::string& name, const std::string& location)
    : bankId(id), name(name), location(location) {}

// Métodos
int Bank::getBankId() const {
    return bankId;
}

std::string Bank::getName() const {
    return name;
}

std::string Bank::getLocation() const {
    return location;
}

void Bank::addCustomer(const Customer& customer) {
    customers.push_back(customer);
}

void Bank::displayCustomers() const {
    for (const auto& customer : customers) {
        std::cout << "Customer ID: " << customer.getId() 
                  << ", Name: " << customer.getName() << "\n";
    }
}
