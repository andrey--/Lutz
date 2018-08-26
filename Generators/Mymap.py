
import Homework_functions
def mymap(func, *args):
    res = []
    print (*args)
    for arg in zip(*args):
        res.append(func(*arg))
        print(arg)
    return res


# print(mymap(pow, [3], [2]))
Homework_functions.xxx[0]=['asdasd']
# print(Homework_functions.xxx)
Homework_functions.yyy='Changes'
# Homework_functions.printer()
# Homework_functions.printeryyy()