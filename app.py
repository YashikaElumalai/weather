import streamlit as st
import pandas as pd

st.title("🌤️ Weather Dataset App (No API)")

# Load dataset
df = pd.read_csv("weather.csv")

# Sidebar filters
city = st.selectbox("Select City", df["city"].unique())

# Filter data
filtered_df = df[df["city"] == city]

st.subheader(f"Weather Data for {city}")

# Show table
st.dataframe(filtered_df)

# Show details
if st.button("Show Latest Weather"):
    latest = filtered_df.iloc[-1]

    st.success(f"Latest Weather in {city}")
    st.write(f"🌡️ Temperature: {latest['temperature']}°C")
    st.write(f"💧 Humidity: {latest['humidity']}%")
    st.write(f"☁️ Condition: {latest['condition']}")
    st.write(f"📅 Date: {latest['date']}")
