from django.db import models

# Create your models here.
class Quest(models.Model):
    hour_of_day = models.PositiveSmallIntegerField()          # 0-23
    message     = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.hour_of_day:02d}h] {self.message}"