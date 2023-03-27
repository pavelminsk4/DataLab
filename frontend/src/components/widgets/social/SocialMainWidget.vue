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

import ContentVolumeByTopLocations from '@/components/widgets/social/ContentVolumeTopLocationsWidget'
import ContentVolumeByTopAuthors from '@/components/widgets/social/ContentVolumeTopAuthorsWidget'
import ContentVolumeByTopLanguages from '@/components/widgets/social/ContentVolumeTopLanguagesWidget'

import Sentiment from '@/components/widgets/social/SentimentForPeriodWidget'
import SentimentAuthors from '@/components/widgets/social/SentimentTopAuthorsWidget'
import SentimentLanguages from '@/components/widgets/social/SentimentTopLanguagesWidget'
import SentimentLocations from '@/components/widgets/social/SentimentTopLocationsWidget'
import SentimentByGender from '@/components/widgets/social/SentimentByGenderWidget'
<<<<<<< HEAD:frontend/src/components/widgets/social/SocialMainWidget.vue
import SentimentDiagram from '@/components/widgets/social/SentimentDiagramWidget'
import SentimentNumberOfResults from '@/components/widgets/social/SentimentNumberOfResultWidget'
=======
import SentimentTopKeywords from '@/components/widgets/social/SentimentTopKeywordsWidget'
>>>>>>> b26fbd8 (ADD: sentiment top keywords widget for social):frontend/src/components/widgets/social/MainWidget.vue

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
    ContentVolumeByTopLocations,
    ContentVolumeByTopAuthors,
    ContentVolumeByTopLanguages,
    Sentiment,
    SentimentAuthors,
    SentimentLanguages,
    SentimentLocations,
    SentimentByGender,
    SentimentTopKeywords,
    GenderVolume,
    SentimentDiagram,
    SentimentNumberOfResults,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
