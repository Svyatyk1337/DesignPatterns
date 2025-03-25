package ua.edu.chnu.kkn.solid_violation.srp;



public class TransactionService {
    private Clock clock;

    public TransactionService(Clock clock) {
        this.clock = clock;
    }

    public Transaction createTransaction(int amount) {
        return new Transaction(clock.today(), amount);
    }
}