class Visitor:
    def visit(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit(self, element):
        print("Visited", element.__class__.__name__)

class Element:
    def accept(self, visitor):
        visitor.visit(self)

class ConcreteElement(Element):
    pass