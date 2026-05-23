import uuid
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.db.models.store import PriceBand, StoreModel

stores = [
    {
        "slug": "urban-research-shibuya",
        "name": "URBAN RESEARCH 渋谷",
        "area": "渋谷",
        "price_band": PriceBand.MIDDLE,
        "styles": ["simple", "clean", "casual"],
        "colors": ["black", "navy", "gray"],
        "description": "シンプルで大人っぽいカジュアルを探しやすい。",
    },
    {
        "slug": "journal-standard-shibuya",
        "name": "JOURNAL STANDARD 渋谷",
        "area": "渋谷",
        "price_band": PriceBand.MIDDLE,
        "styles": ["casual", "vintage", "american"],
        "colors": ["khaki", "navy", "white"],
        "description": "アメカジ・古着ミックス系が好きな人向け。",
    },
    {
        "slug": "beauty-and-youth-shibuya",
        "name": "BEAUTY&YOUTH 渋谷",
        "area": "渋谷",
        "price_band": PriceBand.MIDDLE,
        "styles": ["clean", "minimal", "date"],
        "colors": ["black", "gray", "beige"],
        "description": "きれいめでデート向きの服を探しやすい。",
    },
    {
        "slug": "freaks-store-shibuya",
        "name": "FREAK'S STORE 渋谷",
        "area": "渋谷",
        "price_band": PriceBand.MIDDLE,
        "styles": ["casual", "street", "relaxed"],
        "colors": ["green", "black", "white"],
        "description": "ゆったりしたカジュアル・ストリート寄り。",
    },
    {
        "slug": "uniqlo-shibuya",
        "name": "UNIQLO 渋谷",
        "area": "渋谷",
        "price_band": PriceBand.LOW,
        "styles": ["basic", "simple", "minimal"],
        "colors": ["black", "white", "gray"],
        "description": "価格を抑えつつベーシックな服を探せる。",
    },
]


def seed_stores(db: Session, store_data: dict) -> None:
    existing_store = (
        db.query(StoreModel).filter(StoreModel.slug == store_data["slug"]).first()
    )

    if existing_store is not None:
        return

    store = StoreModel(
        id=str(uuid.uuid4()),
        slug=store_data["slug"],
        name=store_data["name"],
        area=store_data["area"],
        price_band=store_data["price_band"],
        styles=store_data["styles"],
        colors=store_data["colors"],
        description=store_data["description"],
    )

    db.add(store)


def main() -> None:
    db = SessionLocal()

    try:
        for store in stores:
            seed_stores(db, store)

        db.commit()

        print("Seed completed!")
    except Exception:
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
