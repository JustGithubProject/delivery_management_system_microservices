#!/bin/bash

/usr/local/bin/pip install alembic

alembic revision -m "init"

# Upgrade to the latest revision
echo "Running alembic upgrade head"
alembic upgrade head
