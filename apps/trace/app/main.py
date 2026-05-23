from fastapi import FastAPI
from app.modules.stores.router import router as store_router

app = FastAPI()

app.include_router(store_router)


@app.get("/health")
def health():
    return {"status": "ok"}
