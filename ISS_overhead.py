import time

import requests
from datetime import datetime
import pytz
import smtplib

mail = 'swapniljagadale007@gmail.com'
password = 'ecvbxvjmaqaurpyv'
my_lat = 19.0252698
my_lng = 73.1044352
reciver = 'swapniljagadale999@gmail.com'


def to_ist(time_string):
    time_obj = datetime.strptime(time_string, "%I:%M:%S %p")
    utc_timezone = pytz.timezone('UTC')
    ist_timezone = pytz.timezone('Asia/Kolkata')
    utc_aware_time = utc_timezone.localize(time_obj)
    ist_time = utc_aware_time.astimezone(ist_timezone)
    return ist_time

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    if my_lat - 5 <= latitude <= my_lat + 5 and my_lng - 5 <= longitude <= my_lng + 5:
        return True


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_lng,
    }
    response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    data2 = response2.json()
    sunrise_hr = int(str(to_ist(data2['results']['sunrise'])).split(" ")[1].split(":")[0])
    sunset_hr = int(str(to_ist(data2['results']['sunset'])).split(" ")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset_hr and time_now <= sunrise_hr:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(mail, password)
        connection.sendmail(
            from_addr=mail,
            to_addrs=reciver,
            msg="subject:its ISS 🛰️\n\nHurry up!!! its ISS(international space station) is passing from above you get out of your home and see it in sky. 🔭"
                ""
                ""
                "you know what ISS travels at speed of 28,000 Km/h around the earth")





