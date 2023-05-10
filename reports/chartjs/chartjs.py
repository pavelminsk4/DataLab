from . import content_volume_top_5_countries_widget_image, content_volume_top_5_authors_widget_image, content_volume_top_5_source_widget_image, summary_widget_image, top_10_authors_widget_image, volume_widget_image, top_10_sources_widget_image, top_10_countries_widget_image, top_10_languages_widget_image, sentiment_top_10_sources_widget_image, sentiment_top_10_authors_image, sentiment_top_10_countries_image, sentiment_top_10_languages_image, sentiment_for_period_widget_image
from project.models import Project

def prepare_widget_images(project_id):
    project = Project.objects.get(id=project_id)
    widget_pk = project.widgets_list_2.summary_widget_id
    summary_widget_image.create_summary_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_10_authors_by_volume_widget_id
    top_10_authors_widget_image.create_top_10_authors_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.volume_widget_id
    volume_widget_image.create_vol_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_10_brands_widget_id
    top_10_sources_widget_image.create_top_10_sources_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_10_countries_widget_id
    top_10_countries_widget_image.create_top_10_countries_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_10_languages_widget_id
    top_10_languages_widget_image.create_top_10_languages_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_10_sources_widget_id
    sentiment_top_10_sources_widget_image.create_sentiment_top_10_sources_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_10_authors_widget_id
    sentiment_top_10_authors_image.create_sentiment_top_10_authors_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_10_countries_widget_id
    sentiment_top_10_countries_image.create_sentiment_top_10_countries_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_10_languages_widget_id
    sentiment_top_10_languages_image.create_sentiment_top_10_languages_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_for_period_widget_id
    sentiment_for_period_widget_image.create_sentiment_for_period_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.content_volume_top_5_source_widget_id
    content_volume_top_5_source_widget_image.create_content_volume_top_5_source_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.content_volume_top_5_authors_widget_id
    content_volume_top_5_authors_widget_image.create_content_volume_top_5_authors_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.content_volume_top_5_countries_widget_id
    content_volume_top_5_countries_widget_image.create_content_volume_top_5_countries_widget_image(project_id, widget_pk)

def prepare_widget_images_for_regular(item):
    project = Project.objects.get(id = item.module_project_id)
    if item.onl_summary:
        widget_pk = project.widgets_list_2.summary_widget_id
        summary_widget_image.create_summary_widget_image(project.id, widget_pk)
    if item.onl_volume:
        widget_pk = project.widgets_list_2.volume_widget_id
        volume_widget_image.create_vol_widget_image(project.id, widget_pk)
    if item.onl_top_authors_volume:
        widget_pk = project.widgets_list_2.top_10_authors_by_volume_widget_id
        top_10_authors_widget_image.create_top_10_authors_wid_image(project.id, widget_pk)
    if item.onl_top_brands:
        widget_pk = project.widgets_list_2.top_10_brands_widget_id
        top_10_sources_widget_image.create_top_10_sources_wid_image(project.id, widget_pk)
    if item.onl_top_countries:
        widget_pk = project.widgets_list_2.top_10_countries_widget_id
        top_10_countries_widget_image.create_top_10_countries_wid_image(project.id, widget_pk)
    if item.onl_top_languages:
        widget_pk = project.widgets_list_2.top_10_languages_widget_id
        top_10_languages_widget_image.create_top_10_languages_wid_image(project.id, widget_pk)
