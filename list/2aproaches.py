amount = [10, 20, 30, 40, 50, 60]
for i in range(0,len(amount)):
    print(amount[i])
print()


for value in amount:
    print(value)
print()

numbers=[10,11,12,13,14,15]

for num in numbers:
    if num%2==0:
        print(num)


numbers=[11,12,13,14,15,16,17,18]

for num in numbers:
    if num>15:
        print(num+1)

    elif num<15:
         print(num-1)


    elif num==15:
         print(num)

print()


print()
number=[11,12,13,14,15,16,17,18]
count=0
for num in numbers:
    if num in range(14,19):
        count+=1
print(count)
print()


number1=[-1,1,-2,2,0,3,0,-5,6,1]
pos_count=0
neg_count=0
zero_count=0

for num in number1:
    if num<0:
        pos_count+=1


    elif num>0:
        neg_count+=1

    elif num==0:
        zero_count+=1

print(pos_count)
print(pos_count)
print(zero_count)

print()

number3=[1,3,4,5,6,7,8]

sum=0

for num in number3:
    sum+=num
print(f"sum is {sum}")


