import streamlit as st
import requests

st.set_page_config(page_title="BTC & Crypto App", layout="wide")

st.title("📈 BTC & Crypto Live Price")
st.write("Live Bitcoin price using CoinGecko API")

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,inr"

try:
    data = requests.get(url).json()

    usd = data["bitcoin"]["usd"]
    inr = data["bitcoin"]["inr"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Bitcoin Price (USD)", f"${usd:,.2f}")

    with col2:
        st.metric("Bitcoin Price (INR)", f"₹{inr:,.2f}")

except Exception:
    st.error("Unable to fetch live price.")
