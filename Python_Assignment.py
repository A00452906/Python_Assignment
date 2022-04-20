import pandas as pd
import matplotlib.pyplot as plt
import requests
import streamlit as st


API_URL="https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=cad&days=90&interval=daily"

st.title("Bitcoin prices")
days=st.slider('No. of Days', min_value=1, max_value=365, value=90)

currencyList = ['CAD','USD', 'INR']
currency = st.radio('Currency',currencyList)

payload = {'vs_currency': currency,'days': days,'interval':'daily'}


req = requests.get(API_URL, payload)
if(req.status_code==200):
    data=req.json()
raw_data = data['prices']
dataFrame = pd.DataFrame(data=raw_data, columns=['Date','Price'])
dataFrame['Date'] = pd.to_datetime(dataFrame['Date'], unit='ms')

fig, ax = plt.subplots(figsize=(16,6))
ax.plot(dataFrame['Date'], dataFrame['Price'])
ax.set_ylim(ymin=0)
ax.set_xlabel('Date', fontsize=18)
ax.set_ylabel("Price",fontsize=18)
st.pyplot(fig)

st.text(f"Average price {dataFrame['Price'].mean()} {currency.upper()}")