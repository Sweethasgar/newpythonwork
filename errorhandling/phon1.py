import json
import random
try:
    with open("phone.json",encoding="utf-8") as f:
        data=json.load(f)
        print(data)

    all_users=list(map(lambda user:user["id"],data))
    print(all_users)

    my_following=[user["followers"] for user in data if user["username"]=="akhil"].pop()
    print(my_following)
    my_id=[user["id"]for user in data if user["username"]=="akhil"].pop()
    suggesions=set(all_users)-set(my_following)
    suggesions.remove(my_id)
    out=random.sample(suggesions,2)
    print(out)
except Exception as e:
    print(e.__class__)
print("hello world")