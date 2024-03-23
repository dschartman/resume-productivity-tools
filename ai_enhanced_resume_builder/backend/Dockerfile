FROM python:3.12-slim

WORKDIR /code

COPY pyproject.toml poetry.lock* /code/

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /code/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]
