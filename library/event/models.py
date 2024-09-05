from datetime import date
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    colour = models.CharField('colour', max_length=25, null=True, blank=True)
    date_event = models.DateField(default=date.today)  # Только дата
    start_time = models.TimeField()  # Время начала события
    end_time = models.TimeField()    # Время окончания события

    def __str__(self):
        return self.title
