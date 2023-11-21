from common.utils.where_clause import where_clause, ids
from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from project.models import Project, Feedlinks
from django.http import JsonResponse
import json
import re


def content_volume_top_sources(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = aggregator_results_content_volume_top_sources(posts, widget.aggregation_period, widget.top_counts, pk)
    return JsonResponse(res, safe=False)


def content_volume_top_sources_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)

    return {
        'data': aggregator_results_content_volume_top_sources(posts, widget.aggregation_period, widget.top_counts, pk),
        'widget': {'content_volume_top_sources': model_to_dict(widget)},
        'module_name': 'Online'
    }


def aggregator_results_content_volume_top_sources(posts, aggregation_period, top_counts, pk):
    project = Project.objects.get(id=pk)
    top_sources = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
            SELECT f.id id, f.url url, COUNT(p.feedlink_id) post_count
            FROM project_post p
            JOIN project_project_posts ON p.id = project_project_posts.post_id
            JOIN project_feedlinks f ON p.feedlink_id = f.id
            WHERE {where_clause(posts)}
            GROUP BY f.id
            ORDER BY COUNT(f.id) DESC
            LIMIT {top_counts}
            """
        )
    )

    top_sources = tuple(source.id for source in top_sources)
    content_volume = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
                SELECT feedlink_id id, date, SUM(post_count) FROM (
                SELECT p.feedlink_id, date_trunc('{aggregation_period}', p.entry_published) date, COUNT(p.feedlink_id) post_count
                FROM project_post p
                JOIN project_project_posts ON p.id = project_project_posts.post_id
                WHERE feedlink_id IN {ids(top_sources)} AND {where_clause(posts)}
                GROUP BY p.feedlink_id, date_trunc('{aggregation_period}', p.entry_published)

                UNION

                SELECT id feedlink_id, dates.value date, 0 post_count
                FROM project_feedlinks
                FULL JOIN (SELECT * FROM generate_series('{str(project.start_search_date)}', '{str(project.end_search_date)}', interval '1 {aggregation_period}') s(value)) dates
                ON 1 = 1
                WHERE id IN {ids(top_sources)}
                ) stats
                GROUP BY feedlink_id, date
                ORDER BY feedlink_id, date
                """
        )
    )

    result = [{Feedlinks.objects.get(id=source).source1: []} for source in top_sources]
    for line in content_volume:
        for source in top_sources:
            if line.id == source:
                index = top_sources.index(source)
                result[index][Feedlinks.objects.get(id=source).source1].append({'date': str(line.date), 'post_count': int(line.sum)})
    
    return result


def to_cvs(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = aggregator_results_content_volume_top_sources(posts, widget.aggregation_period, widget.top_counts, pk)
    dates = [str(elem['date']) for elem in list(*result[0].values())]
    fields = ['Source'] + dates
    rows = [[*elem.keys()] + [e['post_count'] for e in list(*elem.values())] for elem in result]
    return fields, rows
