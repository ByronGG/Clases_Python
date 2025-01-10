#ifndef TELLER_H
#define TELLER_H

#include <string>

class Teller {
private:
    int id;
    std::string name;

public:
    Teller(int id, const std::string& name);

    int getId() const;
    std::string getName() const;

    void collectMoney();
    void openAccount();
    void closeAccount();
    void loanRequest();
    void provideInfo();
    void issueCard();
};

#endif
