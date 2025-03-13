# app/db/DataBase.py

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.cfg import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# false warning supression
# noinspection PyTypeChecker
async_session: sessionmaker[AsyncSession] = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db():
    try:
        async with async_session() as session:
            yield session
    except Exception as e:
        # Handle database session issues
        print(f"Database session error: {str(e)}")
        raise

fake_db_user = {
    "dwa": {"password": "dwa"},
    "user2": {"password": "dwa"}
}

fake_db_sessions = []

