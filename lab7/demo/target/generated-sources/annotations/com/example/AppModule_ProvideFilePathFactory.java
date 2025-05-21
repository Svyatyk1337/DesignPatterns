package com.example;

import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Preconditions;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
import javax.annotation.processing.Generated;

@ScopeMetadata("javax.inject.Singleton")
@QualifierMetadata("javax.inject.Named")
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
public final class AppModule_ProvideFilePathFactory implements Factory<String> {
  private final AppModule module;

  public AppModule_ProvideFilePathFactory(AppModule module) {
    this.module = module;
  }

  @Override
  public String get() {
    return provideFilePath(module);
  }

  public static AppModule_ProvideFilePathFactory create(AppModule module) {
    return new AppModule_ProvideFilePathFactory(module);
  }

  public static String provideFilePath(AppModule instance) {
    return Preconditions.checkNotNullFromProvides(instance.provideFilePath());
  }
}
