from app.modules.stores.domain.stores import Store
from app.modules.stores.repository.store_repository import StoreRepository


class GetStoreUseCase:
    def __init__(self, store_repository: StoreRepository) -> None:
        self.store_repository = store_repository

    def execute(self, slug: str) -> Store | None:
        return self.store_repository.get_store_by_slug(slug)
