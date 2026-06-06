import streamlit as st
import pandas as pd

# --- BƯỚC 1: Cấu hình ---
st.set_page_config(page_title="Crypto Analytics Dashboard", layout="wide")

st.title("🚀 CoinGecko Real-time Analytics Dashboard")
st.markdown("---")

# --- BƯỚC 2: Đọc dữ liệu ---
@st.cache_data 
def load_data():
    return pd.read_csv("data/raw/raw_coin_data.csv")

try:
    df = load_data()

    col1, col2, col3 = st.columns(3)
    col1.metric("Tổng số Coin", len(df))
    col2.metric("Vốn hóa cao nhất", f"${df['market_cap'].max():,.0f}")
    col3.metric("Giá BTC hiện tại", f"${df[df['symbol']=='btc']['current_price'].values[0]:,.0f}")

    st.markdown("---")

    # --- BƯỚC 4: Vẽ biểu đồ ---
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("📊 Top 10 Vốn hóa (Biểu đồ Cột)")
        top_10_cap = df.nlargest(10, 'market_cap')
        st.bar_chart(data=top_10_cap, x='name', y='market_cap', color="#29b5e8")

    with chart_col2:
        st.subheader("📈 Biến động giá 24h (Biểu đồ Miền)")
        # Sắp xếp theo phần trăm thay đổi để xem độ biến động
        st.area_chart(data=df.set_index('name')['price_change_percentage_24h'].head(20), color="#ff4b4b")

    st.markdown("---")

    # --- BƯỚC 5: Bảng dữ liệu chi tiết---
    st.subheader("📑 Bảng dữ liệu chi tiết")
    
    st.dataframe(
        df, 
        use_container_width=True, 
        column_config={
            "image": st.column_config.ImageColumn("Logo", help="Coin Logo"),
            "market_cap": st.column_config.NumberColumn("Vốn hóa", format="$%d"),
            "current_price": st.column_config.NumberColumn("Giá hiện tại", format="$%.2f"),
        },
        hide_index=True
    )

except FileNotFoundError:
    st.error("Không tìm thấy file 'raw_coin_data.csv'. Vui lòng kiểm tra lại vị trí file!")
except Exception as e:
    st.error(f"Lỗi: {e}")