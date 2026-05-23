dev:
	make -j2 dev-web dev-api

dev-web:
	cd apps/trace-web && pnpm dev

dev-api:
	cd apps/trace && uv run uvicorn app.main:app --reload --port 8000

migrate:
	cd apps/trace && uv run alembic upgrade head

revision:
	cd apps/trace && uv run alembic revision --autogenerate -m "$(m)"

seed:
	cd apps/trace && uv run python -m app.infrastructure.db.seed.stores

lint: lint-web lint-api

lint-web:
	cd apps/trace-web && pnpm lint

lint-api:
	cd apps/trace && uv run ruff check .

format: format-web format-api

format-web:
	cd apps/trace-web && pnpm format

format-api:
	cd apps/trace && uv run ruff format .