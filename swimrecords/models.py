from django.db import models
from .validators import *
from django.core.validators import MinValueValidator

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=255, validators=[validate_stroke])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(auto_now=False, auto_now_add=False, validators=[no_future_date])
    record_broken_date = models.DateTimeField(auto_now=False, auto_now_add=False, validators=[no_break_record_before_set_record])
