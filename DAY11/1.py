import requests
import random
import json
from hashlib import md5
import socket
import threading
def translate(text):
    appid = '20240115001942226'
    appkey = 'xysfnOsgqH7pcfM3Pk5Z'

    from_lang = 'en'
    to_lang =  'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = 'what'

    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result['trans_result'][0]
def connect():
  while True:
    client,address = server.accept()
    thread = threading.Thread(target=run,args=(client,address))
    thread.start()
  pass
def run(client,address):
  t = client.recv(1024)
  r = translate(t.decode())
  client.sendall(r.encode('utf-8'))
  pass
server = socket.socket()
server.bind(('127.0.0.1',10295))
server.listen(5)
thread_main = threading.Thread(target=connect)
thread_main.start()