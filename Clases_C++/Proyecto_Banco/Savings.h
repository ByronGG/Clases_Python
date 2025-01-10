#ifndef SAVINGS_H
#define SAVINGS_H

#include "Account.h"

class Savings : public Account {
public:
    Savings(int id, int customerId);

    void addInterest();
};

#endif
