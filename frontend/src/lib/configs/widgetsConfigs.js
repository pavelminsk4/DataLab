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
}

const SIMPLE_CHARTS = [CHARTS.line, CHARTS.bar, CHARTS.pie, CHARTS.radar]
const SENTIMENTS_CHARTS = [CHARTS.horizontalBarChart, CHARTS.bar]

const MULTI_CHARTS = [CHARTS.multiLine, CHARTS.multiRadar]

export const modalWidgetsConfig = {
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
    defaultChartType: 'SentimentBarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_10_countries_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_COUNTRIES,
    defaultChartType: 'SentimentBarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_10_authors_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_AUTHORS,
    defaultChartType: 'SentimentBarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_top_10_languages_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_LANGUAGES,
    defaultChartType: 'SentimentBarChart',
    availableTypes: SENTIMENTS_CHARTS,
  },
  sentiment_for_period_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_FOR_PERIOD,
    defaultChartType: 'SentimentBarChart',
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

  //social widgets
  content_volume_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_VOLUME_WIDGET,
    isChartShow: true,
    defaultChartType: 'LineChart',
    availableTypes: SIMPLE_CHARTS,
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
