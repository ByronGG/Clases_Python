#ifndef CHECKING_H
#define CHECKING_H

#include "Account.h"

class Checking : public Account{
    public:
        Checking(int id, int customerId);
        
        void writeCheck();
};

#endif