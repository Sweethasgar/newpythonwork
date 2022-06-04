num=123
sum=0

while(num!=0):
    lastdigit=num %10
    cube=lastdigit**3
    sum=sum+cube

    num=num//10
print(sum)


