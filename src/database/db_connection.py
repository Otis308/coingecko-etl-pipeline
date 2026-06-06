from sqlalchemy import create_engine

def get_engine():
    DB_USER = "postgres"
    DB_PASSWORD = "11122223845"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "coingecko_db"

    DATABASE_URL = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(DATABASE_URL)
    return engine