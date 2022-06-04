# num=2
# sum=0
#
# p=3
# for i in range(1,num+1):
#     sum+=p
#     p=(10*3)+3
#
#     print(sum)
num=3
i=1
pattern=""
sum=0
while(i<=num):
    pattern=pattern+str(num)
    sum=sum+int(pattern)
    i+=1
print(sum)
