lst=[1,2,4,5,6,7,8,9,6,]
evenlst=[]
for num in lst:
    if num%2==0:
        evenlst.append(num)
print(evenlst)
evenlst.sort(reverse=True)

evenlst.insert(2,100)
print(evenlst)
print(lst.count(2))






