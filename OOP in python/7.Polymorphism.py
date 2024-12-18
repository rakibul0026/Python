from lamda_function import calculate


class A:
    def print(self):
        print("Here is A")
# Run-Time Polymorphism: Method Overriding
class B(A):
    def print(self):
        print("here is B")
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

ob=B()
ob.print()

# Compile-Time Polymorphism
ob2=Calculator()
print(ob2.add(2,3,5))
print(ob2.add(2,5))
print(ob2.add(2))

