f=open("students.txt")
all_stud=[stud.rstrip("\n")for stud in f]
w=open("failed.txt")
failed_stud=[stud.rstrip("\n")for stud in w]
r=open("passed.txt","w")


passed_stud=set(all_stud)-set(failed_stud)

for st in passed_stud:
    r.write(st)