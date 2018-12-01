text=input("Enter your text here: ")
splittext=text.split(" ")
mydict=dict()
empt=[]
for i in splittext:
    mydict[len(i)]=i
    for n in mydict.keys():
        empt.append(n)
        maxi=max(empt)
mykey = maxi
description=mydict.get(maxi)
print('Longest word in sentence is '+ description)


