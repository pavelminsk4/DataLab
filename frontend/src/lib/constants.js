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
    {name: 'summary_widget'},
    {name: 'content_volume_top_5_source_widget'},
    {name: 'sentiment_for_period_widget'},
    {name: 'volume_widget'},
    {name: 'top_10_countries_widget', isFullWidth: true},
    {name: 'top_10_authors_by_volume_widget'},
    {name: 'top_keywords'},
  ],
  sentiment: [
    {name: 'sentiment_number_of_results'},
    {name: 'sentiment_diagram'},
    {name: 'sentiment_top_10_authors_widget'},
    {name: 'top_keywords'},
    {name: 'sentiment_top_10_sources_widget', isFullWidth: true},
    {name: 'sentiment_top_10_countries_widget'},
    {name: 'sentiment_top_10_languages_widget'},
    {name: 'sentiment_top_keywords'},
  ],
  demography: [
    {name: 'top_sharing_sources', isFullWidth: false},
    {name: 'sources_by_language', isFullWidth: false},
    {name: 'overall_top_sources', isFullWidth: true},
    {name: 'sources_by_country', isFullWidth: false},
  ],
  influencers: [
    {name: 'top_sharing_sources', isFullWidth: false},
    {name: 'authors_by_country', isFullWidth: false},
    {name: 'overall_top_authors', isFullWidth: true},
    {name: 'overall_top_sources', isFullWidth: true},
    {name: 'sources_by_language', isFullWidth: false},
    {name: 'authors_by_language', isFullWidth: false},
    {name: 'authors_by_sentiment', isFullWidth: false},
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
    {name: 'sentiment_top_keywords'},
  ],
  demography: [
    {name: 'top_sharing_sources', isFullWidth: false},
    {name: 'authors_by_language', isFullWidth: false},
    {name: 'overall_top_authors', isFullWidth: true},
    {name: 'top_authors_by_gender', isFullWidth: true},
    {name: 'authors_by_location', isFullWidth: false},
    {name: 'authors_by_gender', isFullWidth: false},
  ],
  influencers: [
    {name: 'top_sharing_sources', isFullWidth: false},
    {name: 'authors_by_sentiment', isFullWidth: false},
    {name: 'overall_top_authors', isFullWidth: true},
    {name: 'authors_by_gender', isFullWidth: false},
    {name: 'authors_by_language', isFullWidth: false},
  ],
}

export const accountAnalysisWidgetsList = {
  dashboard: [
    {name: 'summary', isFullWidth: true, minHeight: 230},
    {name: 'profile_timeline', isFullWidth: true},
    {name: 'follower_growth', isFullWidth: true},
    {name: 'most_frequent_post_types', isFullWidth: false},
    {name: 'most_frequent_media_types', isFullWidth: false},
    {name: 'most_engaging_post_types', isFullWidth: false},
    {name: 'most_engaging_media_types', isFullWidth: false},
  ],
  optimization: [
    {name: 'summary', isFullWidth: true, minHeight: 230},
    {name: 'top_hashtags', isFullWidth: true},
    {name: 'optimal_post_length', isFullWidth: false},
    {name: 'optimal_number_of_hashtags', isFullWidth: false},
    {name: 'average_engagements_by_day', isFullWidth: true},
  ],
}

export const PREDEFINED_COLORS = ['#EE51AF', '#00B884', '#516BEE', '#DD8500']
