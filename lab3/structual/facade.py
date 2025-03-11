class CPU:
    def freeze(self):
        return "CPU freezing"

    def jump(self, position):
        return f"CPU jumping to {position}"

    def execute(self):
        return "CPU executing"

class Memory:
    def load(self, position, data):
        return f"Memory loading data '{data}' from position {position}"

class HardDrive:
    def read(self, lba, size):
        return f"HardDrive reading {size} bytes from lba {lba}"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        result = [
            self.cpu.freeze(),
            self.memory.load("0x00", "OS"),
            self.cpu.jump("0x00"),
            self.cpu.execute()
        ]
        return "\n".join(result)