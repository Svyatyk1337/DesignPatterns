package com.example;

import com.example.services.PlayerService;
import com.google.gson.Gson;
import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Preconditions;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
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
public final class AppModule_ProvidePlayerServiceFactory implements Factory<PlayerService> {
  private final AppModule module;

  private final Provider<Gson> gsonProvider;

  public AppModule_ProvidePlayerServiceFactory(AppModule module, Provider<Gson> gsonProvider) {
    this.module = module;
    this.gsonProvider = gsonProvider;
  }

  @Override
  public PlayerService get() {
    return providePlayerService(module, gsonProvider.get());
  }

  public static AppModule_ProvidePlayerServiceFactory create(AppModule module,
      Provider<Gson> gsonProvider) {
    return new AppModule_ProvidePlayerServiceFactory(module, gsonProvider);
  }

  public static PlayerService providePlayerService(AppModule instance, Gson gson) {
    return Preconditions.checkNotNullFromProvides(instance.providePlayerService(gson));
  }
}
