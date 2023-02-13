import {action} from '@store/constants'

const WIDGET_DEFAULT_SETTINGS = {
  height: 12,
  isChartShow: false,
  hasAggregationPeriod: true,
}

export default {
  summary_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SUMMARY_WIDGET,
    height: 7,
    hasAggregationPeriod: false,
  },
  volume_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_VOLUME_WIDGET,
    isChartShow: true,
  },
  clipping_feed_content_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    height: 13,
    hasAggregationPeriod: false,
  },
  top_10_authors_by_volume_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_AUTHORS_WIDGET,
    height: 13,
    hasAggregationPeriod: false,
  },
  top_10_brands_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_BRANDS_WIDGET,
    height: 13,
    hasAggregationPeriod: false,
  },
  top_10_countries_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_COUNTRIES_WIDGET,
    height: 13,
    hasAggregationPeriod: false,
  },
  top_10_languages_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_TOP_LANGUAGES_WIDGET,
    height: 13,
    hasAggregationPeriod: false,
  },
  sentiment_top_10_sources_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_SOURCES,
  },
  sentiment_top_10_countries_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_COUNTRIES,
  },
  sentiment_top_10_authors_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_AUTHORS,
  },
  sentiment_top_10_languages_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_TOP_LANGUAGES,
  },
  sentiment_for_period_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_SENTIMENT_FOR_PERIOD,
  },
  content_volume_top_5_authors_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_AUTHORS,
  },
  content_volume_top_5_countries_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_COUNTRIES,
  },
  content_volume_top_5_source_widget: {
    ...WIDGET_DEFAULT_SETTINGS,
    actionName: action.GET_CONTENT_VOLUME_TOP_SOURCES,
  },
}
