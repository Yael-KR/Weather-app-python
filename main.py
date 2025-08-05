import streamlit as st
import requests
from datetime import datetime

#כותרת
st.title("Welcome to the Weather App")

#שם המשתמש
user_name = st.text_input("What's your name?", "")

if user_name:
    st.write(f"Nice to meet you, **{user_name}**! ")
    st.markdown("---")

    #הזנת שם העיר ודוגמה לשם עיר
    city = st.text_input("Enter a city name:", placeholder="e.g. Tel Aviv")

#בדיקה שהכל התחבר תקין וסטטוס תקין
    if st.button("Get Weather"):
        # API
        API_KEY = "7f18c94bd1b1789e11380bc490f51bc3"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()

            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            city_name = data['name']
            now = datetime.now().strftime("%d/%m/%Y %H:%M")

            # הצגת התוצאות
            st.markdown(f"### Weather in **{city_name}** at **{now}** is")
            st.write(f"🌡Temperature: **{temp}°C**")
            st.write(f"Feels like: **{feels_like}°C**")
            st.write(f"Humidity: **{humidity}%**")
            st.write(f"Condition: **{description.capitalize()}**")

            # המלצה לפי טמפרטורה
            recommendation = ""
            # המלצה לפי טמפרטורה
            if temp <= 0:
                recommendation = "Freezing temperatures! Better to stay indoors if you can."
            elif temp <= 5:
                recommendation = "It's very cold! Wear warm clothes and stay safe."
            elif temp <= 15:
                recommendation = "Chilly weather. A light jacket might be a good idea."
            elif temp <= 25:
                recommendation = "Pleasant weather. Enjoy your day!"
            elif temp <= 30:
                recommendation = "It's warm. Stay hydrated and wear sunscreen."
            elif temp <= 35:
                recommendation = "Hot weather. Drink water and avoid long exposure to the sun."
            else:
                recommendation = "Extremely hot! Try to stay in cool places and drink plenty of water."

            st.markdown(f"\n**{recommendation}**")


        else:
            st.error("🚫 City not found. Please enter a valid city name.")
