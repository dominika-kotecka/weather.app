import requests
import mysql.connector

API_KEY = "912c622485ebcccfe6e75ebb3dc2de10"
API_CITY = "Kraków"
API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}&appid={API_KEY}&units=metric&lang=pl"

response = requests.get(API_ENDPOINT)

if response.status_code == 200:
    data = response.json()
    print(data)

    # db connection
    connection = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password="",
        database="pogoda"
    )

    cursor = connection.cursor()

    sql_query = "INSERT INTO krakow (tamp,min_temp,max_temp, humiditi,presure, desc) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (
        data["main"]["temp"],
        data["main"]["temp_min"],
        data["main"]["temp_max"],
        data["main"]["humidity"],
        data["main"]["pressure"],
        data["weather"][0]["description"],
    )

    cursor.execute(sql_query, values)
    connection.commit()
    connection.close()
else:
    print("Nie udało się pobrać danych")
