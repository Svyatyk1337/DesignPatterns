package com.example;

import dagger.Module;
import dagger.Provides;
import javax.inject.Singleton;
import java.util.Scanner;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.example.services.PlayerService;

@Module
public class AppModule {

    @Provides
    @Singleton
    public Scanner provideScanner() {
        return new Scanner(System.in);
    }

    @Provides
    @Singleton
    public Gson provideGson() {
        return new GsonBuilder().setPrettyPrinting().create();
    }

    @Provides
    @Singleton
    public PlayerService providePlayerService(Gson gson) {
        String filePath = "/home/sviatoslav/university/DesignPatterns/lab7/demo/data/players.json";
        return new PlayerService(filePath, gson);
    }

    @Provides
    @Singleton
    public Menu provideMenu(Scanner scanner, PlayerService playerService) {
        return new Menu(scanner, playerService);
    }
}