const widgetWithArray = {id: 0, data: []}
const widgetWithObject = {id: 0, data: {}}

const state = {
  summary: widgetWithObject,
  clippingFeedContent: widgetWithArray,
  contentVolume: widgetWithArray,
  genderVolume: widgetWithArray,
  genderByLocation: widgetWithObject,
  authorsByLanguage: widgetWithArray,
  authorsByLocation: widgetWithArray,
  authorsBySentiment: widgetWithObject,
  authorsByGender: widgetWithObject,

  overallTopAuthors: widgetWithArray,
  languagesByLocation: widgetWithArray,
  topLocations: widgetWithArray,
  topLanguages: widgetWithArray,
  topAuthors: widgetWithArray,
  topKeywords: widgetWithArray,
  topKeywordsByCountry: widgetWithArray,
  topSharingSources: widgetWithArray,
  topAuthorsByGender: widgetWithArray,

  contentVolumeTopLocations: widgetWithArray,
  contentVolumeTopAuthors: widgetWithArray,
  contentVolumeTopLanguages: widgetWithArray,

  sentimentTopAuthors: widgetWithObject,
  sentimentTopLocations: widgetWithObject,
  sentimentTopLanguages: widgetWithObject,
  sentimentForPeriod: widgetWithArray,
  sentimentDiagram: widgetWithObject,
  sentimentNumberOfResult: widgetWithObject,
  sentimentTopKeywords: widgetWithObject,
  sentimentByGender: widgetWithObject,
}

export default state
