from math import sqrt


def adder(*x):
    if len(x)==0 : return
    summ=x[0]
    temp=x[1:]
    print(type(x))
    print(*x)
    # print(type(summ))
    # print(summ)
    for i in temp:
        summ+=i
    return summ

def adder_name(**x):
    if len(x) == 0: return "Fuck"
    temp=list(x.keys())
    summ=x[temp[0]]
    temp=temp[1:]
        # print(type(x))
    # print(*x)
    # # print(type(summ))
    # # print(summ)
    #
    for i in temp:
         summ+=x[i]
    return summ

def copyDict(dict):
    # if len(dict) == 0: return "Fuck"
    temp = list(dict.keys())
    summ ={}
    for i in temp:
         summ[i]=dict[i]
    print(type(summ))
    return summ
# print (adder(1,2))
def addDict(dict1, dict2):
    if (type(dict1)==list) and (type(dict2)==list):
        return dict1+dict2
    if (type(dict1)!=list) or (type(dict2)!=list):
        return
    summ_dict=copyDict(dict1)
    temp = list(dict2.keys())
    for i in temp:
         summ_dict[i]=dict2[i]
    return summ_dict
def sqrtgener(input):
    output=list(map(sqrt,input))
    output=[sqrt(x) for x in input]
    return output
def isprime(input):
    for x in range(2, int(sqrt(input))+1):
        if input%x==0:
            print(input, 'has factor', x)
            break
    else:
        print(input, 'is prime')

# isprime(1543235325332332)
xxx=[1,2]
yyy=1
def printer():
    print(xxx)
def printeryyy():
    print(yyy)
# print(int(sqrt(15)))
# isprime(-13)
# isprime(15003453453453453535)
# isprime(15.0)

a={'a':1}
c=[1,2]
d=[1]
e=[2,4,9,16,25]
# print(sqrtgener(e))
#
# if type(d)==list:
#     print ("true")
# b={'b':2, 'a':3}
# print(addDict(a, c))


# print (addDict({'a':1}, {'b':2}))
# print (adder_name(bad='10', ugly='2', good='5', gg='6'))
# new=copyDict({'bad':'10', 'ugly':'2', 'good':'5', 'gg':'6'})
# new['ugly']=11111
# print(new)