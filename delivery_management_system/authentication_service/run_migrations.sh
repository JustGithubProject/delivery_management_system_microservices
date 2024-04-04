#!/bin/bash

cd /auth_app

alembic revision -m "init"

alembic upgrade head