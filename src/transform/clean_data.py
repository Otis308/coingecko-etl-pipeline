from datetime import datetime
from src.utils.logger import logger

def clean_coin_data(df):
    try:
        columns = [
            "id",
            "symbol",
            "name",
            "market_cap",
            "current_price",
            "circulating_supply",
            "price_change_percentage_24h"
        ]
        df = df[columns]

        #Check đủ số dòng cần clean ko ?
        logger.info(
            f"Rows before clean: {len(df)}"
        )

        # Check số lượng null cho từng cột
        # Ghi log 
        logger.info(
            f"Rows: {len(df)}"
        )

        logger.info(
            f"Duplicates: {df.duplicated().sum()}"
        )

        logger.info(
            f"Missing market_cap: "
            f"{df['market_cap'].isnull().sum()}"
        )

        logger.info(
            f"Missing current_price: "
            f"{df['current_price'].isnull().sum()}"
        )

        missing_percent = (
            df.isnull().sum()
            / len(df)
            * 100
        )

        logger.info(
            f"Missing percentage:\n{missing_percent}"
        )

        #Check dupliacate
        duplicate_count = df.duplicated().sum()
        logger.warning(f"Duplicate row: {duplicate_count}")
        df = df.drop_duplicates()

        df["price_change_percentage_24h"] = (
            df["price_change_percentage_24h"].fillna(0)
        )

        logger.info(
            f"Rows after clean: {len(df)}"
        )

        #Check negative price
        negative_price = (
            df["current_price"] < 0
        ).sum()

        logger.info(
            f"Negative prices: {negative_price}"
        )
        logger.info("\n=====================================================")
        if len(df) == 0:
            raise ValueError(
            "Dataset is empty"
        )
        if df["current_price"].isnull().all():
            raise ValueError(
            "current_price column is completely null"
        )
        return df
    except Exception as e:
        
        logger.error(
            f"Clean step failed: {e}"
        )
        raise Exception("Test error")
