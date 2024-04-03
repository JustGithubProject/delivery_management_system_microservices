FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /warehouse_app
WORKDIR /warehouse_app

COPY . .

RUN pip install -r requirements.txt

RUN python3 setup_database.py

EXPOSE 8003

CMD ["uvicorn", "main:warehouse_app", "--host", "0.0.0.0", "--port", "8003", "--reload"]
