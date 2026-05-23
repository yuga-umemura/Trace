import enum

from sqlalchemy import ARRAY, Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.db.base import Base


class PriceBand(str, enum.Enum):
    LOW = "Low"
    MIDDLE = "Middle"
    HIGH = "High"


class StoreModel(Base):
    __tablename__ = "stores"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    slug: Mapped[str] = mapped_column(String, unique=True, index=True)

    name: Mapped[str] = mapped_column(String)

    area: Mapped[str] = mapped_column(String)

    address: Mapped[str | None] = mapped_column(String, nullable=True)

    map_url: Mapped[str | None] = mapped_column(String, nullable=True)

    price_band: Mapped[PriceBand] = mapped_column(Enum(PriceBand))

    styles: Mapped[list[str]] = mapped_column(ARRAY(String))

    colors: Mapped[list[str]] = mapped_column(ARRAY(String))

    description: Mapped[str | None] = mapped_column(String, nullable=True)
