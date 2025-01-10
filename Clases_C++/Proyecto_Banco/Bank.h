#ifndef BANK_H
#define BANK_H

#include <string>
#include <vector>
#include "Customer.h"

class Bank {
private:
    int bankId;
    std::string name;
    std::string location;
    std::vector<Customer> customers;

public:
    Bank(int id, const std::string& name, const std::string& location);

    int getBankId() const;
    std::string getName() const;
    std::string getLocation() const;

    void addCustomer(const Customer& customer);
    void displayCustomers() const;
};

#endif
