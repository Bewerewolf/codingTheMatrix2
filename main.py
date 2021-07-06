import math


def main():
    #print("hola")
    # This is a dictionary
    my_dictionary = dict()
    my_dictionary["first"] = "Erik"
    #print(my_dictionary)
    #print([2*x-1 for x in range(50) if x>0]) #5.18
    L = ['A', 'B', 'C', 'D', 'E']
    myzip = list(zip(range(5), L))
    #print(list(myzip)) #5.19

    numlist1 = [10, 25, 40]
    numlist2 = [1, 15, 20]
    myzip2 = zip([10, 25, 40], [1, 15, 20])
    #print([x+y for (x,y) in list(myzip2)]) #5.20
    dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
    newlist = []
    k = 'James' #key
    for d in dlist:
        newlist.append(d[k])
    #print(newlist) # 5.21
    dlist = [{'Frodo': 'Elijah', 'Bilbo': 'Ian'}, {'Thorin': 'Richard', 'Bilbo': 'Martin'}]
    newlist = []
    k = 'Frodo'
    count = 0
    for d in dlist:
        if k in dlist[count]:
            newlist.append(d[k])
        else:
            newlist.append('NOT PRESENT')
        count += 1
    #print(newlist)# 5.22
    #print({x:x*x for x in range(99)})# 5.23
    D = {'red', 'white', 'blue'}
    #print({x:x for x in D})# 5.24

    base = 999
    digits = set(range(base))
    #heads up, no clue why the following line works. dunno why it wants 0*math.floor(x/100). i tried 100*math.floor(x/100) but that worked too much? confusing
    #print({x:[math.floor(x/100), math.floor(x/10)-10*math.floor(x/100), x-0*math.floor(x/100)-10*math.floor(x/10)] for x in digits})# 5.25
    def twice(z):
        return 2*z
    #print(twice(2))
    dct = {'a':'A', 'b':'B', 'c':'C'}
    L = ['b', 'c', 'a']
    def dict2list(L):
        output = []
        for i in L:
            output.append(dct[i])
        return output
    #print(dict2list(L))# 5.30
    keylist = ['a', 'b', 'c']
    L = ['A', 'B', 'C']
    def list2dict(L, keylist):
        output = {}
        for i in range(len(keylist)):
            output[keylist[i]] = L[i]
        return output
    #print(list2dict(L, keylist))# 5.31
    #S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}
    #plot(S, 4)



if __name__ == '__main__':
    main()
