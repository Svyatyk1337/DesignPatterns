package com.example;

import com.example.services.PlayerService;
import com.google.gson.Gson;
import dagger.internal.DaggerGenerated;
import dagger.internal.DoubleCheck;
import dagger.internal.Preconditions;
import dagger.internal.Provider;
import java.util.Scanner;
import javax.annotation.processing.Generated;

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
public final class DaggerAppComponent {
  private DaggerAppComponent() {
  }

  public static Builder builder() {
    return new Builder();
  }

  public static AppComponent create() {
    return new Builder().build();
  }

  public static final class Builder {
    private AppModule appModule;

    private Builder() {
    }

    public Builder appModule(AppModule appModule) {
      this.appModule = Preconditions.checkNotNull(appModule);
      return this;
    }

    public AppComponent build() {
      if (appModule == null) {
        this.appModule = new AppModule();
      }
      return new AppComponentImpl(appModule);
    }
  }

  private static final class AppComponentImpl implements AppComponent {
    private final AppComponentImpl appComponentImpl = this;

    private Provider<Scanner> provideScannerProvider;

    private Provider<String> provideFilePathProvider;

    private Provider<Gson> provideGsonProvider;

    private AppComponentImpl(AppModule appModuleParam) {

      initialize(appModuleParam);

    }

    private PlayerService playerService() {
      return new PlayerService(provideFilePathProvider.get(), provideGsonProvider.get());
    }

    @SuppressWarnings("unchecked")
    private void initialize(final AppModule appModuleParam) {
      this.provideScannerProvider = DoubleCheck.provider(AppModule_ProvideScannerFactory.create(appModuleParam));
      this.provideFilePathProvider = DoubleCheck.provider(AppModule_ProvideFilePathFactory.create(appModuleParam));
      this.provideGsonProvider = DoubleCheck.provider(AppModule_ProvideGsonFactory.create(appModuleParam));
    }

    @Override
    public Menu getMenu() {
      return new Menu(provideScannerProvider.get(), playerService());
    }
  }
}
