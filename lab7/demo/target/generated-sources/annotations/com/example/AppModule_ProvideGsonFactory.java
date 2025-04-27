package com.example;

import com.google.gson.Gson;
import dagger.internal.DaggerGenerated;
import dagger.internal.Factory;
import dagger.internal.Preconditions;
import dagger.internal.QualifierMetadata;
import dagger.internal.ScopeMetadata;
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
public final class AppModule_ProvideGsonFactory implements Factory<Gson> {
  private final AppModule module;

  public AppModule_ProvideGsonFactory(AppModule module) {
    this.module = module;
  }

  @Override
  public Gson get() {
    return provideGson(module);
  }

  public static AppModule_ProvideGsonFactory create(AppModule module) {
    return new AppModule_ProvideGsonFactory(module);
  }

  public static Gson provideGson(AppModule instance) {
    return Preconditions.checkNotNullFromProvides(instance.provideGson());
  }
}
