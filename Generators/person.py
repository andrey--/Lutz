import classtools
class Person(classtools.AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    # def __str__(self):
    #     return '[%s: %s, %s]'%(self.__class__.__name__, self.name, self.pay)

    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay=int(self.pay*(1+percent))


class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)
    # def anotherOne(self):
    #     print("PPPP")
    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)
class ttt(Person):
    def giveRaise(self, a):
        self.pay=10
    # def __str__(self):
    #     return '[PAY: %s]'%(self.pay)

if __name__=='__main__':
    bob=Person("Bob", pay=1000)
    sue=Person("Sue", job="Engineer")
    tom=Manager("Tom jr", 50000)
andrey=ttt('andrey')
def test(*employees):
    for employee in employees:
        employee.giveRaise(.10)
        print(employee)
test(tom, bob, sue, andrey)
