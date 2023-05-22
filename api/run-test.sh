sudo docker run --name postgresql -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_USER=yemicode -d postgres
sudo docker run --name redis_db -p 6379:6379 -d redis
export FLASK_APP='dts:create_app("development")'

export SECRET_KEY="doNotUseThisInProd"
export DATABASE_URL='postgresql://yemicode:password@localhost:5432/postgres'
export REDIS_URI="redis://localhost:6379/0"

sudo rm migrations/versions/*.py

alembic revision --autogenerate -m "initial migrations"
alembic upgrade head

pip install -r requirements.txt
pytest 

docker stop postgresql
docker stop redis_db
docker system prune -f
