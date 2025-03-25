package ua.edu.chnu.kkn.solid_violation.ocp;

public abstract class Employee {
    protected int salary;
    
    Employee(int salary) {
        this.salary = salary;
    }
    
    public abstract int payAmount();
}