from urllib.request import urlopen

resp = urlopen("https://www.baidu.com")
print(resp.status)
print(resp.read()[ :100])