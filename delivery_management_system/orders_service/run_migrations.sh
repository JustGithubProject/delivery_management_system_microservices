#!/bin/bash

ls -l

pip install alembic


alembic revision -m "init"

alembic upgrade head