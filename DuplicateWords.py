#Duplicate words
def remove_duplicate(s):
    words=s.split()
  #  words="".join(words)
    print(words)
    dup=""
    uniq=""
    for i in words:
        if(i in uniq):
            dup=dup+" "+i
            pass
        else:
            uniq=uniq+" "+i
    print("Unique Words: ",uniq)
    print("Duplicate words: ",dup)
    
s="My name is Anuradha My name is not Anuradha"
print(s)
print(remove_duplicate(s))
