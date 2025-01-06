#include "Bank.h"
#include <iostream>


// Construtor
Bank::Bank(int id, const std::string& name, const std::string& location)
    : bankId(id), name(name), location(location){}

int Bank::getBankid() const{
    return bankId;
}

std::string Bank::getName() const{
    return name;
}

std::string Bank::getLocation() const{
    return location;
}

void Bank::addCustomer(const Customer& customer){
    customers.push_back(customer);
}

void Bank::displayCustomer() const{
    for(const auto& customer : customers){
        std::cout<<"Customer ID: "<<customer.getId()
            <<", Name: "<<customer.getName()<<"\n";
    }
}
