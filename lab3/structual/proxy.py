class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        if self.check_access():
            return self.real_subject.request()
        else:
            return "Proxy: Access denied."

    def check_access(self):
        return True