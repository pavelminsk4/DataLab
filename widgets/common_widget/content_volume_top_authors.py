from common.utils.where_clause import where_clause, multi_or_single_typle
from .project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
from project.models import Project
import json
import re


def content_volume_top_authors(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    body = json.loads(request.body)
    aggregation_period = body['aggregation_period']
    res = aggregator_results_content_volume_top_authors(posts, aggregation_period, widget.top_counts, pk)
    return JsonResponse(res, safe = False)

def content_volume_top_authors_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': aggregator_results_content_volume_top_authors(posts, widget.aggregation_period, widget.top_counts, pk),
        'widget': {'content_volume_top_authors': model_to_dict(widget)},
        'module_name': 'Online'
    }

def aggregator_results_content_volume_top_authors(posts, aggregation_period, top_counts, pk):
    project = Project.objects.get(id=pk)
    top_authors = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
            SELECT 1 as id, p.entry_author, COUNT(p.entry_author) post_count
            FROM project_post p
            JOIN project_project_posts ON p.id = project_project_posts.post_id
            WHERE {where_clause(posts)}
            GROUP BY p.entry_author
            ORDER BY COUNT(p.entry_author) DESC
            LIMIT {top_counts}
            """
        )
    )

    top_authors = tuple(author.entry_author for author in top_authors)
    content_volume = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
                SELECT 1 as id, entry_author, date, SUM(post_count) FROM (
                SELECT p.entry_author, date_trunc('{aggregation_period}', p.entry_published) date, COUNT(p.entry_author) post_count
                FROM project_post p
                JOIN project_project_posts ON p.id = project_project_posts.post_id
                WHERE entry_author IN {multi_or_single_typle(top_authors)} AND {where_clause(posts)}
                GROUP BY p.entry_author, date_trunc('{aggregation_period}', p.entry_published)

                UNION

                SELECT entry_author, dates.value date, 0 post_count
                FROM project_post
                FULL JOIN (SELECT * FROM generate_series('{str(project.start_search_date)}', '{str(project.end_search_date)}', interval '1 {aggregation_period}') s(value)) dates
                ON 1 = 1
                WHERE entry_author IN {multi_or_single_typle(top_authors)}
                ) stats
                GROUP BY entry_author, date
                ORDER BY entry_author, date
                """
        )
    )

    result = [{author: []} for author in top_authors]
    for line in content_volume:
        for author in top_authors:
            if line.entry_author == author:
                index = top_authors.index(author)
                result[index][author].append({'date': str(line.date), 'post_count': int(line.sum)})

    return result
