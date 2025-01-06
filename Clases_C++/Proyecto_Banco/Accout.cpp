#include "Account.h"

Account::Account(int id, int customerId)
    : id(id), customerId(customerId){}

int Account::getId() const{
    return id;
}

int Account::getCustomerId() const{
    return customerId;
}