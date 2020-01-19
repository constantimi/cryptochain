import os

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.conf import settings

from celery import Celery


from django.core.management import call_command
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto.settings')

app = Celery('crypto')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def update_block():
    call_command('pull_bitcoin', version=True)

app.conf.beat_schedule = {
    "update-block-task": {
        "task": "periodic.update_block",
        "schedule": 20.0
    }
}

@periodic_task(run_every=(crontab(minute='*/15')), name="blocks_task", ignore_result=True)
def block_task():
    call_command('pull_bitcoin', version=True)


if __name__ == '__main__':
    app.start()
