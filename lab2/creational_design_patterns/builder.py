from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class ComputerBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of a Computer object.
    """

    @property
    @abstractmethod
    def computer(self) -> None:
        """Return the Computer object."""
        pass

    @abstractmethod
    def build_cpu(self) -> None:
        """Build the CPU component."""
        pass

    @abstractmethod
    def build_ram(self) -> None:
        """Build the RAM component."""
        pass

    @abstractmethod
    def build_storage(self) -> None:
        """Build the storage component."""
        pass

    @abstractmethod
    def build_gpu(self) -> None:
        """Build the GPU component."""
        pass

class GamingComputerBuilder(ComputerBuilder):
    """
    Concrete Builder that constructs Gaming Computer objects.
    """

    def __init__(self) -> None:
        """Initialize a new Gaming Computer Builder."""
        self.reset()

    def reset(self) -> None:
        """Reset the builder to a blank product."""
        self._computer = Computer()

    @property
    def computer(self) -> Computer:
        """Return the constructed Computer object and reset the builder."""
        computer = self._computer
        self.reset()
        return computer

    def build_cpu(self) -> None:
        """Add a high-end CPU to the computer."""
        self._computer.add("Intel Core i9")

    def build_ram(self) -> None:
        """Add ample RAM to the computer."""
        self._computer.add("32GB DDR4")

    def build_storage(self) -> None:
        """Add fast storage to the computer."""
        self._computer.add("1TB NVMe SSD")

    def build_gpu(self) -> None:
        """Add a powerful GPU to the computer."""
        self._computer.add("NVIDIA GeForce RTX 3080")

class OfficeComputerBuilder(ComputerBuilder):
    """
    Concrete Builder that constructs Office Computer objects.
    """

    def __init__(self) -> None:
        """Initialize a new Office Computer Builder."""
        self.reset()

    def reset(self) -> None:
        """Reset the builder to a blank product."""
        self._computer = Computer()

    @property
    def computer(self) -> Computer:
        """Return the constructed Computer object and reset the builder."""
        computer = self._computer
        self.reset()
        return computer

    def build_cpu(self) -> None:
        """Add a mid-range CPU to the computer."""
        self._computer.add("Intel Core i5")

    def build_ram(self) -> None:
        """Add sufficient RAM to the computer."""
        self._computer.add("16GB DDR4")

    def build_storage(self) -> None:
        """Add adequate storage to the computer."""
        self._computer.add("512GB SATA SSD")

    def build_gpu(self) -> None:
        """Add integrated graphics to the computer."""
        self._computer.add("Integrated Graphics")

class Computer:
    """
    Product: Represents the Computer object.
    """

    def __init__(self) -> None:
        """Initialize a new Computer object with an empty parts list."""
        self.parts = []

    def add(self, part: Any) -> None:
        """Add a component to the computer."""
        self.parts.append(part)

    def list_parts(self) -> None:
        """Print the list of components in the computer."""
        print(f"Computer components: {', '.join(self.parts)}", end="")

class ComputerAssembler:
    """
    Director: Manages the construction of Computer objects using a builder.
    """

    def __init__(self) -> None:
        """Initialize a new Computer Assembler."""
        self._builder = None

    @property
    def builder(self) -> ComputerBuilder:
        """Return the current builder."""
        return self._builder

    @builder.setter
    def builder(self, builder: ComputerBuilder) -> None:
        """Set the builder to be used for construction."""
        self._builder = builder

    def build_basic_computer(self) -> None:
        """Construct a basic computer with CPU and RAM."""
        self.builder.build_cpu()
        self.builder.build_ram()

    def build_full_computer(self) -> None:
        """Construct a full computer with all components."""
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()
