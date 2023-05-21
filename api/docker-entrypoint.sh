#!/bin/bash -x

alembic revision --autogenerate -m "initial migrations" || exit 1
alembic upgrade head || exit 1

exec "$@"

