import requests

url='http://127.0.0.1:8000/articles/3/'

token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1ODE3MjA1LCJpYXQiOjE3MDU4MDI5NTcsImp0aSI6ImQ1NzZhYjExOWM3NjQzMWI4ZTAwYjBiNzAyM2RlYThjIiwidXNlcl9pZCI6Mn0.z7z7SIV0uqZHMZG8M8bG23YHd_xyrk6sOgq9lQt56iY'

headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

data={
    'title': 'This is new artcile created using API',
    'content': 'This is new artcile\'s body created using API'
}

res=requests.put(url, headers=headers, json=data)

print(res.json())
print('Proccess ended')
