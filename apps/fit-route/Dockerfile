FROM public.ecr.aws/docker/library/python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir uv

FROM base AS builder

COPY apps/fit-route/pyproject.toml apps/fit-route/uv.lock ./apps/fit-route/

WORKDIR /app/apps/fit-route

RUN uv sync --frozen --no-dev

FROM base AS runner

RUN addgroup --system --gid 1001 app
RUN adduser --system --uid 1001 --ingroup app app

COPY --from=builder /app/apps/fit-route/.venv /app/apps/fit-route/.venv
COPY --chown=app:app apps/fit-route/app /app/apps/fit-route/app
COPY --chown=app:app apps/fit-route/alembic /app/apps/fit-route/alembic
COPY --chown=app:app apps/fit-route/alembic.ini /app/apps/fit-route/alembic.ini
COPY --chown=app:app apps/fit-route/pyproject.toml /app/apps/fit-route/pyproject.toml

WORKDIR /app/apps/fit-route

ENV PATH="/app/apps/fit-route/.venv/bin:$PATH"

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]