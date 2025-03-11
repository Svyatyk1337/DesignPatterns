from structual import adapter, bridge, composite, decorator, facade, flyweight, proxy

# Adapter
adaptee = adapter.Adaptee()
target = adapter.Adapter(adaptee)
print("Adapter:", target.request())

# Bridge
red_circle = bridge.Circle(bridge.RedColor())
blue_square = bridge.Square(bridge.BlueColor())
print("Bridge:", red_circle.draw())
print("Bridge:", blue_square.draw())

# Composite
mouse = composite.Leaf("Mouse", 100)
keyboard = composite.Leaf("Keyboard", 200)
monitor = composite.Leaf("Monitor", 500)
computer = composite.Composite("Computer")
computer.add_component(mouse)
computer.add_component(keyboard)
computer.add_component(monitor)
print("Composite:", computer.show_price())

# Decorator
coffee = decorator.Coffee()
coffee = decorator.MilkDecorator(coffee)
coffee = decorator.SugarDecorator(coffee)
print("Decorator:", coffee.get_description())
print("Decorator:", coffee.get_cost())

# Facade
computer = facade.ComputerFacade()
print("Facade:", computer.start_computer())

# Flyweight
factory = flyweight.CharacterFactory()
a = factory.get_character('a')
b = factory.get_character('b')
a2 = factory.get_character('a')
print("Flyweight:", a.display(1, 1))
print("Flyweight:", b.display(2, 2))
print("Flyweight:", a2.display(3, 3))

# Proxy
real_subject = proxy.RealSubject()
proxy_instance = proxy.Proxy(real_subject)
print("Proxy:", proxy_instance.request())