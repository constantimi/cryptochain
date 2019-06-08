FROM python:3.6
RUN apt-get update && apt-get install -y vim && apt-get clean

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uwsgi","--http",":8000", "--module", "django_project.wsgi"]
