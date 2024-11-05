import datetime
import requests
from bs4 import BeautifulSoup

now = datetime.datetime.now()
correct_heartbeat = "Heartbeat! " + now.strftime("%Y-%m-%d %H:%M:%S")

url = "http://localhost:12345"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    current_heartbeat = soup.find('p', {'id': 'heartBeat'})
    if current_heartbeat.text.strip() == correct_heartbeat:
        print("Success")
    else:
        print("Failure")
else:
    print(f"Request error, status code: {response.status_code}")

