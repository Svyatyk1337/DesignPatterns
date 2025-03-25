package ua.edu.chnu.kkn.solid_violation.dip;

import java.time.MonthDay;

public class BirthdayGreeter {
    private final EmployeeRepository employeeRepository;
    private final TimeProvider timeProvider;
    private final EmailService emailService;

    public BirthdayGreeter(
        EmployeeRepository employeeRepository, 
        TimeProvider timeProvider, 
        EmailService emailService
    ) {
        this.employeeRepository = employeeRepository;
        this.timeProvider = timeProvider;
        this.emailService = emailService;
    }

    public void sendGreetings() {
        MonthDay today = timeProvider.getCurrentMonthDay();
        employeeRepository.findEmployeesBornOn(today)
                .stream()
                .map(this::emailFor)
                .forEach(emailService::send);
    }

    private Email emailFor(Employee employee) {
        String message = String.format("Happy birthday, dear %s!", employee.getFirstName());
        return new Email(employee.getEmail(), "Happy birthday!", message);
    }
}