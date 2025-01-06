#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <string>

class Customer{
    private:
        int id;
        std::string name;
        std::string address;
        int phoneNo;

    public:
        Customer(int id, const std::string& name, const std::string& address, int phoneNo);

    int getId() const;
    std::string getName() const;
    std::string getAddress() const;
    int getPhoneNo() const;
};

#endif