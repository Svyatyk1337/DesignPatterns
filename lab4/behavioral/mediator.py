class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self.component1 = component1
        self.component2 = component2
        self.component1.mediator = self
        self.component2.mediator = self
    
    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers B.")
            self.component2.do_b()

class Component:
    def __init__(self, mediator=None):
        self.mediator = mediator

class Component1(Component):
    def do_a(self):
        print("Component1 does A.")
        self.mediator.notify(self, "A")

class Component2(Component):
    def do_b(self):
        print("Component2 does B.")