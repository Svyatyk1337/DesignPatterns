from threading import Lock, Thread

class AppSettingsMeta(type):
    """
    Thread-safe implementation of Singleton for AppSettings.
    """

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class AppSettings(metaclass=AppSettingsMeta):
    """
    Singleton class for application settings.
    """

    def __init__(self, database_url="default_url", log_level="INFO"):
        self.database_url = database_url
        self.log_level = log_level

    def get_database_url(self):
        """
        Returns the database URL.
        """
        return self.database_url

    def set_database_url(self, url):
        """
        Sets the database URL.
        """
        self.database_url = url

    def get_log_level(self):
        """
        Returns the log level.
        """
        return self.log_level

    def set_log_level(self, level):
        """
        Sets the log level.
        """
        self.log_level = level

def access_settings(thread_name, new_url=None, new_level=None):
    """
    Simulates accessing and modifying application settings from different threads.
    """
    settings = AppSettings()  # Get the singleton instance

    print(f"Thread {thread_name}: Database URL: {settings.get_database_url()}, Log Level: {settings.get_log_level()}")

    if new_url:
        settings.set_database_url(new_url)
        print(f"Thread {thread_name}: Updated Database URL to: {settings.get_database_url()}")

    if new_level:
        settings.set_log_level(new_level)
        print(f"Thread {thread_name}: Updated Log Level to: {settings.get_log_level()}")

