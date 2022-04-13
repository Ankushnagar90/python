mylist=[]
num=int(input("how many numbers you want to put in the list "))
for i in range(0,num):
    n=int(input("enter a number"))
    mylist.append(n)
    if n%2==0:
        print(i)

