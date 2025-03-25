class AbstractClass:
    def template_method(self):
        self.step_one()
        self.step_two()
    
    def step_one(self):
        pass
    
    def step_two(self):
        pass

class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Step One Implemented")
    
    def step_two(self):
        print("Step Two Implemented")