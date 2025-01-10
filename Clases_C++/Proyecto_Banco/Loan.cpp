#include "Loan.h"
#include <iostream>

// Constructor
Loan::Loan(int id, const std::string& type, int accountId, int customerId)
    : id(id), type(type), accountId(accountId), customerId(customerId) {}

// Métodos
int Loan::getId() const {
    return id;
}

std::string Loan::getType() const {
    return type;
}

int Loan::getAccountId() const {
    return accountId;
}

int Loan::getCustomerId() const {
    return customerId;
}

void Loan::approveLoan() {
    std::cout << "Loan approved for customer ID: " << customerId << "\n";
}
