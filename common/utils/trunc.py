from django.db.models import F, Func

def trunc(field, interval):
    return Func(F(field), function='DATE_TRUNC', interval=interval, template="%(function)s('%(interval)s', %(expressions)s)")
