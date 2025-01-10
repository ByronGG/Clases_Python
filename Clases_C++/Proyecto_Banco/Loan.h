#ifndef LOAN_H
#define LOAN_H

#include <string>

class Loan {
private:
    int id;
    std::string type;
    int accountId;
    int customerId;

public:
    Loan(int id, const std::string& type, int accountId, int customerId);

    int getId() const;
    std::string getType() const;
    int getAccountId() const;
    int getCustomerId() const;

    void approveLoan();
};

#endif
