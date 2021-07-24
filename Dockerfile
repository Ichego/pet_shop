# pull official base image
FROM python:3.8.3-alpine

# set work directory

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN rm -rf  ./requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project

COPY . .
COPY ./entrypoint.sh .
RUN ["chmod", "+x", "./entrypoint.sh"]


RUN python manage.py collectstatic --no-input

ENTRYPOINT ["./entrypoint.sh"]
