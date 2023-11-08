from django.db.models import F, Func

def trunc_function(field, period):
    return Func(F(field), function='DATE_TRUNC', aggregation_period=period, template="%(function)s('%(aggregation_period)s', %(expressions)s)")
