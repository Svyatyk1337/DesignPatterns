package ua.edu.chnu.kkn.solid_violation.ocp;

public class EngineerEmployee extends Employee {
    EngineerEmployee(int salary) {
        super(salary);
    }
    
    @Override
    public int payAmount() {
        return salary;
    }
}