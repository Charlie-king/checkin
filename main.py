import requests, json, re, os


# 从环境变量获取参数
URL = os.environ.get('URL')
ACCOUNTS = json.loads(os.environ.get('ACCOUNTS'))  
PUSH_TOKEN = os.environ.get('PUSH_TOKEN')

session = requests.Session()

def sign(email, passwd):
  login_url = f"{URL}/auth/login"
  check_url = f"{URL}/user/checkin"

  data = {"email": email, "passwd": passwd}
  resp = session.post(login_url, json=data)

  resp = session.post(check_url)
  return resp.json()["msg"]

results = {}
for account in ACCOUNTS:
  email = account["email"]
  passwd = account["passwd"]  

  result = sign(email, passwd)
  results[email] = result

  print(f"{email} 签到结果: {result}")

desp = ""  
for email, status in results.items():
  desp += f"{email} 签到结果:{status}\n"

if PUSH_TOKEN:
  # 推送代码

print("签到任务完成")
