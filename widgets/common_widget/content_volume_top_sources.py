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
            SELECT 1 as id, f.source1 source1, COUNT(f.source1) post_count
            FROM project_post p
            JOIN project_project_posts ON p.id = project_project_posts.post_id
            JOIN project_feedlinks f ON p.feedlink_id = f.id
            WHERE {where_clause(posts)}
            GROUP BY f.source1
            ORDER BY COUNT(f.source1) DESC
            LIMIT {top_counts}
            """
        )
    )

    top_sources = tuple(top.source1 for top in top_sources)
    content_volume = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
                SELECT 1 as id, source1, date, SUM(post_count) FROM (
                SELECT f.source1 source1, date_trunc('{aggregation_period}', p.entry_published) date, COUNT(f.source1) post_count
                FROM project_post p
                JOIN project_feedlinks f ON p.feedlink_id = f.id
                JOIN project_project_posts ON p.id = project_project_posts.post_id
                WHERE source1 IN {ids(top_sources)} AND {where_clause(posts)}
                GROUP BY f.source1, date_trunc('{aggregation_period}', p.entry_published)

                UNION

                SELECT source1 feedlink_source1, dates.value date, 0 post_count
                FROM project_feedlinks
                FULL JOIN (SELECT * FROM generate_series(date_trunc('{aggregation_period}','{str(project.start_search_date)}'::timestamptz), date_trunc('{aggregation_period}','{str(project.end_search_date)}'::timestamptz), interval '1 {aggregation_period}') s(value)) dates
                ON 1 = 1
                WHERE source1 IN {ids(top_sources)}
                ) stats
                GROUP BY source1, date
                ORDER BY source1, date
                """
        )
    )

    result = [{Feedlinks.objects.filter(source1=source).first().source1: []} for source in top_sources]
    for line in content_volume:
        for source1 in top_sources:
            if line.source1 == source1:
                index = top_sources.index(source1)
                result[index][source1].append({'date': str(line.date), 'post_count': int(line.sum)})
    
    return result


def to_cvs(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = aggregator_results_content_volume_top_sources(posts, widget.aggregation_period, widget.top_counts, pk)
    dates = [str(elem['date']) for elem in list(*result[0].values())]
    fields = ['Source'] + dates
    rows = [[*elem.keys()] + [e['post_count'] for e in list(*elem.values())] for elem in result]
    return fields, rows
