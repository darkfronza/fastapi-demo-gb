from fastapi import FastAPI

from .routers import search, users, auth, sources
from .evhub_client import get_async_client


app = FastAPI()
app.evhub_client = get_async_client()

prefix = "/api/v1"

app.include_router(auth.router)
app.include_router(search.router, prefix=prefix)
app.include_router(users.router, prefix=prefix)
app.include_router(sources.router, prefix=prefix)
