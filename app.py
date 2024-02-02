import streamlit as st
import requests

FASTAPI_BACKEND_URL = "http://localhost:8000/weather/"

st.title('test weather API')

location = st.text_input('Enter a location:', '')

if st.button('Get Weather'):
    if location:
        response = requests.get(FASTAPI_BACKEND_URL, params={"location": location})
        if response.status_code == 200:
            weather_data = response.json()
            st.write(f"Weather in {location} is {weather_data['weather'][0]['description']}.")  # e.g. "clear sky"
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Feels like: {weather_data['main']['feels_like']}°C")
            st.write(f"Min temperature: {weather_data['main']['temp_min']}°C")
            st.write(f"Max temperature: {weather_data['main']['temp_max']}°C")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            
        else:
            st.error("Failed to retrieve weather data.")
    else:
        st.error("Please enter a location.")
