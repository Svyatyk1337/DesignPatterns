package ua.edu.chnu.kkn.solid_violation.ocp;

abstract class Employee {
    protected int salary;

    Employee(int salary) {
        this.salary = salary;
    }

    public abstract int payAmount();
}

class Engineer extends Employee {
    Engineer(int salary) {
        super(salary);
    }

    @Override
    public int payAmount() {
        return salary;
    }
}

class Manager extends Employee {
    private int bonus;

    Manager(int salary, int bonus) {
        super(salary);
        this.bonus = bonus;
    }

    @Override
    public int payAmount() {
        return salary + bonus;
    }
}
