def simple_decorator(func):
    def wrapper():
        print()
        func()
        print()
    return wrapper

@simple_decorator
def say_hello():
    print("Hello World")

say_hello()


