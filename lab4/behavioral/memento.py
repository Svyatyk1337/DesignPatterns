class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self):
        self.state = ""
    
    def save(self):
        return Memento(self.state)
    
    def restore(self, memento):
        self.state = memento.state