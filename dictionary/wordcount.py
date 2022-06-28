# pattern="ABACD"
#
# count={}
#
# for char in pattern:
#     if char in count:
#         count[char]+=1
#
#     else:
#         count[char]=1
#
# print(count)



# pattern="ABACD"
#
# count={}
#
# for alph in pattern:
#     if alph in count:
#
#         print(f"first occured ",alph)
#         break
#
#     else:
#         count[alph]=1
#

pattern="ABACCD"

count={}
count_arr=[]
for char in pattern:
    if char in count:
        count_arr.append(char)

    else:
        count[char]=1

print(count_arr)