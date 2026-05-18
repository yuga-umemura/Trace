from app.modules.stores.domain.stores import Store
from app.modules.stores.repository.store_repository import StoreRepository


class ListStoresUseCase:
    def __init__(self, store_repository: StoreRepository) -> None:
        self.store_repository = store_repository

    def execute(self) -> list[Store]:
        return self.store_repository.list_stores()
