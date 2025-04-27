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

    private Provider<Gson> provideGsonProvider;

    private Provider<PlayerService> providePlayerServiceProvider;

    private Provider<Menu> provideMenuProvider;

    private AppComponentImpl(AppModule appModuleParam) {

      initialize(appModuleParam);

    }

    @SuppressWarnings("unchecked")
    private void initialize(final AppModule appModuleParam) {
      this.provideScannerProvider = DoubleCheck.provider(AppModule_ProvideScannerFactory.create(appModuleParam));
      this.provideGsonProvider = DoubleCheck.provider(AppModule_ProvideGsonFactory.create(appModuleParam));
      this.providePlayerServiceProvider = DoubleCheck.provider(AppModule_ProvidePlayerServiceFactory.create(appModuleParam, provideGsonProvider));
      this.provideMenuProvider = DoubleCheck.provider(AppModule_ProvideMenuFactory.create(appModuleParam, provideScannerProvider, providePlayerServiceProvider));
    }

    @Override
    public Menu getMenu() {
      return provideMenuProvider.get();
    }
  }
}
