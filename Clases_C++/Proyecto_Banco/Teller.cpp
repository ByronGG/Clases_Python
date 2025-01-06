#include "Teller.h"
#include<iostream>

Teller::Teller(int id, const std::string& name)
    : id(id), name(name){}

int Teller::getId() const{
    return id;
}

std::string Teller::getName() const{
    return name;
}

void Teller::collectMoney(){
    std::cout<<"colleting money...\n";
}

void Teller::openAccount(){
    std::cout<<"Opening accout...\n";
}

void Teller::closeAccount(){
    std::cout<<"Closing account...\n";
}

void Teller::loanRequest(){
    std::cout<<"Processing loan request...\n";
}

void Teller::provideInfo(){
    std::cout<<"Provinf information...\n";
}

void Teller::issueCard(){
    std::cout<<"Issiung card...\n";
}