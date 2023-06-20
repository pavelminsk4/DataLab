from . import content_volume_top_5_countries_widget_image, content_volume_top_5_authors_widget_image, content_volume_top_5_source_widget_image, summary_widget_image, top_10_authors_widget_image, volume_widget_image, top_10_sources_widget_image, top_10_countries_widget_image, top_10_languages_widget_image, sentiment_top_10_sources_widget_image, sentiment_top_10_authors_image, sentiment_top_10_countries_image, sentiment_top_10_languages_image, sentiment_for_period_widget_image
from project.models import Project

def prepare_widget_images(project_id):
    project = Project.objects.get(id=project_id)
    widget_pk = project.widgets_list_2.summary_id
    summary_widget_image.create_summary_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_authors_id
    top_10_authors_widget_image.create_top_10_authors_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.volume_id
    volume_widget_image.create_vol_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_brands_id
    top_10_sources_widget_image.create_top_10_sources_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_countries_id
    top_10_countries_widget_image.create_top_10_countries_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.top_languages_id
    top_10_languages_widget_image.create_top_10_languages_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_sources_id
    sentiment_top_10_sources_widget_image.create_sentiment_top_10_sources_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_authors_id
    sentiment_top_10_authors_image.create_sentiment_top_10_authors_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_countries_id
    sentiment_top_10_countries_image.create_sentiment_top_10_countries_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_top_languages_id
    sentiment_top_10_languages_image.create_sentiment_top_10_languages_wid_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.sentiment_for_period_id
    sentiment_for_period_widget_image.create_sentiment_for_period_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.content_volume_top_sources_id
    content_volume_top_5_source_widget_image.create_content_volume_top_5_source_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.content_volume_top_authors_id
    content_volume_top_5_authors_widget_image.create_content_volume_top_5_authors_widget_image(project_id, widget_pk)
    widget_pk = project.widgets_list_2.content_volume_top_countries_id
    content_volume_top_5_countries_widget_image.create_content_volume_top_5_countries_widget_image(project_id, widget_pk)

def prepare_widget_images_for_regular(item):
    project = Project.objects.get(id = item.module_project_id)
    if item.onl_summary:
        widget_pk = project.widgets_list_2.summary_id
        summary_widget_image.create_summary_widget_image(project.id, widget_pk)
    if item.onl_volume:
        widget_pk = project.widgets_list_2.volume_id
        volume_widget_image.create_vol_widget_image(project.id, widget_pk)
    if item.onl_top_authors:
        widget_pk = project.widgets_list_2.top_authors_id
        top_10_authors_widget_image.create_top_10_authors_wid_image(project.id, widget_pk)
    if item.onl_top_brands:
        widget_pk = project.widgets_list_2.top_brands_id
        top_10_sources_widget_image.create_top_10_sources_wid_image(project.id, widget_pk)
    if item.onl_top_countries:
        widget_pk = project.widgets_list_2.top_countries_id
        top_10_countries_widget_image.create_top_10_countries_wid_image(project.id, widget_pk)
    if item.onl_top_languages:
        widget_pk = project.widgets_list_2.top_languages_id
        top_10_languages_widget_image.create_top_10_languages_wid_image(project.id, widget_pk)
