import widgets.common_widget.content_volume_top_countries as volume_countries
import widgets.common_widget.sentiment_top_languages as sentiment_languages
import widgets.common_widget.sentiment_top_countries as sentiment_country
import widgets.common_widget.content_volume_top_sources as volume_sources
import widgets.common_widget.content_volume_top_authors as volume_authors
import widgets.sentiment.sentiment_number_of_results as sentiment_number
import widgets.common_widget.sentiment_top_sources as sentiment_sources
import widgets.common_widget.sentiment_top_authors as sentiment_authors
import widgets.demography.top_keywords_by_country as keywords_countries
import widgets.sentiment.sentiment_top_keywords as sentiment_keywords
import widgets.influencers.authors_by_sentiment as authors_sentiment
import widgets.demography.languages_by_country as languages_country
import widgets.influencers.authors_by_language as authors_language
import widgets.demography.sources_by_language as sources_language
import widgets.influencers.authors_by_country as authors_country
import widgets.demography.sources_by_country as sources_country
import widgets.common_widget.sentiment_for_period as sentiment
import widgets.common_widget.top_countries as countries
import widgets.common_widget.top_languages as languages
import widgets.common_widget.volume_widget as volume
import widgets.common_widget.top_authors as authors
import widgets.common_widget.top_sources as sources
import widgets.summary.top_keywords as keywords
import widgets.common_widget.summary as summary

import project_social.widgets.dashboard.content_volume_top_locations as soc_volume_location
import project_social.widgets.dashboard.content_volume_top_languages as soc_volume_language
import project_social.widgets.sentiment.sentiment_number_of_results as soc_sentiment_number
import project_social.widgets.sentiment.sentiment_top_keywords as soc_sentiment_keywords
import project_social.widgets.demography.languages_by_location as soc_languages_location
import project_social.widgets.dashboard.content_volume_top_authors as soc_volume_author
import project_social.widgets.dashboard.sentiment_languages as soc_sentiment_languages
import project_social.widgets.dashboard.sentiment_locations as soc_sentiment_locations
import project_social.widgets.influencers.authors_by_sentiment as soc_author_sentiment
import project_social.widgets.demography.keywords_by_location as soc_keywords_location
import project_social.widgets.sentiment.sentiment_by_gender as soc_sentiment_gender
import project_social.widgets.demography.authors_by_language as soc_author_language
import project_social.widgets.demography.authors_by_location as soc_author_location
import project_social.widgets.dashboard.sentiment_authors as soc_sentiment_authors
import project_social.widgets.demography.gender_by_location as soc_gender_location
import project_social.widgets.demography.authors_by_gender as soc_author_gender
import project_social.widgets.dashboard.top_locations as soc_top_locations
import project_social.widgets.dashboard.top_languages as soc_top_languages
import project_social.widgets.summary.gender_volume as soc_gender_volume
import project_social.widgets.summary.top_keywords as soc_top_keywords
import project_social.widgets.dashboard.top_authors as soc_top_authors
import project_social.widgets.dashboard.summary_widget as soc_summary
import project_social.widgets.dashboard.content_volume as soc_volume
import project_social.widgets.dashboard.sentiment as soc_sentiment

import account_analysis.widgets.optimization.mentions.average_engagements_by_day_for_mentions as average_engagements_by_day_for_mentions
import account_analysis.widgets.dashboard.mentions.most_frequent_mention_media_types as most_frequent_mention_media_types
import account_analysis.widgets.optimization.optimal_number_of_hashtags as optimal_number_of_hashtags
import account_analysis.widgets.optimization.average_engagements_by_day as average_engagements_by_day
import account_analysis.widgets.optimization.mentions.audience_mention_time as audience_mention_time
import account_analysis.widgets.dashboard.most_frequent_media_types as most_frequent_media_types
import account_analysis.widgets.dashboard.most_engaging_media_types as most_engaging_media_types
import account_analysis.widgets.dashboard.most_frequent_post_types as most_frequent_post_types
import account_analysis.widgets.dashboard.most_engaging_post_types as most_engaging_post_types
import account_analysis.widgets.dashboard.mentions.mention_sentiment as mention_sentiment
import account_analysis.widgets.dashboard.mentions.mention_timeline as mention_timeline
import account_analysis.widgets.optimization.optimal_post_length as optimal_post_length
import account_analysis.widgets.optimization.best_times_to_post as best_times_to_post
import account_analysis.widgets.optimization.optimal_post_time as optimal_post_time
import account_analysis.widgets.dashboard.profile_timeline as profile_timeline
import account_analysis.widgets.dashboard.follower_growth as follower_growth
import account_analysis.widgets.optimization.top_hashtags as top_hashtags



widgets = {
    'Summary': summary,
    'Content volume': volume,
    'Top authors': authors,
    'Top sources': sources,
    'Top countries': countries,
    'Top languages': languages,
    'Sentiment for period': sentiment,
    'Content Volume by top sources': volume_sources,
    'Sentiment top sources': sentiment_sources,
    'Sentiment top countries': sentiment_country,
    'Sentiment top authors': sentiment_authors,
    'Sentiment top languages': sentiment_languages,
    'Content volume by top authors': volume_authors,
    'Content volume by top countries': volume_countries,
    'Top keywords': keywords,
    'Sentiment top keywords': sentiment_keywords,
    'Sentiment number of results': sentiment_number,
    'Sentiment diagram': sentiment_number,
    'Authors by country': authors_country,
    'Sources by country': sources_country,
    'Sources by language': sources_language,
    'Authors by language': authors_language,
    'Authors by sentiment': authors_sentiment,
    'Top keywords by country': keywords_countries,
    'Top languages by country': languages_country,
}
social_widgets = {
    'Summary': soc_summary,
    'Top locations': soc_top_locations,
    'Top authors': soc_top_authors,
    'Top languages': soc_top_languages,
    'Content volume': soc_volume,
    'Content volume by top locations': soc_volume_location,
    'Content volume by top authors': soc_volume_author,
    'Content volume by top languages': soc_volume_language,
    'Sentiment': soc_sentiment,
    'Gender volume': soc_gender_volume,
    'Sentiment number of results': soc_sentiment_number,
    'Sentiment authors': soc_sentiment_authors,
    'Sentiment locations': soc_sentiment_locations,
    'Sentiment languages': soc_sentiment_languages,
    'Sentiment by gender': soc_sentiment_gender,
    'Top keywords': soc_top_keywords,
    'Sentiment top keywords': soc_sentiment_keywords,
    'Sentiment diagram': soc_sentiment_number,
    'Authors by language': soc_author_language,
    'Authors by location': soc_author_location,
    'Authors by sentiment': soc_author_sentiment,
    'Authors by gender': soc_author_gender,
    'Top keywords by location': soc_keywords_location,
    'Top languages by location': soc_languages_location,
    'Top gender by location': soc_gender_location,
}

account_analysis_widgets = {
    'Profile timeline': profile_timeline,
    'Follower growth': follower_growth,
    'Most frequent post types': most_frequent_post_types,
    'Most frequent media types': most_frequent_media_types,
    'Most engaging post types': most_engaging_post_types,
    'Most engaging media types': most_engaging_media_types,
    'Mention timeline': mention_timeline,
    'Mention sentiment': mention_sentiment,
    'Most frequent mention media types': most_frequent_mention_media_types,
    'Best times to post': best_times_to_post,
    'Optimal post length': optimal_post_length,
    'Optimal post time': optimal_post_time,
    'Top hashtags': top_hashtags,
    'Optimal number of hashtags': optimal_number_of_hashtags,
    'Average engagements by day': average_engagements_by_day,
    'Average engagements by day (mentions)': average_engagements_by_day_for_mentions,
    'Audience mention time': audience_mention_time,
}
