# news-search-app
A simple search engine to search news built with django and elasticsearch. 

## Prepare Environments
Create and set up a python environment by running the following command in the terminal
```
# create python venv and install libraries in the requirements.txt
source ./create_env
pip install -r requirements.txt
```

## Docker
Since this app depends on the elastic search, rabbitmq, Kibana, Logstash services, it is preferable to use docker compose. 
therefore, before getting started

```
#use docker compose:
source env/bin/activate
docker-compose up -d
```

## Run web app
```
source env/bin/activate
python manage.py runserver 0.0.0.0:8000
```


## migrate schema
```
python manage.py migrate
```


## Run celery worker
```
celery -A news_collection worker -l info
```

## Run celery beat
```
celery -A news_collection beat -l INFO
```
