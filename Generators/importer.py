def reclist(instance):
    valueToReturn = instance.__class__.__qualname__ + "\n"
    for elem in instance.__dict__:
        valueToReturn += "{0}={1}\n".format(elem, getattr(instance, elem))
    return valueToReturn


class clas1:
    rrrrr = 1

    def __str__(self):
        return reclist(self)

    def aaa(self):
        pass

    def __init__(self):
        self.fff = 5
        self.new = 123


asd = clas1()
asd.ppp = 56
asd.iii = lambda r: r + 10
print(asd)
print(clas1)
# asd.ppp=56
# def asdsada():
#     pass
