package com.example;

import com.example.services.PlayerService;
import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Preconditions;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
import java.util.Scanner;
import javax.annotation.processing.Generated;
import javax.inject.Provider;

@ScopeMetadata("javax.inject.Singleton")
@QualifierMetadata
@DaggerGenerated
@Generated(
    value = "dagger.internal.codegen.ComponentProcessor",
    comments = "https://dagger.dev"
)
@SuppressWarnings({
    "unchecked",
    "rawtypes",
    "KotlinInternal",
    "KotlinInternalInJava",
    "cast"
})
public final class AppModule_ProvideMenuFactory implements Factory<Menu> {
  private final AppModule module;

  private final Provider<Scanner> scannerProvider;

  private final Provider<PlayerService> playerServiceProvider;

  public AppModule_ProvideMenuFactory(AppModule module, Provider<Scanner> scannerProvider,
      Provider<PlayerService> playerServiceProvider) {
    this.module = module;
    this.scannerProvider = scannerProvider;
    this.playerServiceProvider = playerServiceProvider;
  }

  @Override
  public Menu get() {
    return provideMenu(module, scannerProvider.get(), playerServiceProvider.get());
  }

  public static AppModule_ProvideMenuFactory create(AppModule module,
      Provider<Scanner> scannerProvider, Provider<PlayerService> playerServiceProvider) {
    return new AppModule_ProvideMenuFactory(module, scannerProvider, playerServiceProvider);
  }

  public static Menu provideMenu(AppModule instance, Scanner scanner, PlayerService playerService) {
    return Preconditions.checkNotNullFromProvides(instance.provideMenu(scanner, playerService));
  }
}
