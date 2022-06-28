students={"name":"sweeth","roll_num":2,"class":"tenth","grade":100}
print(students["name"])
print(students["roll_num"])
print(students["class"])
print("grace mark "in students)

students["grace mark"]=23
print(students)
students["class"]="nineth"
print(students)

print(students.get("name"))

# if "mark" in students:
#     students["mark"]=56
# else:
#     students["mark"]=12
# print(students.get("mark"))

students["mark"]=23  if "mark" in students else 12
print(students.get("mark"))

if students["grade"] > 150:
    students["grade"]-=10
else:
    students["grade"]-=20
    
    print(students.get("grade"))