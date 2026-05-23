from pydantic import BaseModel


class StoreResponse(BaseModel):
    id: str

    slug: str

    name: str

    area: str

    address: str | None

    map_url: str | None

    price_band: str

    styles: list[str]

    colors: list[str]

    description: str | None
