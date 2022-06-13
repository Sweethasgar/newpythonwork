lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]

# for sub_lst in lst:
#     for num in sub_lst:
#         if num>16:
#             print(num)

# flaten_lst=[]
#
# for sub_lst in lst:
#     for num in sub_lst:
#         flaten_lst.append(num)
# print(flaten_lst)
# print(max(flaten_lst))


flaten_lst=[num for s_lst in lst for num in s_lst]
print(flaten_lst)

gt_lst=[ num for num in flaten_lst if num > 16]
print(gt_lst)

odd_lst=[num for num in flaten_lst if num%2!=0]
print(odd_lst)

even_lst=sum([num for num in flaten_lst if num%2==0])
print(even_lst)

mapped_lst = [num+1 if num > 25 else num-1 for num in flaten_lst]
print(mapped_lst)