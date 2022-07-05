from blog.model import users,posts


# print (users)

# username="akhil"
# password="Password@123"
#
# user=[user for user in users if user["username"]==username and user["password"]==password]
# if user:
#     print("succes")
#
# else:
#     print("failed")

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid user")

    return wrapper


session={}
def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")

    user = [user for user in users if user["username"] == username and user["password"] == password]

    return user

# print(authenticate(username="akhil",password="Password@123"))
class Loginview:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]

        print(session)





class postlistview:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @sighnin_required
    def post(self, *args, **kwargs):
        userid = session["user"]["id"]
        post = kwargs.get("data")
        post["userid"] = userid
        print(post)
        posts.append(post)
        print("posted succesfully")
        print(post[-1])


log_in=Loginview()
log_in.post(username="akhil",password="Password@123")
all_posts=postlistview()
mypost={"title":"goodmorning","content":"my content","likedby":[]}
all_posts.post(data=mypost)
print(all_posts.get())

# do my post vir