import json

with open("post.json", encoding="utf-8") as f:
    data = json.load(f)
    print(len(data))

num_post = [post for post in data if post["userId"] == 1]
print(len(num_post))

user_liked = [len(post["liked_by"]) for post in data if post["postId"] ==6]
print(user_liked)

user_likedd=[post for post  in data if 2 in post["liked_by"]]
print(len(user_likedd))