mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
# number_phone=[mob for sub_ls in mobiles for mob in sub_ls]
# print(number_phone)
# phones=[mob for mob in mobiles if mob==[2]]
# print(phones)
#
# print(mobiles[7])
#
# total_stck=[stck for stck in mobiles[7]]
# print(total_stck)
#
# samsung=[mob for mob in mobiles if mob[1]=="samsung"]
# print(samsung)

print(f"th total number of mobiles {len(mobiles)}")

stk=[mob for mob in mobiles if mob[-1]==0]
print(stk)

mobile_gt=[mob for mob in mobiles if mob[4] in range(20000,30001)]
print(mobile_gt)

fiveg=[mob for mob in mobiles if mob[2]=="5g"]
print(fiveg)
# max_price=max([mob[4] for mob in mobiles])



mobiles.sort(reverse=True, key=lambda mob:mob[4])
print(mobiles)

costly_mob=max(mobiles,key=lambda m:m[4])
print(costly_mob)

low_cost=min(mobiles,key=lambda m:m[4])
print(low_cost)

mob_ten=[mob[4]==10000 for mob in mobiles]
print("available" if True in mob_ten else "na")