# Create your tasks here
from __future__ import absolute_import
from celery import Celery
from celery import shared_task

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@shared_task
def send_notification():
    print('Started here!')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
