#!/bin/bash

pip install alembic

alembic revision -m "init"

alembic upgrade head