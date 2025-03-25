class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("State A handling request.")

class Context:
    def __init__(self, state):
        self.state = state
    
    def request(self):
        self.state.handle()