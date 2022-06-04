# def prime_number(num):
#     flag=0
#     for i in range(2,num):
#         if (num%i==0):
#             flag=1
#             break
#     return True if flag==0 else False
#
# def prime_range(low,upp):
#     for num in range(low,upp+1):
#         if prime_number(num):
#             print(num)
#
# prime_range(10,50)


def prime_number(num):
    flag=0
    for i in range(2,num):
        if (num%i==0):
            flag=1
            break
    return True if flag==0 else False



def prime_range(low,upp):
    for num in range(low,upp+1):
        if prime_number(num):
            print(num)

prime_range(10,50)
