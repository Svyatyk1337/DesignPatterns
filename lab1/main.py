# creational_patterns/main.py

from creational_design_patterns.singleton import AppSettings
from creational_design_patterns.builder import ComputerAssembler, GamingComputerBuilder, OfficeComputerBuilder
from creational_design_patterns.abstract_factory import create_ui, WindowsGUIFactory, MacOSGUIFactory
from creational_design_patterns.prototype import Document
from creational_design_patterns.singleton import AppSettings
from creational_design_patterns.factory_method import CarFactory, BikeFactory, client_code 
import copy
from threading import Thread

def test_singleton():
    """Demonstrates the Singleton pattern."""
    print("\n--- Testing Singleton (AppSettings) ---")
    settings1 = AppSettings("db1", "INFO")
    settings2 = AppSettings()
    print(f"Settings 1: DB={settings1.get_database_url()}, Log={settings1.get_log_level()}")
    print(f"Settings 2: DB={settings2.get_database_url()}, Log={settings2.get_log_level()}")
    print("Singleton works: Both instances have the same settings.")

def test_builder():
    """Demonstrates the Builder pattern."""
    print("\n--- Testing Builder (ComputerAssembler) ---")
    assembler = ComputerAssembler()

    gaming_builder = GamingComputerBuilder()
    assembler.builder = gaming_builder
    assembler.build_full_computer()
    gaming_computer = gaming_builder.computer
    print("Gaming Computer:", ", ".join(gaming_computer.parts))

    office_builder = OfficeComputerBuilder()
    assembler.builder = office_builder
    assembler.build_basic_computer()
    office_computer = office_builder.computer
    print("Office Computer:", ", ".join(office_computer.parts))

def test_abstract_factory():
    """Demonstrates the Abstract Factory pattern."""
    print("\n--- Testing Abstract Factory (GUI) ---")
    print("Windows UI:")
    create_ui(WindowsGUIFactory())
    print("\nmacOS UI:")
    create_ui(MacOSGUIFactory())

def test_prototype():
    """Demonstrates the Prototype pattern."""
    print("\n--- Testing Prototype (Document) ---")
    doc1 = Document("Original", "Content", [])
    doc2 = Document("Related", "Related Content", [doc1])
    doc3 = Document("Main", "Main Content", [doc2])

    shallow_copy_doc3 = copy.copy(doc3)
    deep_copy_doc3 = copy.deepcopy(doc3)

    print("Original:", doc3.title, doc3.content)
    print("Shallow Copy:", shallow_copy_doc3.title, shallow_copy_doc3.content)
    print("Deep Copy:", deep_copy_doc3.title, deep_copy_doc3.content)

def test_thread_safe_singleton():
    """Demonstrates the thread safe singleton pattern."""
    print("\n--- Testing Thread-Safe Singleton (AppSettings) ---")

    def access_settings(thread_name, new_url=None, new_level=None):
        settings = AppSettings()
        print(f"Thread {thread_name}: Database URL: {settings.get_database_url()}, Log Level: {settings.get_log_level()}")
        if new_url:
            settings.set_database_url(new_url)
            print(f"Thread {thread_name}: Updated Database URL to: {settings.get_database_url()}")
        if new_level:
            settings.set_log_level(new_level)
            print(f"Thread {thread_name}: Updated Log Level to: {settings.get_log_level()}")

    thread1 = Thread(target=access_settings, args=("Thread-1", "new_db_url"))
    thread2 = Thread(target=access_settings, args=("Thread-2", None, "DEBUG"))
    thread3 = Thread(target=access_settings, args=("Thread-3",))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("\nSettings access completed.")
    final_settings = AppSettings()
    print(f"Final settings: Database URL: {final_settings.get_database_url()}, Log Level: {final_settings.get_log_level()}")

def test_factory_method():
    """Demonstrates the Factory Method pattern."""
    print("\n--- Testing Factory Method (Transport) ---")
    print("App: Launched with the CarFactory.")
    client_code(CarFactory())
    print("\n")

    print("App: Launched with the BikeFactory.")
    client_code(BikeFactory())
    print("\n")
if __name__ == "__main__":
    test_singleton()
    test_builder()
    test_abstract_factory()
    test_prototype()
    test_factory_method()
