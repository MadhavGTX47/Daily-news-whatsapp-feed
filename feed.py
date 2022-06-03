import pywhatkit
import requests
import schedule
import time

from datetime import datetime
from bs4 import BeautifulSoup

url='https://www.bbc.com/news'

def job(t):
    
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    
    for x in headlines:
        s += (x.text.strip())+ " \n"

        print(s)
    message = input(s)

    pywhatkit.sendwhatmsg(mobile,message,hour,minute)
    return


now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))


schedule.every().day.at("{}:{}".format(hour,minute)).do(job,'Sent')

while True:
    schedule.run_pending()
    time.sleep(60) 