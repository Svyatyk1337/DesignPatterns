class Resource:
    def __init__(self):
        print("creating an external resource")

    def __enter__(self):
        return self

    def op1(self):
        print("op1")
        return self

    def op2(self):
        print("op2")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("cleaning up external resource")


def use(block):
    with Resource() as resource:
        block(resource)


def main():
    use(lambda resource: resource.op1().op2())


if __name__ == "__main__":
    main()
