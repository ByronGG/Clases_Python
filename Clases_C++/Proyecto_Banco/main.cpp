#include <iostream>
#include "Bank.h"
#include "Customer.h"
#include "Teller.h"
#include "Account.h"
#include "Checking.h"
#include "Savings.h"
#include "Loan.h"

int main() {
    // Crear un banco
    Bank bank(1, "Global Bank", "123 Main Street");
    std::cout << "Bank created: " << bank.getName() << " at " << bank.getLocation() << "\n";

    // Crear algunos clientes
    Customer customer1(101, "Alice Johnson", "456 Elm Street", 1234567890);
    Customer customer2(102, "Bob Smith", "789 Oak Avenue", 9876543210);

    // Agregar clientes al banco
    bank.addCustomer(customer1);
    bank.addCustomer(customer2);

    // Mostrar clientes
    std::cout << "Customers in the bank:\n";
    bank.displayCustomers();

    // Crear cuentas
    Checking checkingAccount(201, customer1.getId());
    Savings savingsAccount(202, customer2.getId());

    std::cout << "\nChecking account created for customer ID: " << checkingAccount.getCustomerId() << "\n";
    std::cout << "Savings account created for customer ID: " << savingsAccount.getCustomerId() << "\n";

    // Operaciones de cuentas
    checkingAccount.writeCheck();
    savingsAccount.addInterest();

    // Crear un cajero (Teller)
    Teller teller1(301, "John Doe");
    std::cout << "\nTeller created: " << teller1.getName() << "\n";

    // Operaciones del cajero
    teller1.openAccount();
    teller1.collectMoney();
    teller1.issueCard();

    // Crear un préstamo
    Loan loan1(401, "Home Loan", checkingAccount.getId(), customer1.getId());
    std::cout << "\nLoan created for customer ID: " << loan1.getCustomerId() << " of type: " << loan1.getType() << "\n";
    loan1.approveLoan();

    // Fin del programa
    std::cout << "\nBank system operations completed.\n";
    return 0;
}
