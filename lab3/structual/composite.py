class Component:
    def show_price(self):
        pass

class Leaf(Component):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_price(self):
        return f"{self.name} : {self.price}"

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def show_price(self):
        result = [f"{self.name} :"]
        for component in self.components:
            result.append(component.show_price())
        return "\n".join(result)