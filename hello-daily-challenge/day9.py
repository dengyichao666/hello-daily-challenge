import random
import time

target = random.randint(1,10)
print("我想到一个1~10之间的数，你猜猜看！")
start = time.time()
for turn in range (1,6):
	guess = int(input("你的猜测:"))
	if guess == target:
		print("猜对了!")
		break
	elif guess < target:
		print("小了，再大点")
	else:
		print("大了，再小点")
else:
	print("机会用完了，答案是{tartget}")

end = time.time()
print(f"你猜了{end - start}秒")
