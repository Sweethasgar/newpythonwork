lst1=[1,2,3,4,5,54,32,43,45]
lst2=[2,3,4,1,65,64,3,22,23]

lst3=[]

# for num in lst1:
#     if num in lst2:
#         lst3.append(num)
# print(lst3)

for n1 in lst1:
    for n2 in lst2:
        if n1==n2:
         lst3.append(n1)
print(lst3)