package ua.edu.chnu.kkn.solid_violation.isp;

public class Dog implements Runnable, Barkable {
    @Override
    public void run() {
        System.out.print("Dog is running");
    }

    @Override
    public void bark() {
        System.out.print("Dog is barking");
    }
}