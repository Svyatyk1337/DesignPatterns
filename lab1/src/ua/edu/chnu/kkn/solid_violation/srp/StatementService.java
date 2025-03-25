package ua.edu.chnu.kkn.solid_violation.srp;


import java.util.LinkedList;
import java.util.List;

import java.util.concurrent.atomic.AtomicInteger;
import static java.util.stream.Collectors.toCollection;

public class StatementService {
    private static final String STATEMENT_HEADER = "DATE | AMOUNT | BALANCE";
    
    
    private Console console;
    private StatementFormatter statementFormatter;

    public StatementService(Console console, StatementFormatter statementFormatter) {
        this.console = console;
        this.statementFormatter = statementFormatter;
    }

    public void printStatement(List<Transaction> transactions) {
        printHeader();
        printTransactions(transactions);
    }

    private void printHeader() {
        printLine(STATEMENT_HEADER);
    }

    private void printTransactions(List<Transaction> transactions) {
        final AtomicInteger balance = new AtomicInteger(0);
        transactions.stream()
            .map(transaction -> statementFormatter.formatStatementLine(transaction, balance.addAndGet(transaction.amount())))
            .collect(toCollection(LinkedList::new))
            .descendingIterator()
            .forEachRemaining(this::printLine);
    }

    private void printLine(String line) {
        console.printLine(line);
    }
}