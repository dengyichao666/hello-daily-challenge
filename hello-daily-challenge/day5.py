user = {"name":"张三","age":18,"city":"青岛"}
print(user["name"])
print(user["age"])
user["age"] = 19
user["hobby"] = "写代码"
del user["city"]
print (user)
#第三点开始未写  
for key,value in user.items():
	print(f"{key} = {value}")
print(user.get("city"))
print(user.get("city","未知"))
users = [
{"name":"张三","age":"19"},
{"name":"李四","age":"20"},
{"name":"王五","age":"18"}
]
for u in users:
	print(f"{u["name"]}今年{u["age"]}岁")
#好像不太理解
#完成