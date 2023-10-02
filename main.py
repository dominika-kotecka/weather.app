import requests
import mysql.connector
from datetime import datetime
import schedule
import time

API_KEY = "912c622485ebcccfe6e75ebb3dc2de10"
API_CITY = "Kraków"
API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}&appid={API_KEY}&units=metric&lang=pl"

def fetch_weather():
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()

        # db connection
        connection = mysql.connector.connect(
            host ="localhost",
            user ="root",
            password="",
            database="pogoda"
        )

        cursor = connection.cursor()

        sql_query = "INSERT INTO krakow (temp,min_temp,max_temp, humidity,pressure, descryption, date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (
            data["main"]["temp"],
            data["main"]["temp_min"],
            data["main"]["temp_max"],
            data["main"]["humidity"],
            data["main"]["pressure"],
            data["weather"][0]["description"],
            datetime.now().strftime('%H:%M:%S,%d/%m/%Y')
        )

        cursor.execute(sql_query, values)
        connection.commit()
        connection.close()
        print ("Udało się pobrać dane")
    else:
        print("Nie udało się pobrać danych")


schedule.every(15).minutes.do(fetch_weather)

while True:
    schedule.run_pending()
    time.sleep(1)
