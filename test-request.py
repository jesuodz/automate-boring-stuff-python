import requests

res = requests.get('http://localhost:8000/code/script.py')

playFile = open('script.py', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()
