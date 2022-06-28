class employeee:
    def __init__(self,**kwargs):
        self.id=kwargs.get(id)
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name

class department:
    def __init__(self,**kwargs):
        user=kwargs.get("user")
        if user=="admin":
            self.dep_name=kwargs.get("dep_name")
            self.user=kwargs.get("user")
        else:
            print("no acces")


    def __str__(self):
        return self.dep_name


user=employeee(id=1,name="rahul",role="hr")
print(employeee)

department=department(dep_name="social",user=employeee)
print(department)
