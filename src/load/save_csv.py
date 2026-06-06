import os

def save_raw(df):

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    df.to_csv(
        "data/raw/raw_coin_data.csv",
        index=False
    )

    print("Raw data saved")


def save_processed(df):

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    df.to_csv(
        "data/processed/coin_data_clean.csv",
        index=False
    )

    print("Processed data saved")