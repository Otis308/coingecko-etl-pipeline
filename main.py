from src.extract.coingecko_api import get_top_coins
from src.transform.clean_data import clean_coin_data
from src.load.save_csv import (save_raw, save_processed)
from src.load.save_postgres import save_to_postgres
from datetime import datetime

def main():

    print("Extracting data...")

    raw_df = get_top_coins()

    save_raw(raw_df)

    print("Transforming data...")

    clean_df = clean_coin_data(raw_df)
    clean_df = clean_df.rename(columns={'id': 'coin_id'})
    clean_df['snapshot_date'] = datetime.now().date()

    save_processed(clean_df)

    print("Pipeline completed")

    save_processed(clean_df)
    save_to_postgres(clean_df)

if __name__ == "__main__":
    main()