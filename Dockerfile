FROM ghcr.io/astral-sh/uv:0.4.10-python3.12-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && \
    apt-get install -y gcc libuv1-dev git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN uv sync


WORKDIR /bot

CMD ["uv", "run", "granian", "--interface", "asgi", "app:app", "--host", "0.0.0.0",  "--port", "8000", "--loop", "uvloop", "--workers", "1"]
