FROM python:3.10.2-alpine3.14

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
    
RUN pip install -r /requirements.txt

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


