def countLines(name):
    fileList=open(name, "r").readlines()
    # print(fileList)
    print(len(fileList))


def countChars(name):
    fileList = open(name, "r").read()
    # print(fileList)
    print(len(fileList))


def test():
    countChars("mymod.py")
    countLines("mymod.py")


if __name__=='__main__':
    test() 1
