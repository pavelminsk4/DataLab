<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import Summary from '@/components/widgets/social/SummaryWidget'
import ClippingFeedContent from '@/components/widgets/social/ClippingFeedContentWidget'
import ContentVolume from '@/components/widgets/social/ContentVolumeWidget'
import GenderVolume from '@/components/widgets/social/GenderVolumeWidget'

import TopLocations from '@/components/widgets/social/TopLocationsWidget'
import TopLanguages from '@/components/widgets/social/TopLanguagesWidget'
import TopAuthors from '@/components/widgets/social/TopAuthorsWidget'
import TopKeywords from '@/components/widgets/social/TopKeywordsWidget'
import KeywordsByLocation from '@/components/widgets/social/TopKeywordsByCountryWidget'
import TopSharingSources from '@/components/widgets/social/TopSharingSourcesWidget'

import ContentVolumeTopLocations from '@/components/widgets/social/ContentVolumeTopLocationsWidget'
import ContentVolumeTopAuthors from '@/components/widgets/social/ContentVolumeTopAuthorsWidget'
import ContentVolumeTopLanguages from '@/components/widgets/social/ContentVolumeTopLanguagesWidget'
import AuthorsByLanguage from '@/components/widgets/social/AuthorsByLanguageWidget'
import AuthorsByLocation from '@/components/widgets/social/AuthorsByLocationWidget'
import AuthorsBySentiment from '@/components/widgets/social/AuthorsBySentimentWidget'
import AuthorsByGender from '@/components/widgets/social/AuthorsByGenderWidget'

import Sentiment from '@/components/widgets/social/SentimentForPeriodWidget'
import SentimentAuthors from '@/components/widgets/social/SentimentTopAuthorsWidget'
import SentimentLanguages from '@/components/widgets/social/SentimentTopLanguagesWidget'
import SentimentLocations from '@/components/widgets/social/SentimentTopLocationsWidget'
import SentimentByGender from '@/components/widgets/social/SentimentByGenderWidget'
import SentimentDiagram from '@/components/widgets/social/SentimentDiagramWidget'
import SentimentNumberOfResults from '@/components/widgets/social/SentimentNumberOfResultWidget'
import SentimentTopKeywords from '@/components/widgets/social/SentimentTopKeywordsWidget'

import OverallTopAuthors from '@/components/widgets/social/OverallTopAuthorsWidget'
import TopAuthorsByGender from '@/components/widgets/social/TopAuthorsByGenderWidget'
import LanguagesByLocation from '@/components/widgets/social/LanguagesByLocationWidget'

export default {
  name: 'SocialMainWidget',
  components: {
    ClippingFeedContent,
    Summary,
    ContentVolume,
    TopLocations,
    TopLanguages,
    TopAuthors,
    TopKeywords,
    TopSharingSources,
    ContentVolumeTopLocations,
    ContentVolumeTopAuthors,
    ContentVolumeTopLanguages,
    Sentiment,
    SentimentAuthors,
    SentimentLanguages,
    SentimentLocations,
    SentimentByGender,
    SentimentTopKeywords,
    GenderVolume,
    SentimentDiagram,
    SentimentNumberOfResults,
    OverallTopAuthors,
    TopAuthorsByGender,
    AuthorsByLanguage,
    AuthorsByLocation,
    AuthorsBySentiment,
    AuthorsByGender,
    KeywordsByLocation,
    LanguagesByLocation,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
