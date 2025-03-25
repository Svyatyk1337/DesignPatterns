class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Strategy A executed")

class ContextStrategy:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def execute(self):
        self.strategy.execute()