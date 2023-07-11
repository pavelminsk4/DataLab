import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },
  [get.LOADING_WIDGETS](state) {
    return state.loadingWidgets
  },

  [get.PROJECTS](state) {
    return state.projects
  },

  [get.WORKSPACES](state) {
    return state.workspaces
  },

  [get.USER_INFO](state) {
    return state.userInfo
  },

  [get.DEPARTMENT](state) {
    return state.userInfo?.user_profile.department
  },

  [get.CURRENT_STEP](state) {
    return state.currentStep
  },

  [get.KEYWORDS](state) {
    return state.keywords
  },

  [get.NEW_PROJECT](state) {
    return state.newProject
  },

  [get.NEW_WORKSPACE](state) {
    return state.newWorkspace
  },

  [get.SEARCH_DATA](state) {
    return state.searchData
  },

  [get.COUNTRIES](state) {
    return state.countries
      .map((country) => country.name)
      .filter((country) => country.trim())
  },

  [get.LANGUAGES](state) {
    return state.languages
      .map((language) => language.language)
      .filter((language) => language.trim())
  },

  [get.SOURCES](state) {
    return state.sources
      .map((source) => source.source1)
      .filter((source) => source.trim())
  },

  [get.AUTHORS](state) {
    return state.authors
      .map((author) => author.entry_author)
      .filter((author) => author.trim())
  },
  [get.SEARCH_LISTS](state, getters) {
    return {
      authors: getters[get.AUTHORS],
      countries: getters[get.COUNTRIES],
      languages: getters[get.LANGUAGES],
      sources: getters[get.SOURCES],
    }
  },

  [get.ADDITIONAL_FILTERS](state) {
    return state.additionalFilters
  },

  [get.SUMMARY_WIDGET](state) {
    return state.summary
  },

  [get.VOLUME_WIDGET](state) {
    return state.volume
  },

  [get.AUTHORS_BY_SENTIMENT](state) {
    return state.authorsBySentiment
  },

  [get.AUTHORS_BY_LANGUAGE](state) {
    return state.authorsByLanguage
  },

  [get.OVERALL_TOP_AUTHORS](state) {
    return state.overallTopAuthors
  },

  [get.CLIPPING_FEED_CONTENT_WIDGET](state) {
    return state.clippingFeedContent
  },

  [get.AVAILABLE_WIDGETS](state) {
    return state.availableWidgets
  },

  [get.CLIPPING_WIDGETS_DETAILS](state) {
    return state.availableWidgets?.clipping_feed_content
  },

  [get.TOP_AUTHORS](state) {
    return state.topAuthors
  },

  [get.TOP_COUNTRIES](state) {
    return state.topCountries
  },

  [get.TOP_BRANDS](state) {
    return state.topBrands
  },

  [get.TOP_LANGUAGES](state) {
    return state.topLanguages
  },

  [get.TOP_SHARING_SOURCES](state) {
    return state.topSharingSources
  },

  [get.SENTIMENT_TOP_SOURCES](state) {
    return state.sentimentTopSources
  },

  [get.SENTIMENT_TOP_COUNTRIES](state) {
    return state.sentimentTopCountries
  },

  [get.SENTIMENT_TOP_LANGUAGES](state) {
    return state.sentimentTopLanguages
  },

  [get.SENTIMENT_TOP_AUTHORS](state) {
    return state.sentimentTopAuthors
  },

  [get.SENTIMENT_FOR_PERIOD](state) {
    return state.sentimentForPeriod
  },

  [get.CONTENT_VOLUME_TOP_SOURCES](state) {
    return state.contentVolumeTopSources
  },

  [get.CONTENT_VOLUME_TOP_AUTHORS](state) {
    return state.contentVolumeTopAuthors
  },

  [get.CONTENT_VOLUME_TOP_COUNTRIES](state) {
    return state.contentVolumeTopCountries
  },

  [get.SENTIMENT_TOP_KEYWORDS_WIDGET](state) {
    return state.sentimentTopKeywordsWidget
  },

  [get.TOP_KEYWORDS_WIDGET](state) {
    return state.topKeywordsWidget
  },

  [get.TOP_KEYWORDS_BY_COUNTRY_WIDGET](state) {
    return state.topKeywordsByCountryWidget
  },

  [get.SENTIMENT_DIAGRAM](state) {
    return state.sentimentDiagram
  },

  [get.SENTIMENT_NUMBER_OF_RESULT](state) {
    return state.sentimentNumberOfResult
  },

  [get.AUTHORS_BY_COUNTRY](state) {
    return state.authorsByCountry
  },

  [get.SOURCES_BY_LANGUAGE](state) {
    return state.sourcesByLanguage
  },

  [get.SOURCES_BY_COUNTRY](state) {
    return state.sourcesByCountry
  },

  [get.OVERALL_TOP_SOURCES](state) {
    return state.overallTopSources
  },

  [get.DIMENSIONS](state) {
    return state.dimensions
  },

  [get.FILTERS_LANGUAGES](state) {
    return state.dimensionLanguages
  },

  [get.FILTERS_COUNTRIES](state) {
    return state.dimensionCountries
  },

  [get.FILTERS_AUTHORS](state) {
    return state.dimensionAuthors
  },

  [get.DIMENSIONS_LIST](state) {
    return {
      authors: state.dimensionAuthors
        ?.map((author) => author.entry_author)
        .filter((author) => author.trim()),
      countries: state.dimensionCountries
        ?.map((country) => country.feedlink__country)
        .filter((country) => country.trim()),
      languages: state.dimensionLanguages
        ?.map((language) => language.feed_language__language)
        .filter((language) => language.trim()),
      sources: state.dimensionSources
        ?.map((source) => source.feedlink__source1)
        .filter((source) => source.trim()),
    }
  },

  [get.SOCIAL_FILTERS_LIST](state) {
    return {
      authors: state.dimensionAuthors
        ?.map((author) => author.user_alias)
        .filter((author) => author.trim()),
      countries: state.dimensionCountries
        ?.map((country) => country.locationString)
        .filter((country) => country.trim()),
      languages: state.dimensionLanguages
        ?.map((language) => language.language)
        .filter((language) => language.trim()),
    }
  },

  [get.FILTERS_SOURCES](state) {
    return state.dimensionSources
  },

  [get.SELECTED_FILTERS](state) {
    return state.selectedFilters
  },

  [get.TEMPLATES](state) {
    return state.templates
  },

  [get.NEW_PROJECT_ID](state) {
    return state.newProjectId
  },

  [get.NEW_WORKSPACE_ID](state) {
    return state.newWorkspaceId
  },

  [get.COMPANY_USERS](state) {
    return state.companyUsers
  },

  [get.POSTS_NUMBER](state) {
    return state.numberOfPosts
  },

  [get.PAGES_NUMBER](state) {
    return state.numberOfPages
  },

  [get.INTERACTIVE_DATA](state) {
    return state.interactiveData
  },

  [get.INTERACTIVE_DATA_MODAL](state) {
    return state.inreractiveDataModal
  },

  [get.ALL_PROJECTS](state) {
    const onlineProjects = state.projects
    const socialProjects = state.social.projects
    return [...onlineProjects, ...socialProjects].sort(
      (a, b) =>
        a.title.toLowerCase().charCodeAt() - b.title.toLowerCase().charCodeAt()
    )
  },

  // Reports
  [get.REGULAR_REPORTS](state) {
    return state.regularReports
  },
  [get.CREATE_REPORTS_STEP](state) {
    return state.newReport.step
  },

  // Alerts

  [get.ALERTS](state) {
    return state.alerts
  },
  [get.CREATE_ALERT_STEP](state) {
    return state.newAlert.step
  },
}
