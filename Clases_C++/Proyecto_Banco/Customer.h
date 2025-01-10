// Customer.h
#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <string>

class Customer {
private:
    int id;
    std::string name;
    std::string address;
    std::string contact;  // Cambiar de int a std::string

public:
    Customer(int id, const std::string& name, const std::string& address, const std::string& contact);

    int getId() const;
    std::string getName() const;
    std::string getAddress() const;
    std::string getContact() const;
};

#endif
