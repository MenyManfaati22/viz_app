import pandas as pd
import streamlit as st
st.title("Welcome to Meny Web App")
st.header("Book Your Data Analytics Consulting")

check_on = st.checkbox("Check to book a consultation")
if check_on:
    st.write("Thank you for booking a consultation with us!")
else:
    st.write("Please check the box to book a consultation")

user_name = st.text_input("Enter your name")
if user_name:
    st.write(f"Hello, {user_name}! We are glad to have you here")

user_email = st.text_input("Enter your email address")
if user_email:
    st.write(f"Thank you for providing your email: {user_email}")

import pandas as pd
import streamlit as st
data = pd.read_csv("iris_data.csv")

import plotly.express as px
fig = px.scatter(data, x="SepalLengthCm", y="SepalWidthCm", color="Species")
st.plotly_chart(fig, use_container_width=True)