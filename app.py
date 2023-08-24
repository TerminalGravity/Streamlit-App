import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simulating the data
# Replace this with actual data loading from CSV or other sources
def generate_data():
    dates = pd.date_range('2021-01-01', periods=12, freq='M')
    inflation_ireland = [1.5, 1.2, 1.3, 1.4, 1.6, 1.7, 1.5, 1.3, 1.4, 1.5, 1.6, 1.7]
    inflation_us = [1.3, 1.5, 1.4, 1.6, 1.5, 1.4, 1.3, 1.5, 1.4, 1.6, 1.5, 1.4]
    df = pd.DataFrame({'Date': dates, 'Ireland': inflation_ireland, 'US': inflation_us})
    return df

# Title
st.title("Month-over-Month Inflation Comparison: Ireland vs US")

# Description
st.write("""
This chart represents the rolling month-over-month inflation rates for Ireland and the United States.
""")

# Loading data
data = generate_data()

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['Date'], data['Ireland'], label="Ireland", marker='o')
ax.plot(data['Date'], data['US'], label="US", marker='x')
plt.title('MoM Inflation Comparison')
plt.xlabel('Date')
plt.ylabel('Inflation Rate (%)')
plt.legend()
plt.grid(True)

# Display the plot
st.pyplot(fig)
