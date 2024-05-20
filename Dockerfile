FROM python:3.9-slim

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt


ADD runstring /code/
#ADD .env.docker /code/.env


CMD python manage.py migrate


ENV APP_NAME=RUN_STRING

#RUN pip install -r requirements.txt

CMD gunicorn runstring.wsgi:application -b 0.0.0.0:8000