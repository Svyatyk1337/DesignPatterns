from behavioral.iterator  import MyIterator
from behavioral.command import ConcreteCommand, Receiver
from behavioral.mediator import Component1, Component2, ConcreteMediator
from behavioral.memento import Originator
from behavioral.chain_of_responsibility import ConcreteHandler1, ConcreteHandler2
from behavioral.observer import ConcreteObserver, Subject
from behavioral.state import ConcreteStateA, Context
from behavioral.strategy import ConcreteStrategyA, ContextStrategy
from behavioral.template_method import ConcreteClass
from behavioral.visitor import ConcreteElement, ConcreteVisitor


if __name__ == "__main__":
    # Chain of Responsibility
    handler = ConcreteHandler1(ConcreteHandler2())
    handler.handle("low")
    handler.handle("high")

    # Command
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    command.execute()

    # Iterator
    iterator = MyIterator([1, 2, 3])
    for item in iterator:
        print(item)

    # Mediator
    component1 = Component1()
    component2 = Component2()
    mediator = ConcreteMediator(component1, component2)
    component1.do_a()

    # Memento
    originator = Originator()
    originator.state = "State1"
    memento = originator.save()
    originator.state = "State2"
    originator.restore(memento)
    print("Restored State:", originator.state)

    # Observer
    subject = Subject()
    observer = ConcreteObserver()
    subject.attach(observer)
    subject.notify("Event occurred")

    # State
    context = Context(ConcreteStateA())
    context.request()

    # Strategy
    strategy = ConcreteStrategyA()
    context_strategy = ContextStrategy(strategy)
    context_strategy.execute()

    # Template Method
    template = ConcreteClass()
    template.template_method()

    # Visitor
    visitor = ConcreteVisitor()
    element = ConcreteElement()
    element.accept(visitor)
