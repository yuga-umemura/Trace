FROM public.ecr.aws/docker/library/python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir uv

FROM base AS builder

COPY apps/trace/pyproject.toml apps/trace/uv.lock ./apps/trace/

WORKDIR /app/apps/trace

RUN uv sync --frozen --no-dev

FROM base AS runner

RUN addgroup --system --gid 1001 app
RUN adduser --system --uid 1001 --ingroup app app

COPY --from=builder /app/apps/trace/.venv /app/apps/trace/.venv
COPY --chown=app:app apps/trace/app /app/apps/trace/app
COPY --chown=app:app apps/trace/alembic /app/apps/trace/alembic
COPY --chown=app:app apps/trace/alembic.ini /app/apps/trace/alembic.ini
COPY --chown=app:app apps/trace/pyproject.toml /app/apps/trace/pyproject.toml

WORKDIR /app/apps/trace

ENV PATH="/app/apps/trace/.venv/bin:$PATH"

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]