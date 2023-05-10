from reports.models import ReportItem


class Converter:
    def __init__(self, project):
        self.project = project

    def convert_to_item(self):
        project_type = self.project.__class__.__name__

        if project_type == 'Project':
            widget_list = self.project.widgets_list_2
            item = ReportItem.objects.create(
                module_type = project_type,
                module_project_id = self.project.id,

                onl_summary = widget_list.summary_widget.is_active,
                onl_volume = widget_list.volume_widget.is_active,
                onl_clipping_feed_content = widget_list.clipping_feed_content_widget.is_active,
                onl_top_authors_by_volume = widget_list.top_10_authors_by_volume_widget.is_active,
                onl_top_brands = widget_list.top_10_brands_widget.is_active,
                onl_top_countries = widget_list.top_10_countries_widget.is_active,
                onl_top_languages = widget_list.top_10_languages_widget.is_active,
                onl_content_volume_top_source = widget_list.content_volume_top_5_source_widget.is_active,
                onl_sentiment_top_sources = widget_list.sentiment_top_10_sources_widget.is_active,
                onl_sentiment_top_countries = widget_list.sentiment_top_10_countries_widget.is_active,
                onl_sentiment_top_authors = widget_list.sentiment_top_10_authors_widget.is_active,
                onl_sentiment_top_languages = widget_list.sentiment_top_10_languages_widget.is_active,
                onl_sentiment_for_period = widget_list.sentiment_for_period_widget.is_active,
                onl_content_volume_top_authors = widget_list.content_volume_top_5_authors_widget.is_active,
                onl_content_volume_top_countries = widget_list.content_volume_top_5_countries_widget.is_active,
                onl_top_keywords = widget_list.top_keywords.is_active,
                onl_sentiment_top_keywords = widget_list.sentiment_top_keywords.is_active,
                onl_sentiment_number_of_results = widget_list.sentiment_number_of_results.is_active,
                onl_sentiment_diagram = widget_list.sentiment_diagram.is_active,
                onl_authors_by_country = widget_list.authors_by_country.is_active,
                onl_top_sharing_sources = widget_list.top_sharing_sources.is_active,
                onl_overall_top_sources = widget_list.overall_top_sources.is_active,
                onl_sources_by_country = widget_list.sources_by_country.is_active,
                onl_sources_by_language = widget_list.sources_by_language.is_active,
                onl_authors_by_language = widget_list.authors_by_language.is_active,
                onl_authors_by_sentiment = widget_list.authors_by_sentiment.is_active,
                onl_overall_top_authors = widget_list.overall_top_authors.is_active,
            )

        elif project_type == 'ProjectSocial':
            widget_list = self.project.social_widgets_list
            item = ReportItem.objects.create(
                module_type = project_type,
                module_project_id = self.project.id,

                soc_summary = widget_list.summary.is_active,
                soc_clipping_feed_content = widget_list.clipping_feed_content.is_active,
                soc_top_locations = widget_list.top_locations.is_active,
                soc_top_authors = widget_list.top_authors.is_active,
                soc_top_languages = widget_list.top_languages.is_active,
                soc_content_volume = widget_list.content_volume.is_active,
                soc_content_volume_top_locations = widget_list.content_volume_top_locations.is_active,
                soc_content_volume_top_authors = widget_list.content_volume_top_authors.is_active,
                soc_content_volume_top_languages = widget_list.content_volume_top_languages.is_active,
                soc_sentiment = widget_list.sentiment.is_active,
                soc_gender_volume = widget_list.gender_volume.is_active,
                soc_sentiment_number_of_results = widget_list.sentiment_number_of_results.is_active,
                soc_sentiment_authors = widget_list.sentiment_authors.is_active,
                soc_sentiment_locations = widget_list.sentiment_locations.is_active,
                soc_sentiment_languages = widget_list.sentiment_languages.is_active,
                soc_sentiment_by_gender = widget_list.sentiment_by_gender.is_active,
                soc_top_keywords = widget_list.top_keywords.is_active,
                soc_sentiment_top_keywords = widget_list.sentiment_top_keywords.is_active,
                soc_sentiment_diagram = widget_list.sentiment_diagram.is_active,
                soc_top_sharing_sources = widget_list.top_sharing_sources.is_active,
                soc_overall_top_authors = widget_list.overall_top_authors.is_active,
                soc_top_authors_by_gender = widget_list.top_authors_by_gender.is_active,
                soc_authors_by_language = widget_list.authors_by_language.is_active,
                soc_authors_by_location = widget_list.authors_by_location.is_active,
                soc_authors_by_sentiment = widget_list.authors_by_sentiment.is_active,
                soc_authors_by_gender = widget_list.authors_by_gender.is_active,
            )
        return item
