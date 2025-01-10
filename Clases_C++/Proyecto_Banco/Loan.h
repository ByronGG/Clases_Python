// Loan.h
#ifndef LOAN_H
#define LOAN_H

#include <string>

class Loan {
private:
    int loanId;
    std::string type;
    int accountId;
    int customerId;

public:
    Loan(int id, const std::string& type, int accountId, int customerId);

    void approveLoan();  // Declaración del método
    int getCustomerId() const;
    std::string getType() const;
};

#endif
