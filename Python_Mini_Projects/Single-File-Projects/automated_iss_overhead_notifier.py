import requests
from datetime import datetime
import smtplib
import time

LAT = 24.659222
LONG = -68.840448
EMAIL = "your email here"
PASSWORD = "your email password here"



def is_iss_overhead():

    response =  requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data['iss_position']["longitude"])
    iss_latitude = float(data['iss_position']['latitude'])

    if LAT-5<= iss_latitude  <= LAT+5 and LONG-5 <= iss_longitude <= LONG+5:
        return True

def is_night():

    parameters = {
        "lat":LAT,
        "lng":LONG,
        "formatted":0,
    }

    url = "https://api.sunrise-sunset.org/json"
    response =  requests.get(url,params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=576) as connection:
            connection.starttls()
            connection.login(EMAIL,PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject: look Up\n\nThe ISS is above you in the sky")












