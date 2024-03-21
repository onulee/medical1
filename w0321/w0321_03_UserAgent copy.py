import requests

# User-Agent 사용방법
# res = requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
print("코드 : ",res.status_code)
res.raise_for_status()

print(res.text)

# with open("a1.html","w",encoding="utf8") as f:
#     f.write(res.text)
    
# print("파일이 저장되었습니다.")    