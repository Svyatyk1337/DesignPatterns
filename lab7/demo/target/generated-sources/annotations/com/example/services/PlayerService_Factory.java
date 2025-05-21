package com.example.services;

import com.google.gson.Gson;
import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
import javax.annotation.processing.Generated;
import javax.inject.Provider;

@ScopeMetadata
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
public final class PlayerService_Factory implements Factory<PlayerService> {
  private final Provider<String> filePathProvider;

  private final Provider<Gson> gsonProvider;

  public PlayerService_Factory(Provider<String> filePathProvider, Provider<Gson> gsonProvider) {
    this.filePathProvider = filePathProvider;
    this.gsonProvider = gsonProvider;
  }

  @Override
  public PlayerService get() {
    return newInstance(filePathProvider.get(), gsonProvider.get());
  }

  public static PlayerService_Factory create(Provider<String> filePathProvider,
      Provider<Gson> gsonProvider) {
    return new PlayerService_Factory(filePathProvider, gsonProvider);
  }

  public static PlayerService newInstance(String filePath, Gson gson) {
    return new PlayerService(filePath, gson);
  }
}
