package ua.edu.chnu.kkn.solid_violation.isp;

public class Dog implements Animal {
    @Override
    public void run() {
        System.out.print("Dog is running");
    }

    public void bark() {
        System.out.print("Dog is barking");
    }
}
