package com.example;

import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Preconditions;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
import java.util.Scanner;
import javax.annotation.processing.Generated;

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
public final class AppModule_ProvideScannerFactory implements Factory<Scanner> {
  private final AppModule module;

  public AppModule_ProvideScannerFactory(AppModule module) {
    this.module = module;
  }

  @Override
  public Scanner get() {
    return provideScanner(module);
  }

  public static AppModule_ProvideScannerFactory create(AppModule module) {
    return new AppModule_ProvideScannerFactory(module);
  }

  public static Scanner provideScanner(AppModule instance) {
    return Preconditions.checkNotNullFromProvides(instance.provideScanner());
  }
}
