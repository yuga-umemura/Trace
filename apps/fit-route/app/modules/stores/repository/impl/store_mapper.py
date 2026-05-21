from app.infrastructure.db.models.store import StoreModel
from app.modules.stores.domain.stores import Store


def to_entity(model: StoreModel) -> Store:
    return Store(
        id=model.id,
        slug=model.slug,
        name=model.name,
        area=model.area,
        address=model.address,
        map_url=model.map_url,
        price_band=model.price_band.value,
        styles=model.styles,
        colors=model.colors,
        description=model.description,
    )
