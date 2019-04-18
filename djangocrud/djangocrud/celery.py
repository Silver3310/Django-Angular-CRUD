from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrud.settings.base')

app = Celery('djangocrud')

app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
