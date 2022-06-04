# for row in range(1,5):
#     for col in range(1,5):
#       print(col,end=" ")
#
#     print()
#
# for row in range(1,4):
#     for col in range(1,4):
#         print(row,end=" ")
#     print()

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end="")
#     print()
#


# for row in range(1,5):
#     for col in range(row):
#      print(row,end=" ")
#     print()

#
# for r in range(1,5):
#     for c in range(5,r,-1):
#         print("#",end="")
#     print()



# full pyramid and holo full pyramid


#
# for row in range(1,5):
#     for col in range(1,(5-row)):
#         for col in range(1,(row+1)):
#             print("*",end=" ")
#             print()



for row in range(1,5):
    for col in range(1,7):
        if row==4 or (col+row==4) or (col-row==2):
            print("*",end=" ")

