f=open("mobiles.tx","r")
# fun=[i.rstrip("\n") for i in f]
# print(fun)
#
# largest=[i for i in fun if fun[2]
# print(largest)
all_mobiles=[]
for line in f:
    mobiles=line.rstrip("\n").split(",")
    all_mobiles.append(mobiles)
print(all_mobiles)


costly_mob=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mob)