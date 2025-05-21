package com.example;

import dagger.Module;
import dagger.Provides;

import javax.inject.Named;
import javax.inject.Singleton;
import java.util.Scanner;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

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
    @Named("filePath")
    public String provideFilePath() {
        return "/home/sviatoslav/university/DesignPatterns/lab7/demo/data/players.json";
    }
}