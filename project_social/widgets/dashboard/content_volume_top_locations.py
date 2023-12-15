from project_social.widgets.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from common.utils.trunc import trunc
from django.http import JsonResponse
from django.db.models import Count
import json


def content_volume_top_locations(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_for_content_volume_top_locations(posts, widget.aggregation_period, widget.top_counts)
    return JsonResponse(res, safe=False)


def content_volume_top_locations_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_content_volume_top_locations(posts, widget.aggregation_period, widget.top_counts),
        'widget': {'content_volume_top_locations': model_to_dict(widget)},
        'module_name': 'Social'
    }


def calculate_for_content_volume_top_locations(posts, aggregation_period, top_counts):
    top_locations = list(map(lambda x: x['country'], list(posts.values('country').annotate(country_count=Count('country')).order_by('-country_count')[:top_counts])))
    results = [{location: list(posts.filter(country=location).annotate(date_trunc=trunc('date', aggregation_period)).values("date_trunc").annotate(created_count=Count('id')).order_by("date"))} for location in top_locations]
    dates = set()
    for elem in range(len(results)):
        for i in range(len(results[elem][top_locations[elem]])):
            dates.add(str(results[elem][top_locations[elem]][i]['date_trunc']))
    res = []
    for elem in range(len(results)):
        list_dates = []
        for date in sorted(list(dates)):
            count = 0
            if date in sorted(list({str(results[elem][top_locations[elem]][i]['date_trunc']) for i in range(len(results[elem][top_locations[elem]]))})):
                for i in range(len(results[elem][top_locations[elem]])):
                    if date == str(results[elem][top_locations[elem]][i]['date_trunc']):
                        count += results[elem][top_locations[elem]][i]['created_count']
                list_dates.append({"date": date, "post_count": count})
            else:
                list_dates.append({"date": date, "post_count": 0})
        res.append({top_locations[elem]: list_dates})
    return res


def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_content_volume_top_locations(posts, widget.aggregation_period, widget.top_counts)
    dates = [str(elem['date']) for elem in list(*result[0].values())]
    fields = ['Location'] + dates
    rows = [[*elem.keys()] + [e['post_count'] for e in list(*elem.values())] for elem in result]
    return fields, rows
