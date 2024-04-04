#!/bin/bash

cd /authentication_service

alembic revision -m "init"

alembic upgrade head