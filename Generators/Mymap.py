def mymap(func, *args):
    res = []
    print (*args)
    for arg in zip(*args):
        res.append(func(*arg))
        print(arg)
    return res


print(mymap(pow, [3], [2]))
