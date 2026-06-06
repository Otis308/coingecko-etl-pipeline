import pandas as pd
import requests # Đảm bảo bạn đã cài: pip install requests

def top_marketcap(df):
    try:
        df["market_cap"] = pd.to_numeric(df["market_cap"], errors='coerce')
        
        result = df.sort_values(by="market_cap", ascending=False)
        
        print("\n--- KẾT QUẢ TOP 10 ---")
        print(result[["name", "market_cap"]].head(10))
        return result
    except Exception as e:
        print(f"Lỗi trong hàm xử lý: {e}")
        return None

def get_data_from_coingecko():
    print("Đang gọi API...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print("Lấy dữ liệu thành công!")
        return pd.DataFrame(response.json())
    else:
        print(f"Lỗi API: {response.status_code}")
        return None

if __name__ == "__main__":
    df = get_data_from_coingecko()
    
    if df is not None:
        top_marketcap(df)
    else:
        print("Không có dữ liệu để chạy!")