class user:
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")


class addproduct:
    def post(self,**kwargs):

           self.p_name=kwargs.get("p_name")
           self.user=kwargs.get("user")

    def __str__(self):
         return self.p_name



user=user(name="rahul",role="admin")

pro1=addproduct()
pro1.post(p_name="soap",user=user)
print(pro1)