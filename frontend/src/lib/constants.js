export const months = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December',
]

export const weekDays = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
]

export const years = [
  1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,
  1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995,
  1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
  2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
  2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034,
  2035, 2036, 2037, 2038, 2039, 2040,
]

export const onlineWidgetsList = {
  summary: [
    {name: 'summary'},
    {name: 'volume'},
    {name: 'sentiment_for_period', isFullWidth: true},
    {name: 'top_sources', isFullWidth: true},
    {name: 'top_authors'},
    {name: 'top_keywords'},
  ],
  sentiment: [
    {name: 'sentiment_number_of_results'},
    {name: 'sentiment_diagram'},
    {name: 'sentiment_top_sources', isFullWidth: true},
    {name: 'sentiment_top_countries'},
    {name: 'sentiment_top_authors'},
    {name: 'sentiment_top_languages'},
    {name: 'sentiment_top_keywords'},
  ],
  demography: [
    {name: 'sources_by_country', isFullWidth: false},
    {name: 'authors_by_country', isFullWidth: false},
    {name: 'languages_by_country', isFullWidth: true},
    {name: 'sentiment_top_countries', isFullWidth: true},
    {name: 'top_keywords', isFullWidth: false},
    {name: 'top_keywords_by_country', isFullWidth: false},
  ],
  influencers: [
    {name: 'top_sharing_sources', isFullWidth: false},
    {name: 'authors_by_language', isFullWidth: false},
    {name: 'overall_top_sources', isFullWidth: true},
    {name: 'overall_top_authors', isFullWidth: true},
    {name: 'authors_by_country', isFullWidth: false},
    {name: 'authors_by_sentiment', isFullWidth: false},
    {name: 'sources_by_language', isFullWidth: true},
  ],
}

export const socialWidgetsList = {
  summary: [
    {name: 'summary'},
    {name: 'sentiment'},
    {name: 'content_volume'},
    {name: 'top_keywords'},
    {name: 'top_authors'},
    {name: 'gender_volume'},
  ],
  sentiment: [
    {name: 'sentiment_number_of_results'},
    {name: 'sentiment_diagram'},
    {name: 'sentiment_authors'},
    {name: 'sentiment_locations'},
    {name: 'sentiment_languages'},
    {name: 'sentiment_by_gender'},
    {name: 'sentiment_top_keywords', isFullWidth: true},
  ],
  demography: [
    {name: 'top_keywords'},
    {name: 'keywords_by_location'},
    {name: 'authors_by_location', isFullWidth: true},
    {name: 'languages_by_location', isFullWidth: true},
    {name: 'sentiment_locations', isFullWidth: true},
    {name: 'authors_by_gender', isFullWidth: true},
    {name: 'gender_by_location', isFullWidth: true},
  ],
  influencers: [
    {name: 'top_sharing_sources', isFullWidth: false},
    {name: 'authors_by_sentiment', isFullWidth: false},
    {name: 'overall_top_authors', isFullWidth: true},
    {name: 'top_authors_by_gender', isFullWidth: true},
    {name: 'authors_by_location', isFullWidth: false},
    {name: 'authors_by_gender', isFullWidth: false},
    {name: 'authors_by_language', isFullWidth: true},
  ],
}

export const accountAnalysisWidgetsList = {
  AccountActivity: {
    dashboard: [
      {name: 'summary', isFullWidth: true, minHeight: 230},
      {name: 'profile_timeline', isFullWidth: true},
      {name: 'follower_growth', isFullWidth: true},
      {name: 'most_frequent_post_types', isFullWidth: false},
      {name: 'most_frequent_media_types', isFullWidth: false},
      {name: 'most_engaging_post_types', isFullWidth: false},
      {name: 'most_engaging_media_types', isFullWidth: false},
      {name: 'top_posts_by_engagements', isFullWidth: true},
    ],
    optimization: [
      {name: 'summary', isFullWidth: true, minHeight: 230},
      {name: 'optimal_post_time', isFullWidth: true},
      {name: 'best_times_to_post', isFullWidth: false},
      {name: 'optimal_post_length', isFullWidth: false},
      {name: 'top_hashtags', isFullWidth: true},
      {name: 'optimal_number_of_hashtags', isFullWidth: true},
      {name: 'average_engagements_by_day', isFullWidth: true},
    ],
  },

  Mentions: {
    dashboard: [
      {name: 'mention_summary', isFullWidth: true, minHeight: 230},
      {name: 'mention_timeline', isFullWidth: true},
      {name: 'mention_sentiment', isFullWidth: false},
      {name: 'most_frequent_mention_media_types', isFullWidth: false},
      {name: 'top_mentions_by_engagements', isFullWidth: true},
    ],
    optimization: [
      {name: 'mention_summary', isFullWidth: true, minHeight: 230},
      {name: 'audience_mention_time', isFullWidth: true},
      {name: 'average_engagements_by_day_for_mentions', isFullWidth: true},
    ],
  },
}

export const comparisonWidgetsList = {
  online: {
    summary: [
      {name: 'summary', isFullWidth: true},
      {name: 'content_volume'},
      {name: 'top_authors'},
      {name: 'sentiment'},
      {name: 'top_sources'},
      {name: 'top_keywords', isFullWidth: true},
      {name: 'top_languages'},
      {name: 'top_countries'},
    ],
    sentiment: [
      {name: 'sentiment_number_of_results'},
      {name: 'sentiment'},
      {name: 'top_keywords_by_sentiment', isFullWidth: true},
      {name: 'sentiment_by_locations', isFullWidth: true},
      {name: 'sentiment_by_period', isFullWidth: true},
      {name: 'sentiment_top_languages', isFullWidth: true},
      {name: 'sentiment_top_authors', isFullWidth: true},
    ],

    demography: [
      {name: 'top_keywords', isFullWidth: true},
      {name: 'top_languages_by_location', isFullWidth: true},
      {name: 'sentiment_by_locations', isFullWidth: true},
    ],

    influencers: [
      {name: 'top_sharing_sources', isFullWidth: true},
      {name: 'overall_top_sources', isFullWidth: true},
      {name: 'overall_top_authors', isFullWidth: true},
    ],
  },
  social: {
    summary: [
      {name: 'summary', isFullWidth: true, minHeight: 100},
      {name: 'content_volume', isFullWidth: true},
      {name: 'top_authors'},
      {name: 'sentiment'},
      {name: 'top_keywords', isFullWidth: true},
      {name: 'top_languages'},
      {name: 'top_locations'},
    ],
    sentiment: [
      {name: 'sentiment_number_of_results'},
      {name: 'sentiment'},
      {name: 'top_keywords_by_sentiment', isFullWidth: true},
      {name: 'sentiment_by_locations', isFullWidth: true},
      {name: 'sentiment_by_period', isFullWidth: true},
      {name: 'sentiment_top_languages', isFullWidth: true},
      {name: 'sentiment_top_authors', isFullWidth: true},
    ],
    demography: [
      {name: 'top_keywords', isFullWidth: true},
      {name: 'top_languages_by_location', isFullWidth: true},
      {name: 'sentiment_by_locations', isFullWidth: true},
      {name: 'top_gender_by_location', isFullWidth: true},
    ],
    influencers: [
      {name: 'top_sharing_sources', isFullWidth: true},
      {name: 'overall_top_authors', isFullWidth: true},
      {name: 'top_authors_by_gender', isFullWidth: true},
    ],
  },
}

export const expertModeFilters = {
  online: ['author', 'country', 'language', 'source', 'sentiment'],
  social: ['followers', 'location', 'author', 'sentiment', 'language'],
}

export const PREDEFINED_COLORS = [
  '#5500FF',
  '#5A12B3',
  '#00B1FF',
  '#BA0DE5',
  '#FF007A',
  '#FFCC01',
  '#00D9A5',
  '#FF6B00',
  '#69D101',
  '#D6F2FF',
  '#E1BDE2',
  '#F8FFAB',
  '#20812A',
  '#D5FCD4',
  '#FEDDD6',
]

export const SENTIMENT_COLORS = {
  positive: '#00b884',
  neutral: '#516bee',
  negative: '#ed2549',
}

export const GENDER_COLORS = {
  male: '#516BEE',
  female: '#FD7271',
}

export const COMPARISON_COLORS = ['#516BEE', '#00B1FF', '#00BF7F']

export const SORT_BY = {
  ASCENDING: 'ascending',
  DESCENDING: 'descending',
}

export const SENTIMENT = {
  NEUTRAL: 'neutral',
  NEGATIVE: 'negative',
  POSITIVE: 'positive',
}

export const SORTED_SENTIMENT = [
  SENTIMENT.NEUTRAL,
  SENTIMENT.POSITIVE,
  SENTIMENT.NEGATIVE,
]

export const LANGUAGES = {
  ENGLISH: 'en',
  ARABIC: 'ar',
}

export const MODES = {
  CREATE_REPORT: 'CREATE_REPORT',
}
