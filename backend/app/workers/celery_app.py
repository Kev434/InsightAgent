"""
Celery Application Configuration

Sets up the Celery app for background task processing.

TODO:
- Create Celery app instance with Redis as broker and backend
- Configure task serialization (json)
- Configure task routing (optional)
- Set up periodic beat schedule for recurring scrapes

Hints:
    - celery_app = Celery("insightagent", broker=REDIS_URL, backend=REDIS_URL)
    - celery_app.conf.task_serializer = "json"
    - celery_app.conf.result_serializer = "json"
    - celery_app.autodiscover_tasks(["app.workers"])
"""

from celery import Celery

# TODO: Initialize and configure Celery
# celery_app = Celery("insightagent")
