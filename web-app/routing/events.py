from app import app
from utils.database import delete_tables, create_tables


@app.on_event("startup")
async def on_startup() -> None:
    await delete_tables()
    await create_tables()