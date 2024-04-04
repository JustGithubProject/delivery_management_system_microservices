#!/bin/bash

cd /delivery_app

alembic revision -m "init"

alembic upgrade head