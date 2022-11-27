from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone

def validate_stroke(stroke):
    if stroke not in ['front crawl', 'butterfly', 'breast', 'back','freestyle']:
        raise ValidationError(f'{stroke} is not a valid stroke')

def no_future_date(input_record_date):
    today = timezone.now()
    if input_record_date > today:
        raise ValidationError("Can't set record in the future.")

def no_break_record_before_set_record(record_broken_date):
    record_date=timezone.now()
    record_broken_date=(timezone.now() - timedelta(days=1))
    if record_broken_date < record_date:
        raise ValidationError("Can't break record before record was set.")

