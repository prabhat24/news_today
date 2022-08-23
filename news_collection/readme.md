migrate data
python manage.py migrate

to run elastic search, rabbitmq services
docker-compose up -d

to run celery worker
celery -A news_collection worker -l info


to run celery beat
celery -A news_collection beat -l INFO

runserver
python manage.py runserver 0.0.0.0:8000