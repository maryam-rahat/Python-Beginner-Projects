import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : '9622670992',
        'message' : 'Hi Maryam, From Maryam',
        'key': 'textbelt'
    })
    print(resp.json())


schedule.every().day.at('21:19').do(send_message)

