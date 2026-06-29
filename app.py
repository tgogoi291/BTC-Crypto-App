from streamlit_autorefresh import st_autorefresh
import streamlit as st
import requests

# Auto refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

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

    try:
        response = requests.get(url)
        data = response.json()

        if coin in data and "usd" in data[coin]:
            price = data[coin]["usd"]

            if i % 2 == 0:
                with col1:
                    st.metric(symbol, f"${price:,.2f}")
            else:
                with col2:
                    st.metric(symbol, f"${price:,.2f}")
        else:
            st.error(f"{symbol}: Price not available")

    except Exception as e:
        st.error(f"{symbol}: {e}")

st.markdown("---")
st.subheader("Other Markets")

st.info("🥇 XAUTUSD (Gold): Coming Soon")
st.info("💎 VELVETUSD: Coming Soon")
