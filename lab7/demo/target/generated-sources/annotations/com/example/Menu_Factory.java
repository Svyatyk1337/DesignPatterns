package com.example;

import com.example.services.PlayerService;
import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
import java.util.Scanner;
import javax.annotation.processing.Generated;
import javax.inject.Provider;

@ScopeMetadata
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
public final class Menu_Factory implements Factory<Menu> {
  private final Provider<Scanner> scannerProvider;

  private final Provider<PlayerService> playerServiceProvider;

  public Menu_Factory(Provider<Scanner> scannerProvider,
      Provider<PlayerService> playerServiceProvider) {
    this.scannerProvider = scannerProvider;
    this.playerServiceProvider = playerServiceProvider;
  }

  @Override
  public Menu get() {
    return newInstance(scannerProvider.get(), playerServiceProvider.get());
  }

  public static Menu_Factory create(Provider<Scanner> scannerProvider,
      Provider<PlayerService> playerServiceProvider) {
    return new Menu_Factory(scannerProvider, playerServiceProvider);
  }

  public static Menu newInstance(Scanner scanner, PlayerService playerService) {
    return new Menu(scanner, playerService);
  }
}
