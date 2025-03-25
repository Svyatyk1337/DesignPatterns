package ua.edu.chnu.kkn.solid_violation.dip;

public class ConsoleEmailSender implements EmailService {
    @Override
    public void send(Email email) {
        System.out.println(
            "To: " + email.getTo() + 
            ", Subject: " + email.getSubject() + 
            ", Message: " + email.getMessage()
        );
    }
}