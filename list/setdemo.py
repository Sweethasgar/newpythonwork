# lst=[1,2,3,4,4,3,5,6,7]
# st=set(lst)
# print(st)

st1={1,2,3,4,5,6}
st2={10,11,12,2,3}

st1.add(10)
union_set=st1.union(st2)
print(union_set)

inter_set=st1.intersection(st2)
print(inter_set)

set_diff=st1.difference(st2)
print(set_diff)

students=["raju","rahul","neena","abhi"]
pass_student=["raju","rahul"]
st=set(students)
pas_set=set(pass_student)

failed_students=st-pas_set
print(failed_students)


