#include "Customer.h"

// Construtor
Customer::Customer(int id, const std::string& name, const std::string& address, int phoneNo)
    : id(id), name(name), address(address), phoneNo(phoneNo){}

// Métodos
int Customer::getId() const{
    return id;
}

std::string Customer::getName() const{
    return name;
}

std::string Customer::getAddress() const{
    return address;
}

int Customer::getPhoneNo() const{
    return phoneNo;
}