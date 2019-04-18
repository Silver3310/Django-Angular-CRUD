# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def added(movie):
    """Inform that a movie's been added"""
    return f'the "{movie}" was added'


@shared_task
def removed(movie):
    """Inform that a movie's been removed"""
    return f'the "{movie}" was removed'


@shared_task
def changed(movie):
    """Inform that a movie's been changed"""
    return f'the "{movie}" was changed'
