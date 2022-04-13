def add(fnum,snum):
    return fnum+snum
def sub(fnum,snum):
    return fnum-snum
def mul(fnum,snum):
    return fnum*snum
def div(fnum,snum):
    return fnum/snum
def mod(fnum,snum):
    return fnum%snum

print("addtion for 1")
print("subtraction for 2")
print("multiply for 3")
print("divide for 4")
print("modulus for 5")
number=input("so please enter a number for operation:")

num1=int(input("please enter a first num= "))
num2=int(input("please enter a first num= "))

if number ==1:
        print(num1,"+",num2,"=",add(num1,num2))
elif number ==2:
    print(num1,"-",num2,"=",sub(num1,num2))
elif number ==3:
    print(num1,"*",num2,"=",mul(num1,num2))
elif number ==4:
    print(num1,"/",num2,"=",div(num1,num2))
elif number ==5:
    print(num1,"%",num2,"=",mod(num1,num2))

else:
    print("please enter valid num")