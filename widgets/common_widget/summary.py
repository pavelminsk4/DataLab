from .project_posts_filter import project_posts_filter
from common.utils.where_clause import where_clause
from django.forms.models import model_to_dict
from django.http import JsonResponse
from project.models import Post
import re


def summary_widget(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_summary_widget(posts)
    return JsonResponse(res, safe=False)
  
def summary_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_summary_widget(posts),
        'widget': {'summary': model_to_dict(widget)},
        'module_name': 'Online'
    }

def calculate_summary_widget(posts):
    potential_reach = posts.order_by('-feedlink__alexaglobalrank')[0].feedlink.alexaglobalrank if posts else 0
    
    posts_count = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
            SELECT 1 as id, COUNT(p.id) count
            FROM project_post p
            LEFT JOIN project_project_posts ON (p.id = project_project_posts.post_id) 
            LEFT JOIN project_feedlinks ON (p.feedlink_id = project_feedlinks.id) 
            WHERE {where_clause(posts)}
            """
        )
    )
    
    sentiment_query = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
                SELECT 1 as id, p.sentiment, COUNT(p.sentiment) sentiment_count, COUNT(p.id) post_count
                FROM project_post p
                LEFT JOIN project_project_posts ON p.id = project_project_posts.post_id
                WHERE {where_clause(posts)}
                GROUP BY p.sentiment
            """
        )
    )
    sentiment = {x.sentiment: x.sentiment_count for x in sentiment_query}
    
    source_count = posts.raw(query_for_post_feedlink('source1', posts))
    
    location_count = posts.raw(query_for_post_feedlink('country', posts))
    
    author_count = posts.raw(query_for_post_field('entry_author', posts))
    
    language_count = posts.raw(query_for_post_field('feed_language_id', posts))
    
    return {
      'posts': [int(x.count) for x in posts_count][0],
      'sources': [int(x.count) for x in source_count][0],
      'authors': [int(x.count) for x in author_count][0],
      'countries': [int(x.count) for x in location_count][0],
      'languages': [int(x.count) for x in language_count][0],
      'positive': sentiment['positive'] if sentiment.get('positive') else 0,
      'negative': sentiment['negative'] if sentiment.get('negative') else 0,
      'neutral': sentiment['neutral'] if sentiment.get('neutral') else 0,
      'reach': potential_reach
      }

def query_for_post_feedlink(field, posts):
    query = re.sub(
                r'\s+', ' ', f"""
                    SELECT 1 as id, COUNT(DISTINCT project_feedlinks.{field}) count
                    FROM project_post p
                    LEFT JOIN project_project_posts ON (p.id = project_project_posts.post_id)
                    LEFT JOIN project_feedlinks ON (p.feedlink_id = project_feedlinks.id)
                    WHERE {where_clause(posts)}
                """
            )

    return query

def query_for_post_field(field, posts):
    query = re.sub(
            r'\s+', ' ', f"""
                SELECT 1 as id, COUNT(DISTINCT p.{field}) count
                FROM project_post p
                LEFT JOIN project_project_posts ON (p.id = project_project_posts.post_id)
                WHERE {where_clause(posts)}
            """
        )
    
    return query

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_summary_widget(posts)
    fields = ['authors', 'countries', 'languages', 'negative', 'neutral', 'positive', 'posts', 'reach', 'sources']
    row = []
    for elem in fields:
        row.append(res[elem])
    return fields, [row]
