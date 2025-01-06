#include "Checking.h"
#include <iostream>

Checking::Checking(int id, int customerId)
    : Account(id, customerId){}

void Checking::writeCheck(){
    std::cout<<"Writting a check...\n";
}