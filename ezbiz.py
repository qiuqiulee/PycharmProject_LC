import requests

url = 'https://www.easybiz.me/users/sign_in'
values = {'user_login': 'qiuqiu',
          'user_password': 'aa19901028'}

r = requests.post(url, data=values)
print(r.content)

