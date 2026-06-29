import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Nifty + Sensex + BTC Dashboard", layout="wide")

st.title("📈 Nifty + Sensex + BTC Dashboard")

coin = st.selectbox(
    "Select Crypto",
    ["bitcoin", "ethereum", "solana", "dogecoin"]
)

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr"

try:
    data = requests.get(url).json()

    usd = data[coin]["usd"]
    inr = data[coin]["inr"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("USD Price", f"${usd:,.2f}")

    with col2:
        st.metric("INR Price", f"₹{inr:,.2f}")

    st.success("🟢 BUY Signal (Demo)")
    st.info("Target: +2%")
    st.error("Stop Loss: -1%")

except:
    st.error("Unable to fetch live price.")

st.divider()

st.subheader("📊 Market Watch")

market = pd.DataFrame({
    "Index": ["NIFTY 50", "SENSEX", "BANK NIFTY"],
    "Signal": ["BUY", "SELL", "BUY"]
})

st.dataframe(market, use_container_width=True)
