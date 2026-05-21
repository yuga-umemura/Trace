from abc import ABC, abstractmethod

from app.modules.stores.domain.stores import Store


class StoreRepository(ABC):
    @abstractmethod
    def list_stores(self) -> list[Store]:
        pass

    @abstractmethod
    def get_store_by_slug(self, slug: str) -> Store | None:
        pass
