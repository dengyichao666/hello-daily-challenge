text = input("写一句话存起来：")
with open("note.txt","w",encoding = "utf-8") as f:
    f.write(text)
with open("note.txt","r",encoding = "utf-8") as f:
    content = f.read()
    print("读回来的是：",content)


import json
users = {"name":"张三","age":18,"city":"青岛"}
with open("user.json","w",encoding = "utf-8") as f:
    json.dump(users,f,ensure_ascii = False)
with open("user.json","r",encoding = "utf-8") as f:
    loaded = json.load(f)

    print(loaded["name"],loaded["age"])


users = [
{"name":"张三","age":"19"},
{"name":"李四","age":"20"},
{"name":"王五","age":"18"}
]
with open("users.json","w",encoding = "utf-8") as f:
    json.dump(users,f,ensure_ascii = False)
with open("users.json","r",encoding = "utf-8") as f:
    for u in json.load(f):
        print(u["name"])