import streamlit as st
import datetime as dt
import matplotlib.image as mpimg
import requests


st.markdown("# Taxi-fare app    🚖")
st.markdown("### The cheapest way to get around NYC\n ### without getting robbed 💰💰💰")

st.markdown("")
st.markdown("")

taxi_img = mpimg.imread('jfk_taxi_new.jpg')
st.image(taxi_img)

st.markdown("")
st.markdown("")

st.markdown("#### Fill in the following details the press the 'Calculate' button")
col1, col2 = st.columns(2)

date = col1.date_input("Enter a date", dt.date(2019, 7, 6))
time = col1.time_input('Enter a time', dt.time(8, 45))
pickup_datetime = dt.datetime.combine(date, time)

pickup_longitude = col1.number_input("Pickup longitude", step=0.000001, format="%f")
pickup_latitude = col1.number_input("Pickup latitude", step=0.000001, format="%f")
dropoff_longitude = col1.number_input("Dropoff longitude", step=0.000001, format="%f")
dropoff_latitude = col1.number_input("Dropoff latitude", step=0.000001, format="%f")

passenger_count = col1.number_input("Passenger count", step=1, min_value=1, format="%d")

col2.write("")
col2.write("")
NYC_img = mpimg.imread('new_york.jpg')
col2.image(NYC_img)


url = 'https://taxifare.lewagon.ai/predict'

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

response = requests.get(url, params).json()

if st.button("Calculate"):
    st.write('Your estimated fare is', round(response['fare'], 2), '$')

    st.write('')
    st.write('Yeah! Time for some shopping!')

    shopping_img = mpimg.imread('shopping.jpg')
    st.image(shopping_img)
