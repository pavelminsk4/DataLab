import {action} from '@store/constants'

export default {
  summary_widget: {
    height: 8,
    actionName: action.GET_SUMMARY_WIDGET,
    isChartShow: false,
  },
  volume_widget: {
    height: 12,
    actionName: action.GET_VOLUME_WIDGET,
    isChartShow: true,
  },
  clipping_feed_content_widget: {
    height: 13,
    actionName: action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    isChartShow: false,
  },
  top_10_authors_by_volume_widget: {
    height: 13,
    actionName: action.GET_TOP_AUTHORS_WIDGET,
    isChartShow: false,
  },
  top_10_brands_widget: {
    height: 13,
    actionName: action.GET_TOP_BRANDS_WIDGET,
    isChartShow: false,
  },
  top_10_countries_widget: {
    height: 13,
    actionName: action.GET_TOP_COUNTRIES_WIDGET,
    isChartShow: false,
  },
  top_10_languages_widget: {
    height: 13,
    actionName: action.GET_TOP_LANGUAGES_WIDGET,
    isChartShow: false,
  },
  sentiment_top_10_sources_widget: {
    height: 12,
    actionName: action.GET_SENTIMENT_TOP_SOURCES,
    isChartShow: false,
  },
  sentiment_top_10_countries_widget: {
    height: 12,
    actionName: action.GET_SENTIMENT_TOP_COUNTRIES,
    isChartShow: false,
  },
  sentiment_top_10_authors_widget: {
    height: 12,
    actionName: action.GET_SENTIMENT_TOP_AUTHORS,
    isChartShow: false,
  },
  sentiment_top_10_languages_widget: {
    height: 12,
    actionName: action.GET_SENTIMENT_TOP_LANGUAGES,
    isChartShow: false,
  },
  sentiment_for_period_widget: {
    height: 12,
    actionName: action.GET_SENTIMENT_FOR_PERIOD,
    isChartShow: false,
  },
  content_volume_top_5_authors_widget: {
    height: 12,
    actionName: action.GET_CONTENT_VOLUME_TOP_AUTHORS,
    isChartShow: false,
  },
  content_volume_top_5_countries_widget: {
    height: 12,
    actionName: action.GET_CONTENT_VOLUME_TOP_COUNTRIES,
    isChartShow: false,
  },
  content_volume_top_5_source_widget: {
    height: 12,
    actionName: action.GET_CONTENT_VOLUME_TOP_SOURCES,
    isChartShow: false,
  },
}
