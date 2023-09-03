const widget = {id: 0, data: []}

const state = {
  summary: {id: 0, data: {}},
  clippingFeedContent: widget,
  contentVolume: widget,
  genderVolume: widget,
  genderByLocation: widget,
  authorsByLanguage: widget,
  authorsByLocation: widget,
  authorsBySentiment: widget,
  authorsByGender: widget,

  overallTopAuthors: widget,
  languagesByLocation: widget,
  topLocations: widget,
  topLanguages: widget,
  topAuthors: widget,
  topKeywords: widget,
  topKeywordsByCountry: widget,
  topSharingSources: widget,
  topAuthorsByGender: widget,

  contentVolumeTopLocations: widget,
  contentVolumeTopAuthors: widget,
  contentVolumeTopLanguages: widget,

  sentimentTopAuthors: {id: 0, data: {}},
  sentimentTopLocations: {id: 0, data: {}},
  sentimentTopLanguages: {id: 0, data: {}},
  sentimentForPeriod: widget,
  sentimentDiagram: {id: 0, data: {}},
  sentimentNumberOfResult: {id: 0, data: {}},
  sentimentTopKeywords: {id: 0, data: {}},
  sentimentByGender: {id: 0, data: {}},
}

export default state
