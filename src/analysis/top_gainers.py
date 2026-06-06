def top_gainers(df):

    result = df.sort_values(
        by="price_change_percentage_24h",
        ascending=False
    )

    print("\nTOP GAINERS")

    print(
        result[
            [
                "name",
                "price_change_percentage_24h"
            ]
        ].head(10)
    )