lst = []
num = int(input('How many numbers: '))
summ=0
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
    summ=summ+numbers
print("print the list ",lst)
print("Sum of elements in given list is :",summ)