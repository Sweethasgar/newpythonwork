num = 123
res = " "
while (num != 0):
    last_digit = num % 10
    #     print(last_digit ,end =" ")
    #     num=num//10
    res = res + str(last_digit)
    num = num // 10
print(res)

# q1 2=>2+22 24
# 3=>3+33+333+>369
# 4=>4+44+444+4444=>4936