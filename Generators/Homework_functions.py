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
    if len(dict) == 0: return "Fuck"
    temp = list(dict.keys())
    summ ={}
    for i in temp:
         summ[i]=dict[i]
    return summ
# print (adder(1,2))
print (adder_name(bad='10', ugly='2', good='5', gg='6'))
new=copyDict({'bad':'10', 'ugly':'2', 'good':'5', 'gg':'6'})
new['ugly']=11111
print(new)