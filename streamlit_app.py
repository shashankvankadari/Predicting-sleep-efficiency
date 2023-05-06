import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load the saved model
model = joblib.load('rf_model.pkl')

# Load the cleaned data
cleaned_data = pd.read_csv('cleaned_data.csv')

st.title("Sleep Efficiency prediction")
# Define the input form
st.markdown("**Enter the following details:**")
age = st.number_input('Age', min_value=1, max_value=99)
gender = st.selectbox('Gender', ['Male', 'Female'])
if gender == 'Male':
    gender = 1
else:
    gender = 0
#bedtime = st.date_input("Bed Time (YYYY-MM-DD)")
#
# Get the time from user input using sliders

st.write("Enter The Hour,Minute,Second, Year,Month,Day to calculate the bed time")
hour = st.slider('Hour', 0, 23)
minute = st.slider('Minute', 0, 59)
second = st.slider('Second', 0, 59)

# Get the date from user input using number input
year = st.number_input('Year', min_value=1900, max_value=2099, step=1)
month = st.number_input('Month', min_value=1, max_value=12, step=1)
day = st.number_input('Day', min_value=1, max_value=31, step=1)

# Convert the time and date to a Unix timestamp
date_time = datetime(year, month, day, hour, minute, second)
unix_timestamp = int(date_time.timestamp())
#
sleep_duration = st.number_input('Sleep Duration (hours)')
rem_percent = st.number_input('REM Sleep Percentage')
deep_percent = st.number_input('Deep Sleep Percentage')
awakenings = st.selectbox('Number of Awakenings', [0, 1, 2, 3])
caffeine = st.number_input('Caffeine Consumption')
alcohol_consumption = st.selectbox("Alcohol Consumption", ["0", "1", "2", "3", "4", "5"])
smoking = st.selectbox('Smoking Status', ['Yes', 'No'])
if smoking == 'Yes':
    smoking = 1
else:
    smoking = 0
exercise_frequency = st.selectbox("Exercise Frequency", ["0", "1", "2", "3", "4", "5"])

# Preprocess the user input
user_input = pd.DataFrame({
    'Age': [age],
    'Gender': [gender],
    'Bedtime': [unix_timestamp],
    'Sleep duration': [sleep_duration],
    'REM sleep percentage': [rem_percent],
    'Deep sleep percentage': [deep_percent],
    'Awakenings': [awakenings],
    'Caffeine consumption': [caffeine],
    'Alcohol consumption': [alcohol_consumption],
    'Smoking status': [smoking],
    'Exercise frequency': [exercise_frequency]
})

# Make predictions using the saved model
prediction = model.predict(user_input)[0]
final_pred = None
if prediction == 1:
  final_pred = 'Best'
elif prediction == 0:
  final_pred = 'Average'

button_clicked = st.button("Click here to predict the sleep efficiency class!")

if button_clicked:
  # Display the predicted output
  st.markdown(f"**Your sleep efficiency is: {final_pred}**")


