arr=[1,12,34,56,14,56,75,32]

element=14

# if element in arr:
#     print(True)
#
# else:
#  print(False)
flag=0
for num in arr:
    if element==num:
        flag=1
        break
print("element found"if flag==1 else "not found")        