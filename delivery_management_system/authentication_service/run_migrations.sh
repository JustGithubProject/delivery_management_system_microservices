#!/bin/bash

echo "Waiting 15 seconds"
sleep 15
# Upgrade to the latest revision
echo "Running alembic upgrade head"
alembic upgrade head
