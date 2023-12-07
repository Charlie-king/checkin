import requests
import os 
import json

session = requests.Session()

def sign(email, password):

  login_url = f"{url}/login"
  checkin_url = f"{url}/checkin"

  # 为每个账号单独登录
  data = {'email': email, 'password': password}  
  session.post(login_url, data=data)

  # 签到
  result = session.post(checkin_url, json={'email': email}).json()['message']

  print(f'{email} 签到结果: {result}')

  return result

results = {}
for account in accounts:

  email = account['email'] 
  password = account['password']

  result = sign(email, password)

  # 记录结果
  results[email] = result

# 推送
if os.environ.get('SCKEY'):
  # 推送代码
