FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /delivery_app
WORKDIR /delivery_app

COPY . .

RUN pip install -r requirements.txt


EXPOSE 8004

RUN chmod +x run_migrations.sh
RUN chmod +x wait-for-it.sh


CMD ["sh", "-c", "./wait-for-it.sh localhost:5434 -- ./run_migrations.sh && uvicorn main:delivery_app --host 0.0.0.0 --port 8004 --reload"]

