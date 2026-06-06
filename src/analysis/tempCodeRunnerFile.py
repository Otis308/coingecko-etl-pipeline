def top_marketcap(df):

    result = df.sort_values(
        by="market_cap",
        ascending=False
    )

    print("\nTOP MARKET CAP")

    print(
        result[
            ["name", "market_cap"]
        ].head(10)
    )

    return result
