class Adaptee:
    def specific_request(self):
        return "Adaptee's specific request"

class Target:
    def request(self):
        pass

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()