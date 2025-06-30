from django.utils import timezone
from celery import shared_task
from .models import Quest

@shared_task
def execute_quest(message, quest_id):
    print(f"💬 Quest {quest_id}: {message}")

@shared_task
def check_and_run_quests():
    now  = timezone.localtime()
    hour = now.hour                       # e.g. 3 for 3 AM
    quests = Quest.objects.filter(hour_of_day=hour)
    for q in quests:
        execute_quest.delay(q.message, q.id)
