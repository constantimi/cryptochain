FROM python:3.6

WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get install -y vim
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

EXPOSE 8000

CMD ["uwsgi","--http",":8000", "--module", "django_project.wsgi"]
