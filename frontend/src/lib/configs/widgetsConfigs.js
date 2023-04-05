import {action} from '@store/constants'

const WIDGET_DEFAULT_SETTINGS = {
  height: 13,
  isChartShow: false,
  hasAggregationPeriod: true,
  settingsTabs: ['General', 'Dimensions', 'Chart Layout'],
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
    componentName: 'SentimentBarChart',
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
    componentName: 'SentimentWordCloudChart',
    name: 'Word Cloud',
  },
  sentimentBarChart: {
    componentName: 'SentimentBarChartChart',
    name: 'Sentiment Bar Chart',
  },
}

const SIMPLE_CHARTS = [
  CHARTS.line,
  CHARTS.bar,
  CHARTS.pie,
  CHARTS.radar,
  CHARTS.doughnut,
]
const SENTIMENTS_CHARTS = [CHARTS.horizontalBarChart, CHARTS.bar]

const MULTI_CHARTS = [CHARTS.multiLine, CHARTS.multiRadar]

export const widgetsConfig = {
  summary_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SUMMARY_WIDGET,
    height: 7,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General', 'Dimensions'],
  },
  volume_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_VOLUME_WIDGET,
    isChartShow: true,
    defaultChartType: 'LineChart',
    availableTypes: SIMPLE_CHARTS,
  },
  clipping_feed_content_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General'],
  },
  top_10_authors_by_volume_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_AUTHORS_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'PieChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_10_brands_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_BRANDS_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'LineChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_10_countries_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_COUNTRIES_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'HorizontalBarChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_10_languages_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_LANGUAGES_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'PieChart',
    availableTypes: SIMPLE_CHARTS,
  },
  sentiment_top_10_sources_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_SOURCES,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_10_countries_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_COUNTRIES,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_10_authors_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_AUTHORS,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_10_languages_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_LANGUAGES,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_for_period_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_FOR_PERIOD,
    defaultChartType: 'BarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  content_volume_top_5_authors_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_AUTHORS,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
  content_volume_top_5_countries_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_COUNTRIES,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
  content_volume_top_5_source_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_SOURCES,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },

  top_keywords: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: 15,
    actionName: action.GET_TOP_KEYWORDS_WIDGET,
    defaultChartType: 'WordCloudChart',
  },

  sentiment_diagram: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_DIAGRAM,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },

  sentiment_number_of_results: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_NUMBER_OF_RESULT,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General', 'Dimensions'],
  },

  sentiment_top_keywords: {
    ...WIDGET_DEFAULT_SETTINGS,
    height: 15,
    actionName: action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET,
    defaultChartType: 'SentimentWordCloudChart',
  },

  //social widgets
  summary: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SUMMARY_WIDGET,
    height: 7,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General', 'Dimensions'],
  },
  clipping_feed_content: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: null,
    settingsTabs: ['General'],
  },
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
  top_languages: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_LANGUAGES_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'PieChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_AUTHORS_WIDGET,
    hasAggregationPeriod: false,
    defaultChartType: 'PieChart',
    availableTypes: SIMPLE_CHARTS,
  },
  top_sharing_sources: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TO_SHARING_SOURCES,
    height: 8,
    hasAggregationPeriod: false,
    defaultChartType: null,
    availableTypes: null,
  },
  content_volume_by_top_locations: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_LOCATIONS,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
  content_volume_by_top_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_AUTHORS,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
  content_volume_by_top_languages: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_LANGUAGES,
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },

  overall_top_authors: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_OVERALL_TOP_AUTHORS,
    defaultChartType: 'SentimentBarChart',
    availableTypes: null,
  },
  top_authors_by_gender: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_AUTHORS_BY_GENDER,
    defaultChartType: 'SentimentBarChart',
    availableTypes: null,
  },
  authors_by_language: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_AUTHORS_BY_LANGUAGE,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },
  authors_by_location: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_AUTHORS_BY_LOCATION,
    defaultChartType: 'BarChart',
    availableTypes: SIMPLE_CHARTS,
  },
  authors_by_sentiment: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_AUTHORS_BY_SENTIMENT,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
  },
  authors_by_gender: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_AUTHORS_BY_GENDER,
    defaultChartType: 'DoughnutChart',
    availableTypes: SIMPLE_CHARTS,
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
    defaultChartType: 'MultiLineChart',
    availableTypes: MULTI_CHARTS,
  },
}

export const summaryWidgetConfig = [
  {
    name: 'New posts',
    valueName: 'posts',
    iconName: 'NewPostIcon',
    backgroundColor: '#2EA8DD',
  },
  {
    name: 'Neutral posts',
    valueName: 'neut',
    iconName: 'NeutralIcon',
    backgroundColor: '#516BEE',
  },
  {
    name: 'Negative posts',
    valueName: 'neg',
    iconName: 'NegativeIcon',
    backgroundColor: '#ED2549',
  },
  {
    name: 'Positive posts',
    valueName: 'pos',
    iconName: 'PositiveIcon',
    backgroundColor: '#57C7B3',
  },
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
    iconName: 'AuthorsIcon',
    backgroundColor: '#EA6E8F',
  },
]

export const sentimentOverallWidgetConfig = [
  {
    name: 'Positive posts',
    valueName: 'positive',
    iconName: 'PositiveIcon',
    backgroundColor: '#57C7B3',
    className: 'pos',
  },
  {
    name: 'Neutral posts',
    valueName: 'neutral',
    iconName: 'NeutralIcon',
    backgroundColor: '#516BEE',
    className: 'neut',
  },
  {
    name: 'Negative posts',
    valueName: 'negative',
    iconName: 'NegativeIcon',
    backgroundColor: '#ED2549',
    className: 'neg',
  },
]
