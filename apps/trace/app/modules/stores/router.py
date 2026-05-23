from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.modules.stores.repository.impl.sqlalchemy_store_repository import (
    SQLAlchemyStoreRepository,
)
from app.modules.stores.schema import StoreResponse
from app.modules.stores.usecase.get_store import GetStoreUseCase
from app.modules.stores.usecase.list_stores import ListStoresUseCase


router = APIRouter(prefix="/stores", tags=["stores"])


@router.get("", response_model=list[StoreResponse])
def list_stores(db: Session = Depends(get_db)):
    repository = SQLAlchemyStoreRepository(db)
    usecase = ListStoresUseCase(repository)

    return usecase.execute()


@router.get("/{slug}", response_model=StoreResponse)
def get_store(slug: str, db: Session = Depends(get_db)):
    repository = SQLAlchemyStoreRepository(db)
    usecase = GetStoreUseCase(repository)

    store = usecase.execute(slug)

    if store is None:
        raise HTTPException(status_code=404, detail="Store not found")

    return store
