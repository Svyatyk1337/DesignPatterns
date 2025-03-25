class Handler:
    def __init__(self, successor=None):
        self.successor = successor
    
    def handle(self, request):
        if self.successor:
            self.successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == "low":
            print("Handler1 handled request")
        elif self.successor:
            self.successor.handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == "high":
            print("Handler2 handled request")
        elif self.successor:
            self.successor.handle(request)