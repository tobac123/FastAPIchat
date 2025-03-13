from decouple import config

DATABASE_URL = (
    f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}"
    f"@{config('POSTGRES_HOST')}:{config('POSTGRES_PORT')}/{config('POSTGRES_DB')}"
)