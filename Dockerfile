FROM python:3.13

RUN apt-get update && \
    apt-get install -y curl vim

# Copia o binário do uv
COPY --from=ghcr.io/astral-sh/uv:0.7.9 /uv /uvx /bin/

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .
COPY ./.env.docker .env 

CMD ["sh", "-c", "uv run manage.py makemigrations && uv run manage.py migrate && uv run manage.py runserver 0.0.0.0:8002"]
