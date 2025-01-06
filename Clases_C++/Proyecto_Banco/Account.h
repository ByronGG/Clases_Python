#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account{
    private:
        int id;
        int customerId;

    public:
        Account(int id, int customerId);

        int getId() const;
        int getCustomerId() const;
};


#endif