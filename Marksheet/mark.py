n=80
name="name:"                                   #Assigning part
rolln="rollnumber:"
cl="class:"
dob="DOB:"
fname="Father's name:"
mname="Mother's name:"
scl="School'name:"

# sub1="hindi"
# sub2="english"
# sub3="mathematics"
# sub4="so.science"
# sub5="science"

ntotal="100"



# subjects=[hindi,english,mathematics,so_science,sanskirt]
# grade=[A,B,C,D,E]



# uname=input("enter your  name:")              #user input part
# urollno=input("enter a your roll number ")
# ucl=int(input("enter your Class"))
# udob=int(input("enter your DOB:"))
# ufname=input("Enter your father's name:")
# umname=input("Enter your mother's name:")
# uscl=input("Enter your school name:")
# uhmarks=int(input("Enter your Hindi marks:"))
# uemarks=int(input("Enter your English marks:"))
# ummarks=int(input("Enter your Mathematics marks:"))
# usomarks=int(input("Enter your So.Science marks:"))
# usmarks=int(input("Enter your Science marks:"))





def grade(mark):
    scores=int(mark)                     #grade function
    if scores>= 90 and scores<= 100:
        grade='A'

    elif scores >= 75 and scores < 90:
        grade='B'

    elif scores >= 50 and scores < 75:
        grade='C'

    elif scores >= 33 and scores< 50:
        grade='D'
    else :
        grade = "E"

    return grade
uhmarks=56
mark1=grade(uhmarks)    
uemarks=0
mark2=grade(uemarks)
ummarks=25
mark3=grade(ummarks)
usomarks=0
mark4=grade(usomarks)
usmarks=85
mark5=grade(usmarks)


SUM_OBT=int(uhmarks+uemarks+ummarks+usomarks+usmarks)

      #add_obt_marks
percent=int(SUM_OBT/5)
percent1=percent
print(percent1)

def grading(percent1):
    
    grading = ""
    score=int(percent1)
                                            #whole grade function
    if score>= 90 and score<= 100:
        grading='A+'

    elif score >= 75 and score < 450:
        grading='A'

    elif score >= 250 and score < 375:
        grading='B'

    elif score >= 165 and score< 250:
        grading='C'

    return grading

final=grading(percent1)






uname="ankush"                                  #general static part
urollno="12345"
ucl="10"
udob="12/03/2001"
ufname="xyz"
umname="abc"
uscl="SHSS"






le_nm=len(name)                         #length part
le_roll=len(rolln)
le_unm=len(uname)
le_uroll=len(urollno)
le_cl=len(cl)
le_dob=len(dob)
le_ucl=len(ucl)
le_udob=len(udob)
le_fname=len(fname)
le_ufname=len(ufname)
le_mname=len(mname)
le_umname=len(umname)
le_scl=len(scl)
le_uscl=len(uscl)


# le_hin=len(sub1)
# le_eng=len(sub2)
# le_math=len(sub3)
# le_so=len(sub4)
# le_sci=len(sub5)


# le_uemarks=len(str(uemarks))
# le_ummarks=len(str(ummarks))
# le_usomarks=len(str(usomarks))
# le_usmarks=len(str(usmarks))

# le_ntotal=len(ntotal)







print("|"+"-"*(n-2)+"|")
affialate="CENTRAL BOARD OF SECONDARY EDUCATION  " 
length=len(affialate)
print("|"+" "*(int(n-length-2)/2)+affialate+" "*(int(n-length-2)/2)+"|")
scl_name= "SENIOR SECONDARY SCHOOL EXAMINATION 2021"
length_scl=len(scl_name)
print("|"+" "*(int(n-length_scl-2)/2)+scl_name+" "*(int(n-length_scl-2)/2)+"|")
state="MADHYA PRADESH"
length_st=len(state)
print("|"+" "*(int(n-length_st-2)/2)+state+" "*(int(n-length_st-2)/2)+"|")
print("|"+"-"*(n-2)+"|")
 
print("|"+name+uname+" "*(int(n-le_nm-le_roll-le_unm-le_uroll-2-2))+rolln+urollno+" "*2+"|")

print("|"+cl+ucl+" "*(int(n-le_cl-le_dob-le_ucl-le_udob-2-2))+dob+udob+" "*2+"|")

print("|"+fname+ufname+" "*(n-len(fname)-len(ufname)-2)+"|")
print("|"+mname+umname+" "*(n-len(mname)-len(umname)-2)+"|")
print("|"+scl+uscl+" "*(n-len(scl)-len(uscl)-2)+"|")

print("|"+" "*(n-2)+"|")
print("|"+"-"*(n-2)+"|")


print("|"+" "*3+"SUBJECT"+" "*8+"|"+" "*3+"OBTAIN MARKS"+" "*4+"|"+" "*3+"TOTAL"+" "*11+"|"+" "*3+"GRADE"+" "*11+"|")
print("|"+"-"*(n-2)+"|")

print("|"+" "*3+"Hindi"+" "*10+"|"+" "*6+"%03d" % uhmarks+" "*10+"|"+" "*6+"100"+" "*10+"|"+" "*6+mark1+" "*12+"|")
print("|"+" "*3+"English"+" "*8+"|"+" "*6+"%03d" % uemarks+" "*10+"|"+" "*6+"100"+" "*10+"|"+" "*6+mark2+" "*12+"|")
print("|"+" "*3+"Mathematics"+" "*4+"|"+" "*6+"%03d" % ummarks+" "*10+"|"+" "*6+"100"+" "*10+"|"+" "*6+mark3+" "*12+"|")
print("|"+" "*3+"So.Science"+" "*5+"|"+" "*6+"%03d" % usomarks+" "*10+"|"+" "*6+"100"+" "*10+"|"+" "*6+mark4+" "*12+"|")
print("|"+" "*3+"Science"+" "*8+"|"+" "*6+"%03d" % usmarks+" "*10+"|"+" "*6+"100"+" "*10+"|"+" "*6+mark5+" "*12+"|")
print("|"+"-"*(n-2)+"|")
print("|"+" "*3+"TOTAL MARKS"+" "*4+"|"+" "*6+str(SUM_OBT)+" "*10+"|"+" "*6+"500"+" "*10+"|"+" "*6+"GRADE:"+final+" "*6+"|")










