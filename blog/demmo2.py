from blog.model import users,posts


def sighnin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid user")

session={}

def authentication(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")

    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user


class login:
    def post(self,*args,**kwargs):
        self.username=kwargs.get("username")
        self.password=kwargs.get("password")
        user=authentication(user_name="username",password="password")
        if user:
            session["user"] = user[0]
        print(session)

class postlistview:
    @sighnin_required
    def get(self,*args,**kwargs):
        return posts
    @sighnin_required
    def post(self,*args,**kwargs):
        userid=session["user"]["id"]
        post=kwargs.get("data")
        post["userid"]=userid
        print(post)
        posts.append(post)
        print("posted succesfully")
        print(post[-1])


        



login_in=login()
login_in.post(username="akhil",password="Password@123")
print(login_in)
