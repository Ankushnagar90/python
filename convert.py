lst1=["swift","suzuki",2000,"bmw","symbol",2014,"mercedes","2015"]

mydict=dict()

print("before filtering")
for index,value in enumerate(lst1):
    if index%2!=0:
        mydict[index]=value

print(mydict)


    