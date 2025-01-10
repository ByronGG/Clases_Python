#include "Loan.h"
#include <iostream>

// Constructor
Loan::Loan(int id, const std::string& type, int accountId, int customerId)
    : loanId(id), type(type), accountId(accountId), customerId(customerId) {}

// Implementación del método approveLoan
void Loan::approveLoan() {
    std::cout << "Loan ID " << loanId << " of type '" << type 
              << "' for Customer ID " << customerId << " has been approved.\n";
}

// Otros métodos
int Loan::getCustomerId() const {
    return customerId;
}

std::string Loan::getType() const {
    return type;
}
