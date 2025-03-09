from __future__ import annotations
from abc import ABC, abstractmethod

class GUIFactory(ABC):
    """
    Abstract Factory: Defines the interface for creating families of related objects.
    """
    @abstractmethod
    def create_button(self) -> Button:
        """Creates a Button object."""
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        """Creates a TextBox object."""
        pass

class WindowsGUIFactory(GUIFactory):
    """
    Concrete Factory: Creates Windows-specific GUI objects.
    """
    def create_button(self) -> Button:
        """Creates a Windows Button."""
        return WindowsButton()

    def create_textbox(self) -> TextBox:
        """Creates a Windows TextBox."""
        return WindowsTextBox()

class MacOSGUIFactory(GUIFactory):
    """
    Concrete Factory: Creates macOS-specific GUI objects.
    """
    def create_button(self) -> Button:
        """Creates a macOS Button."""
        return MacOSButton()

    def create_textbox(self) -> TextBox:
        """Creates a macOS TextBox."""
        return MacOSTextBox()

class Button(ABC):
    """
    Abstract Product: Defines the interface for Button objects.
    """
    @abstractmethod
    def render(self) -> str:
        """Renders the Button."""
        pass

class WindowsButton(Button):
    """
    Concrete Product: Windows Button.
    """
    def render(self) -> str:
        """Renders a Windows Button."""
        return "Windows Button"

class MacOSButton(Button):
    """
    Concrete Product: macOS Button.
    """
    def render(self) -> str:
        """Renders a macOS Button."""
        return "macOS Button"

class TextBox(ABC):
    """
    Abstract Product: Defines the interface for TextBox objects.
    """
    @abstractmethod
    def render(self) -> str:
        """Renders the TextBox."""
        pass

class WindowsTextBox(TextBox):
    """
    Concrete Product: Windows TextBox.
    """
    def render(self) -> str:
        """Renders a Windows TextBox."""
        return "Windows TextBox"

class MacOSTextBox(TextBox):
    """
    Concrete Product: macOS TextBox.
    """
    def render(self) -> str:
        """Renders a macOS TextBox."""
        return "macOS TextBox"

def create_ui(factory: GUIFactory) -> None:
    """
    Client Code: Uses the factory to create UI elements.
    """
    button = factory.create_button()
    textbox = factory.create_textbox()

    print(button.render())
    print(textbox.render())

