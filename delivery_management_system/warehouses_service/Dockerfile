FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /warehouse_app
WORKDIR /warehouse_app

COPY . .

RUN pip install -r requirements.txt




EXPOSE 8003

RUN chmod +x run_migrations.sh


CMD ["sh", "-c", "./run_migrations.sh"]
