num=int(input("enter a num"))
num1=num
rev=0
while(num1>0):
    rem=num1%10
    rev=(rev*10)+rem
    num1=num1/10
print(rev)
if num==rev:
    print("num is palindrome")
else:
    print("num is not palindrome ")