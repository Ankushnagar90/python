

# # hin=int(input("enter your hindi marks:"))
# # math=int(input("enter your hindi marks:"))
# # so=int(input("enter your hindi marks:"))
# # eng=int(input("enter your hindi marks:"))
# # hin=int(input("enter your hindi marks:"))

# serial=[1,2,3,4,5]
# subjects=["hindi","english","mathematics","so.science","science"]
# max_marks=[100,100,100,100,100]
# obt_lst=[]


# # len_sub=len(subjects)

# summ=0
# for x in subjects:
#     a = int(input("enter obt marks for each subject:"))
#     obt_lst.append(a)
# for y in obt_lst:
#     summ=summ+y
# print(summ)


# total=summ

# len_sub=len(subjects)
# print(len_sub)
# percent=(total/len_sub);
# print(percent)


# for z in obt_lst
# if (percent>33 and percent<50):
#     print("C")
# elif(total>=50 and percent<75):
#     print("B")
# elif(percent>=75 and percent<90):
#     print("A")
# elif(percent>=90 and percent<100):
#     print("A+")


# for (a,b,c,d) in zip(serial,subjects,obt_lst,max_marks):
#     print(a,b,c,d)






# def gradess(scores):
#     if scores >= 90 and scores<= 100:
#         return 'A'
#     elif scores >= 75 and scores < 90:
#         return 'B'
#     elif scores >= 50 and scores < 75:
#         return 'C'
#     elif scores >= 33 and scores< 50:
#         return 'D'
#     else:
#         return 'FAIL'


# grading=gradess(scores)

# print(grading)
# uhmarks=35
# print(type(uhmarks))
# mark1=scores(uhmarks)
# uemarks=65
# mark2=scores(uemarks)
# ummarks=85
# mark3=scores(ummarks)
# usomarks=70
# mark4=scores(usomarks)
# usmarks=85
# mark5=scores(usmarks)
uhmarks=35
uemarks=65
ummarks=85
usomarks=70
usmarks=85

SUM_OBT=uhmarks+uemarks+ummarks+usomarks+usmarks

print(SUM_OBT)
percent=int(SUM_OBT/5)
percent1=percent
print(percent1)

# n=5
# print('%0*d'%(3,n))


# def grade(scores):

#                                    #grade function
#     if scores>= 90 and scores<= 100:
#         grade='A'

#     elif scores >= 75 and scores < 90:
#         grade='B'

#     elif scores >= 50 and scores < 75:
#         grade='C'

#     elif scores >= 33 and scores< 50:
#         grade='D'

#     return grade

# print(grade)
# scores=77
# grade(scores)


# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
