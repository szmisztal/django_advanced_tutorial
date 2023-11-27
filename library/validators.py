from django.core.exceptions import ValidationError

def validate_year(value):
    if value > 2023:
        raise ValidationError("year is gt 2023")
    return value
