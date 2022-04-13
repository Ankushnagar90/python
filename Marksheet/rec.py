n=int(input("enter a num"))
def recu_sum(n):
    if(n <=1):
        return 
    else:
        return n+rec_sum(n-1)
print(rec_sum(num))
