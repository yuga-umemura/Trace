dev:
	make -j2 dev-web dev-api

dev-web:
	cd apps/fit-route-web && pnpm dev

dev-api:
	cd apps/fit-route && uv run uvicorn app.main:app --reload --port 8000

migrate:
	cd apps/fit-route && uv run alembic upgrade head

revision:
	cd apps/fit-route && uv run alembic revision --autogenerate -m "$(m)"

seed:
	cd apps/fit-route && uv run python -m app.infrastructure.db.seed.stores

lint-web:
	cd apps/fit-route-web && pnpm lint

lint-api:
	cd apps/fit-route && uv run ruff check .