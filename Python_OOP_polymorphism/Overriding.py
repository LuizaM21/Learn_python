"""
It is possible on the inheritance level.
If you have Class A (SUPER class) and class B (CHILD class) and they both have
THE SAME METHOD WITH THE SAME NR AND TYPE OF PARAMETERS AND THE SAME RETURN TYPE AS THE SUPER CLASS
it is called overriding.
It is used to add or extend more to the methods behaviour.
"""


class A:
    def __init__(self, param_1=None):
        if param_1 is None:
            self.param = 0
        self.param = param_1

    def addition(self):
        return self.param


class B(A):

    def addition(self):
        return 1 + self.param


if __name__ == '__main__':

    valueA = A(12)
    print(valueA.addition())

    valueB = B(12)
    print(valueB.addition())


