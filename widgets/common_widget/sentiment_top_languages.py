from widgets.common_widget.project_posts_filter import project_posts_filter
from common.utils.where_clause import where_clause, ids
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count
from project.models import Speech
import re


def sentiment_top_languages(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = calculate_sentiment_top_languages(posts, widget.top_counts)
    return JsonResponse(res, safe = False)

def sentiment_top_languages_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_sentiment_top_languages(posts, widget.top_counts),
        'widget': {'sentiment_top_languages': model_to_dict(widget)},
        'module_name': 'Online'
    }

def calculate_sentiment_top_languages(posts, top_counts):
    top_languages = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
                SELECT l.id id, l.language language, COUNT(p.feed_language_id) post_count
                FROM project_post p
                JOIN project_project_posts ON p.id = project_project_posts.post_id
                JOIN project_speech l ON p.feed_language_id = l.id
                WHERE {where_clause(posts)}
                GROUP BY l.id
                ORDER BY post_count DESC
                LIMIT {top_counts}
            """
        )
    )
    
    top_languages = tuple(language.id for language in top_languages)
    
    sentiment_query = posts.raw(
        re.sub(
            r'\s+', ' ', f"""
                SELECT p.feed_language_id id, p.sentiment, COUNT(p.sentiment) sentiment_count, COUNT(p.feedlink_id) post_count
                FROM project_post p
                JOIN project_project_posts ON p.id = project_project_posts.post_id
                WHERE p.feed_language_id IN {ids(top_languages)} AND {where_clause(posts)}
                GROUP BY p.feed_language_id, p.sentiment
                ORDER BY sentiment_count DESC
            """
        )
    )
    
    results = {Speech.objects.get(id=language).language: [
        {'sentiment': 'neutral', 'sentiment_count': 0},
        {'sentiment': 'negative', 'sentiment_count': 0},
        {'sentiment': 'positive', 'sentiment_count': 0}
    ] for language in top_languages}

    for line in sentiment_query:
        for language in top_languages:
             if line.id == language:
                if line.sentiment == 'neutral':
                    results[Speech.objects.get(id=language).language][0]['sentiment_count'] = line.post_count
                elif line.sentiment == 'negative':
                    results[Speech.objects.get(id=language).language][1]['sentiment_count'] = line.post_count
                elif line.sentiment == 'positive':
                    results[Speech.objects.get(id=language).language][2]['sentiment_count'] = line.post_count
    
    return results      
