FROM python:3.10

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /delivery_app

COPY . .

RUN pip install -r requirements.txt


RUN python3 setup_database.py


EXPOSE 8004

CMD ["uvicorn", "main:delivery_app", "--host", "0.0.0.0", "--port", "8004", "--reload"]
