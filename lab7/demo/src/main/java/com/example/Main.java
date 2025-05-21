package com.example;

public class Main {

    public static void main(String[] args) {
        AppComponent appComponent = DaggerAppComponent.create();
        Menu menu = appComponent.getMenu();
        menu.start();
    }
}
