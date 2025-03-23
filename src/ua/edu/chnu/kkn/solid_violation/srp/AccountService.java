package ua.edu.chnu.kkn.solid_violation.srp;

import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class AccountService {
    private TransactionRepository transactionRepository;
    private Clock clock;

    public AccountService(TransactionRepository transactionRepository, Clock clock) {
        this.transactionRepository = transactionRepository;
        this.clock = clock;
    }

    public void deposit(int amount) {
        transactionRepository.add(transactionWith(amount));
    }

    public void withdraw(int amount) {
        transactionRepository.add(transactionWith(-amount));
    }

    public List<StatementLine> getStatement() {
        List<Transaction> transactions = transactionRepository.all();
        AtomicInteger balance = new AtomicInteger(0);
        return transactions.stream()
                .map(transaction -> new StatementLine(transaction, balance.addAndGet(transaction.amount())))
                .collect(Collectors.toList());
    }

    private Transaction transactionWith(int amount) {
        return new Transaction(clock.today(), amount);
    }
}

class StatementPrinter {
    private static final String STATEMENT_HEADER = "DATE | AMOUNT | BALANCE";

    private Console console;

    public StatementPrinter(Console console) {
        this.console = console;
    }

    public void print(List<StatementLine> statementLines) {
        console.printLine(STATEMENT_HEADER);
        statementLines.stream()
                .map(StatementLine::toString)
                .forEach(console::printLine);
    }
}

class StatementLine {
    private Transaction transaction;
    private int balance;

    public StatementLine(Transaction transaction, int balance) {
        this.transaction = transaction;
        this.balance = balance;
    }

    @Override
    public String toString() {
        return String.format("%s | %d | %d", transaction.date(), transaction.amount(), balance);
    }
}
