
def prime_number(num):
    flag=0
    for i in range(2,num):
        if (num%i==0):
            flag=1
            break
    return True if flag==0 else False
print(prime_number(13))