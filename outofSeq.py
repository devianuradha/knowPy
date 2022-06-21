#For a given array containing integer elements in a set sequence and one element out of sequence, write a program to find the element.
def outOfSeq(a):
    thislist = ["apple", 1, "cherry", 2, 3]
    difflist=[]
    thislist.append(a)
    for ele in thislist:
        if type(ele) != type(thislist[0]):
            difflist.append(ele)
    #print(thislist)
    return difflist
