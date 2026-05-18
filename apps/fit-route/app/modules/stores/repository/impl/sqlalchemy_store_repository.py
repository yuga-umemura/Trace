from sqlalchemy.orm import Session

from app.infrastructure.db.models.store import StoreModel
from app.modules.stores.domain.stores import Store
from app.modules.stores.repository.impl.store_mapper import to_entity
from app.modules.stores.repository.store_repository import StoreRepository


class SQLAlchemyStoreRepository(StoreRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_stores(self) -> list[Store]:
        stores = self.db.query(StoreModel).all()

        return [to_entity(store) for store in stores]

    def get_store_by_slug(self, slug) -> Store | None:
        store = self.db.query(StoreModel).filter(StoreModel.slug == slug).first()

        if store is None:
            return None

        return to_entity(store)
