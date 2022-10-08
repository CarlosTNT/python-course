# functions

from html.entities import name2codepoint


def hello(name="person"):
    print(f"hello world {name}")


hello("Joe")
hello("carlos")
hello()

def add(n1,n2):
    return n1 + n2

print(add(28,2))

# lambda

add = lambda n1,n2: n1+n2

print(add(15,45))
