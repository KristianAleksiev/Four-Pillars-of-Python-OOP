class A:
    def method(self):
        print("Belongs to class A")


class B(A):
    def method(self):
        print("Belongs to class B")


class C(A):
    def method(self):
        print("Belongs to class C")


class D(B,C): # => Method resolution order
    pass


d = D()
d.method()



