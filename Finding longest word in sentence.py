enter=input("Enter text in here: ")
x= enter.split(' ')
li=[]
mydict=dict()

for i in x:
    k=len(i)
    mydict[k]=i
print(mydict)

numbers=mydict

mydictkey=int(input("Enter Highest Integer in Dictionary: "))
descriptionValue=numbers.get(mydictkey)
print('Longest Word is '+ descriptionValue)
