#!/bin/bash

# Sleep for 5 seconds
echo "Sleeping for 5 seconds"
sleep 5

# Upgrade to the latest revision
echo "Running alembic upgrade head"
alembic upgrade head
