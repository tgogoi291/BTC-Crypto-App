import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="BTC & Crypto App", layout="wide")

st.title("📈 Market Watch")

coins = {
    "BTCUSD": "bitcoin",
    "ETHUSD": "ethereum",
    "SOLUSD": "solana"
}

col1, col2 = st.columns(2)

for i, (symbol, coin) in enumerate(coins.items()):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    data = requests.get(url).json()
    price = data[coin]["usd"]

    if i % 2 == 0:
        with col1:
            st.metric(symbol, f"${price:,.2f}")
    else:
        with col2:
            st.metric(symbol, f"${price:,.2f}")

st.markdown("---")

st.subheader("Other Markets")

st.info("🥇 XAUTUSD (Gold): Coming Soon")
st.info("💎 VELVETUSD: Coming Soon")
