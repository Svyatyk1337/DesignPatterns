package ua.edu.chnu.kkn.solid_violation.srp;

public class AccountService {
    private TransactionRepository transactionRepository;
    private TransactionService transactionService;
    private StatementService statementService;

    public AccountService(
        TransactionRepository transactionRepository, 
        TransactionService transactionService, 
        StatementService statementService
    ) {
        this.transactionRepository = transactionRepository;
        this.transactionService = transactionService;
        this.statementService = statementService;
    }

    public void deposit(int amount) {
        Transaction transaction = transactionService.createTransaction(amount);
        transactionRepository.add(transaction);
    }

    public void withdraw(int amount) {
        Transaction transaction = transactionService.createTransaction(-amount);
        transactionRepository.add(transaction);
    }

    public void printStatement() {
        statementService.printStatement(transactionRepository.all());
    }
}