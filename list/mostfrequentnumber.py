lst=[1,2,3,4,5,5,5,6,7,7,7]

counter=0
val=0

for num in lst:
    temp=lst.count(num)

    if(temp>counter):
        counter=temp
        val=num

print(f"the most frequent number is {val}  and it repeated {counter}  times")


# lst1=[1,2,3,3]
#
# for num in lst1:
#     print(num)
# print(lst1.count(3))
#