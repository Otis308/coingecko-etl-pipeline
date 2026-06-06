# Chỉ cần import get_engine là đủ
from src.database.db_connection import get_engine

def save_to_postgres(df):
    try:
        engine = get_engine()
        
        df.to_sql(
            name = "coin_market",
            con = engine,
            if_exists = "append",
            index = False,
        )
        
        print("Đã đẩy dữ liệu vào bảng coin_market thành công!")
        print('Data saved to PostgreSQL')

    except Exception as e:
        print(f"Có lỗi xảy ra khi đẩy dữ liệu: {e}")