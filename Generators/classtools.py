#Common class to implement different tools for any class
class AttrDisplay:
    def gatherAttrs(self):
        attrs =  []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def gatherClassTree(self):
        classChain=''
        if len(self.__class__.__bases__)==1 and self.__class__.__bases__[0]=="<class 'object'>":
            return classChain + self.__class__.__bases__[0]
        else:
            for i in 


    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__=='__main__':
    class TopTest(AttrDisplay):
        count=0
        def __init__(self):
            self.attr1=TopTest.count
            self.attr2=TopTest.count+1
            TopTest.count+=2
    class SubTest(TopTest):
        pass
    class Third(SubTest):
        pass

    X, Y = TopTest(), SubTest()
    # print (X)
    # print (Y)
    z=Third()
    # print(Y.__class__.__bases__)
    f=AttrDisplay()
    # print(z.__class__.__bases__)
    print(f.__class__.__bases__[0])
    # z=X.__class__.__bases__[0]
    # print(z.__class__.__name__)
    # for i in Y.__class__.__bases__:
    #     print(i.__name__)