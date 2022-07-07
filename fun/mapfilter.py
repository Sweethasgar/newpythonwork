from functools import reduce
lst=[10,2,30,4]


num_out=[num-1 if num<5 else num+1 for num in lst]
print(num_out)

map_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(map_out)




filter_out=list(filter(lambda  n:n%2==0,lst))
print(filter_out)

all_sum=reduce(lambda n1,n2:n1+n2,lst)
print(all_sum)

all_product=reduce(lambda n1,n2:n1*n2,lst)
print(all_product)


max_out=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max_out)
min_out=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(min_out)