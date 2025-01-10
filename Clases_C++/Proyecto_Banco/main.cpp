#include <iostream>
#include "Bank.h"
#include "Customer.h"
#include "Teller.h"
#include "Account.h"
#include "Checking.h"
#include "Saving.h"
#include "Loan.h"


int main(){
    //Crear un banco
    Bank bank(1, "Santander", "Avenida Hidalgo 450");
    std::cout<<"Banco creado: "<< bank.getName() << " en "<< bank.getLocation() <<"\n";



    return 0;
}