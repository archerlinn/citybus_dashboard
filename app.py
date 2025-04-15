import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app setup
st.title("CityBus Monthly Report Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload a monthly CityBus CSV file", type=["csv"])

# Month input
month_input = st.text_input("Enter the month for the uploaded data (e.g., January 2023)")

if uploaded_file and month_input:
    # Load CSV file
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces

    # Clean necessary columns
    df['Passengers'] = df['Passengers'].replace(',', '', regex=True).replace(['-', ' - ', ' '], pd.NA)
    df['Revenue'] = df['Revenue'].replace(',', '', regex=True).replace(['-', ' - ', ' '], pd.NA)

    df['Passengers'] = pd.to_numeric(df['Passengers'], errors='coerce')
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

    # Drop rows with missing route names or values
    df = df.dropna(subset=['RouteName', 'Passengers', 'Revenue'])

    st.subheader(f"📊 Total Passengers per Route - {month_input}")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.barh(df['RouteName'], df['Passengers'], color='skyblue')
    ax1.set_xlabel("Number of Passengers")
    ax1.set_title("Passengers per Route")
    ax1.invert_yaxis()
    st.pyplot(fig1)

    st.subheader(f"💰 Total Revenue per Route - {month_input}")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.barh(df['RouteName'], df['Revenue'], color='orange')
    ax2.set_xlabel("Revenue ($)")
    ax2.set_title("Revenue per Route")
    ax2.invert_yaxis()
    st.pyplot(fig2)

    st.success("Charts generated successfully!")

else:
    st.info("Please upload a CSV file and enter the corresponding month.")
