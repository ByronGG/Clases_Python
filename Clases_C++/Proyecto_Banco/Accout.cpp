#include "Account.h"

// Constructor
Account::Account(int id, int customerId)
    : id(id), customerId(customerId) {}

// Métodos
int Account::getId() const {
    return id;
}

int Account::getCustomerId() const {
    return customerId;
}
