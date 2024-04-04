#!/bin/bash

cd /order_app

alembic revision -m "init"

alembic upgrade head