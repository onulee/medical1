import requests
# url = "http://www.google.com"
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/#google_vignette"
url = "https://www.melon.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

print(res.text)

# with open("user_agent.html","w",encoding="utf-8") as f:
#     f.write(res.text)

