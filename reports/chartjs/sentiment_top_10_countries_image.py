
from .services.algorithm_for_count_sentiment_top_10_widgets import algorithm_for_count_sentiment_top_10_widgets
from widgets.common_widget.project_posts_filter import project_posts_filter
from django.db.models import Count


def create_sentiment_top_10_countries_wid_image(project_id, widget_pk):
    posts, widget = project_posts_filter(project_id, widget_pk)
    top_countries = posts.values('feedlink__country').annotate(brand_count=Count('feedlink__country')).order_by('-brand_count').values_list('feedlink__country', flat=True)[:10]
    results = {country: list(posts.filter(feedlink__country=country).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for country in top_countries}
    qc = algorithm_for_count_sentiment_top_10_widgets(results, top_countries)
    qc.to_file('tmp/sentiment_top_10_countries_widget.png')
