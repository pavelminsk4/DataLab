import {action} from '@store/constants'

const WIDGET_DEFAULT_SETTINGS = {
  height: '350px',
  isChartShow: false,
  hasPreview: true,
  hasAggregationPeriod: true,
  settingsTabs: ['General', 'Filters', 'Chart Layout'],
}

const CHARTS = {
  line: {
    componentName: 'LineChart',
    name: 'Line chart',
  },
  bar: {
    componentName: 'BarChart',
    name: 'Bar chart',
  },
  horizontalBarChart: {
    componentName: 'HorizontalBarChart',
    name: 'Column chart',
  },
  pie: {
    componentName: 'PieChart',
    name: 'Pie chart',
  },
  doughnut: {
    componentName: 'DoughnutChart',
    name: 'Doughnut chart',
  },
  radar: {
    componentName: 'RadarChart',
    name: 'Radar chart',
  },
  sentimentBar: {
    componentName: 'StackedBarChart',
    name: 'Bar chart',
  },
  sentimentHorizontalStackedBar: {
    componentName: 'SentimentHorizontalStackedBarChart',
    name: 'Column chart',
  },
  multiLine: {
    componentName: 'MultiLineChart',
    name: 'Line chart',
  },
  multiRadar: {
    componentName: 'MultiRadarChart',
    name: 'Radar chart',
  },
  wordCloud: {
    componentName: 'WordCloudChart',
    name: 'Word Cloud',
  },
  sentimentWordCloud: {
    componentName: 'ColoredWordCloudChart',
    name: 'Word Cloud',
  },
  topEntitiesBarChart: {
    componentName: 'TopEntitiesBarChart',
    name: 'Top Entities Bar Chart',
  },
}

const SIMPLE_CHARTS = [
  CHARTS.line,
  CHARTS.bar,
  CHARTS.pie,
  CHARTS.radar,
  CHARTS.doughnut,
  CHARTS.horizontalBarChart,
]
const SENTIMENTS_CHARTS = [CHARTS.horizontalBarChart, CHARTS.bar]

const MULTI_CHARTS = [CHARTS.multiLine, CHARTS.multiRadar]

export const widgetsConfig = {
  summary: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '360px',
    actionName: action.GET_SUMMARY_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General', 'Filters'],
  },

  volume: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_VOLUME_WIDGET,
    isChartShow: true,
    defaultChartType: 'LineChart',
    availableTypes: SIMPLE_CHARTS,
  },

  clipping_feed_content: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: {
      en: ['General'],
      ar: ['لمحة عامة'],
    },
  },
  top_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_AUTHORS_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'PieChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_sources: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_BRANDS_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'LineChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_countries: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_COUNTRIES_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'HorizontalBarChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_languages: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_LANGUAGES_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'PieChart',
    availableTypes: SIMPLE_CHARTS,
  },
  sentiment_top_sources: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_SENTIMENT_TOP_SOURCES,
    defaultChartType: 'HorizontalBarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_countries: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_SENTIMENT_TOP_COUNTRIES,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_SENTIMENT_TOP_AUTHORS,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_languages: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_SENTIMENT_TOP_LANGUAGES,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_for_period: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_FOR_PERIOD,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  content_volume_top_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_AUTHORS,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
  content_volume_top_countries: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_COUNTRIES,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
  content_volume_top_sources: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_SOURCES,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },

  top_keywords: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_TOP_KEYWORDS_WIDGET,
    defaultChartType: 'WordCloudChart',
    settingsTabs: ['General', 'Filters'],
  },

  top_keywords_by_country: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    hasAggregationPeriod: false,
    actionName: action.GET_TOP_KEYWORDS_WIDGET,
    defaultChartType: 'WordCloudChart',
    settingsTabs: ['General', 'Filters'],
  },

  keywords_by_location: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    hasAggregationPeriod: false,
    actionName: action.GET_TOP_KEYWORDS_WIDGET,
    defaultChartType: 'WordCloudChart',
    settingsTabs: ['General', 'Filters'],
  },

  sentiment_diagram: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_SENTIMENT_DIAGRAM,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },

  sentiment_number_of_results: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_NUMBER_OF_RESULT,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General', 'Filters'],
  },

  sentiment_top_keywords: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '420px',
    hasAggregationPeriod: false,
    actionName: action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET,
    defaultChartType: 'ColoredWordCloudChart',
    settingsTabs: ['General', 'Filters'],
  },

  authors_by_country: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    hasAggregationPeriod: false,
    actionName: action.GET_AUTHORS_BY_COUNTRY,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },

  volume_by_country: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_VOLUME_BY_COUNTRY,
    defaultChartType: 'WorldMapChart',
    settingsTabs: ['General', 'Filters'],
  },

  sources_by_language: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    hasAggregationPeriod: false,
    actionName: action.GET_SOURCES_BY_LANGUAGE,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
  },

  sources_by_country: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    hasAggregationPeriod: false,
    actionName: action.GET_SOURCES_BY_COUNTRY,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
  },

  overall_top_sources: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasPreview: false,
    hasAggregationPeriod: false,
    actionName: action.GET_OVERALL_TOP_SOURCES,
    defaultChartType: 'StackedBarChart',
    availableTypes: null,
    settingsTabs: ['General', 'Filters'],
  },

  languages_by_country: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_LANGUAGES_BY_COUNTRY,
    defaultChartType: 'TopEntitiesBarChart',
    availableTypes: null,
    settingsTabs: ['General', 'Filters'],
  },

  //social widgets
  content_volume: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_WIDGET,
    isChartShow: true,
    defaultChartType: 'LineChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_locations: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_LOCATIONS_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'HorizontalBarChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_sharing_sources: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_SHARING_SOURCES,
    hasAggregationPeriod: false,
    defaultChartType: null,
    availableTypes: null,
    settingsTabs: ['General', 'Filters'],
  },
  content_volume_top_locations: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_LOCATIONS,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
  content_volume_top_languages: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_LANGUAGES,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },

  overall_top_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasPreview: false,
    hasAggregationPeriod: false,
    actionName: action.GET_OVERALL_TOP_AUTHORS,
    defaultChartType: 'StackedBarChart',
    availableTypes: null,
    settingsTabs: ['General', 'Filters'],
  },
  top_authors_by_gender: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasPreview: false,
    actionName: action.GET_TOP_AUTHORS_BY_GENDER,
    defaultChartType: 'StackedBarChart',
    availableTypes: null,
    settingsTabs: ['General', 'Filters'],
  },
  authors_by_language: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    hasAggregationPeriod: false,
    actionName: action.GET_AUTHORS_BY_LANGUAGE,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },
  authors_by_location: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    actionName: action.GET_AUTHORS_BY_LOCATION,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
  },
  authors_by_sentiment: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    hasAggregationPeriod: false,
    actionName: action.GET_AUTHORS_BY_SENTIMENT,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },
  authors_by_gender: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '450px',
    actionName: action.GET_AUTHORS_BY_GENDER,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },
  languages_by_location: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_LANGUAGES_BY_LOCATION,
    defaultChartType: 'TopEntitiesBarChart',
    availableTypes: null,
    settingsTabs: ['General', 'Filters'],
  },

  // Sentiment
  sentiment_locations: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_LOCATIONS,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_AUTHORS,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_languages: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_LANGUAGES,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_FOR_PERIOD,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_by_gender: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_BY_GENDER,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  gender_volume: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_GENDER_VOLUME_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },

  gender_by_location: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_GENDER_BY_LOCATION,
    hasAggregationPeriod: false,
    defaultChartType: 'BarChart',
    availableTypes: [CHARTS.bar, CHARTS.horizontalBarChart],
  },

  // Account analysis
  profile_timeline: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_PROFILE_TIMELINE,
    hasAggregationPeriod: false,
    defaultChartType: 'BarLineChart',
    availableTypes: null,
    settingsTabs: ['General'],
  },

  most_engaging_post_types: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_MOST_ENGAGING_POST_TYPES,
    hasAggregationPeriod: false,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  most_engaging_media_types: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_MOST_ENGAGING_MEDIA_TYPES,
    hasAggregationPeriod: false,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  account_analysis_summary: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: '250px',
    actionName: action.GET_ACCOUNT_ANALYSIS_SUMMARY_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General'],
  },

  most_frequent_post_types: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_MOST_FREQUENT_POST_TYPES,
    hasAggregationPeriod: false,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  most_frequent_media_types: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_MOST_FREQUENT_MEDIA_TYPES,
    hasAggregationPeriod: false,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  optimal_post_length: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_OPTIMAL_POST_LENGTH,
    hasAggregationPeriod: false,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General'],
  },

  follower_growth: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_FOLLOWER_GROWTH,
    hasAggregationPeriod: false,
    defaultChartType: 'LineChart',
    availableTypes: null,
    settingsTabs: ['General'],
  },

  top_hashtags: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_HASHTAGS,
    hasAggregationPeriod: false,
    defaultChartType: 'HorizontalBarChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  optimal_number_of_hashtags: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_OPTIMAL_NUMBER_OF_HASHTAGS,
    hasAggregationPeriod: false,
    defaultChartType: 'HorizontalBarChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  average_engagements_by_day: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_OPTIMAL_NUMBER_OF_HASHTAGS,
    hasAggregationPeriod: false,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  optimal_post_time: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_OPTIMAL_POST_TIME,
    hasAggregationPeriod: false,
    defaultChartType: 'HeatmapChart',
    availableTypes: null,
    settingsTabs: ['General'],
  },

  top_posts_by_engagements: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_POSTS_BY_ENGAGEMENTS,
    hasPreview: false,
    hasAggregationPeriod: false,
    availableTypes: null,
    settingsTabs: ['General'],
  },

  best_times_to_post: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_BEST_TIMES_TO_POST,
    hasPreview: false,
    hasAggregationPeriod: false,
    availableTypes: null,
    settingsTabs: ['General'],
  },

  mention_timeline: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    defaultChartType: 'BarLineChart',
    availableTypes: null,
    settingsTabs: ['General'],
  },

  most_frequent_mention_media_types: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_MOST_FREQUENT_MENTION_MEDIA_TYPES,
    hasAggregationPeriod: false,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General'],
  },

  audience_mention_time: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_AUDIENCE_MENTION_TIME,
    hasAggregationPeriod: false,
    defaultChartType: 'HeatmapChart',
    availableTypes: null,
    settingsTabs: ['General'],
  },

  top_mentions_by_engagements: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_MENTIONS_BY_ENGAGEMENTS,
    hasPreview: false,
    hasAggregationPeriod: false,
    availableTypes: null,
    settingsTabs: ['General'],
  },

  average_engagements_by_day_for_mentions: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS,
    hasAggregationPeriod: false,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },

  mention_sentiment: {
    ...WIDGET_DEFAULT_SETTINGS,
    hasAggregationPeriod: false,
    actionName: action.GET_MENTION_SENTIMENT,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
    settingsTabs: ['General', 'Chart Layout'],
  },
}

export const summarySentimentConfig = [
  {
    name: 'Neutral posts',
    valueName: 'neutral',
    iconName: 'NeutralIcon',
    backgroundColor: '#516BEE',
  },
  {
    name: 'Negative posts',
    valueName: 'negative',
    iconName: 'NegativeIcon',
    backgroundColor: '#ED2549',
  },
  {
    name: 'Positive posts',
    valueName: 'positive',
    iconName: 'PositiveIcon',
    backgroundColor: '#57C7B3',
  },
]

export const summaryWidgetConfig = [
  {
    name: 'New posts',
    valueName: 'posts',
    iconName: 'NewPostIcon',
    backgroundColor: '#2EA8DD',
  },
  ...summarySentimentConfig,
  {
    name: 'Sources',
    valueName: 'sources',
    iconName: 'SourceIcon',
    backgroundColor: '#7546FF',
  },
  {
    name: 'Potential reach',
    valueName: 'reach',
    iconName: 'PotentialReachIcon',
    backgroundColor: '#FC732D',
  },
  {
    name: 'Countries',
    valueName: 'countries',
    iconName: 'CountryIcon',
    backgroundColor: '#A0B8BE',
  },
  {
    name: 'Authors',
    valueName: 'authors',
    iconName: 'AuthorIcon',
    backgroundColor: '#EA6E8F',
  },
]

export const socialSummaryWidgetConfig = [
  ...summaryWidgetConfig,
  {
    name: 'Likes',
    valueName: 'likes',
    iconName: 'LikeIcon',
    backgroundColor: '#ED2549',
  },
  {
    name: 'Reply',
    valueName: 'replies',
    iconName: 'RepliesIcon',
    backgroundColor: '#A0B8BE',
  },
  {
    name: 'Retweet',
    valueName: 'retweets',
    iconName: 'RetweetIcon',
    backgroundColor: '#57C7B3',
  },
]

export const sentimentOverallWidgetConfig = [
  {
    name: 'Positive posts',
    valueName: 'positive',
    iconName: 'PositiveIcon',
    backgroundColor: '#57C7B3',
    className: 'positive',
  },
  {
    name: 'Neutral posts',
    valueName: 'neutral',
    iconName: 'NeutralIcon',
    backgroundColor: '#516BEE',
    className: 'neutral',
  },
  {
    name: 'Negative posts',
    valueName: 'negative',
    iconName: 'NegativeIcon',
    backgroundColor: '#ED2549',
    className: 'negative',
  },
]
