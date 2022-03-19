import requests
import smtplib
from datetime import datetime

MY_LAT = 46.288840 # Your latitude
MY_LONG = 28.378440# Your longitude
MY_MAIL = "" # enter your gmail
MY_PASS = "" # enter gmail password

def iss_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if 46 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def nigth():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if iss_head() and nigth():
        server = smtplib.SMTP("smtp.gmail.com")
        server.starttls()
        server.login(MY_MAIL, MY_PASS)
        server.sendmail(
            from_addr=MY_MAIL,
            to_addr=MY_MAIL,
            msg="Subject:look up\n\n the iss is above "

        )