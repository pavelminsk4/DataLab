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
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
