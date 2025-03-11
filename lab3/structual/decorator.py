class Coffee:
    def get_description(self):
        return "Simple coffee"

    def get_cost(self):
        return 1.0

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_description(self):
        return self.coffee.get_description()

    def get_cost(self):
        return self.coffee.get_cost()

class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return super().get_description() + ", milk"

    def get_cost(self):
        return super().get_cost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        return super().get_description() + ", sugar"

    def get_cost(self):
        return super().get_cost() + 0.2