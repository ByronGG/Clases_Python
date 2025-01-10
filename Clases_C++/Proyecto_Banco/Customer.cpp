// Customer.cpp
#include "Customer.h"

Customer::Customer(int id, const std::string& name, const std::string& address, const std::string& contact)
    : id(id), name(name), address(address), contact(contact) {}

int Customer::getId() const { return id; }
std::string Customer::getName() const { return name; }
std::string Customer::getAddress() const { return address; }
std::string Customer::getContact() const { return contact; }
