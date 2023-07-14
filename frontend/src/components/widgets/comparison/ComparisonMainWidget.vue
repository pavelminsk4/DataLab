<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import ContentVolume from '@/components/widgets/comparison/ContentVolumeWidget'
import TopKeywords from '@/components/widgets/comparison/TopKeywordsWidget'
import TopAuthors from '@/components/widgets/comparison/TopAuthorsWidget'
import Sentiment from '@/components/widgets/comparison/SentimentWidget'
import Summary from '@/components/widgets/comparison/SummaryWidget'
import TopLanguages from '@/components/widgets/comparison/TopLanguagesWidget'
import TopLocations from '@/components/widgets/comparison/TopLocationsWidget'
import SentimentNumberOfResults from '@/components/widgets/comparison/SentimentNumberOfResultsWidget'
import TopKeywordsBySentiment from '@/components/widgets/comparison/TopKeywordsBySentimentWidget'
import SentimentByLocations from '@/components/widgets/comparison/SentimentByLocationsWidget'
import SentimentByPeriod from '@/components/widgets/comparison/SentimentByPeriodWidget'
import SentimentTopLanguages from '@/components/widgets/comparison/SentimentByLanguagesWidget'
import SentimentTopAuthors from '@/components/widgets/comparison/SentimentByAuthorsWidget'

export default {
  name: 'ComparisonMainWidget',
  components: {
    ContentVolume,
    TopAuthors,
    Sentiment,
    TopKeywords,
    Summary,
    TopLanguages,
    TopLocations,
    SentimentNumberOfResults,
    TopKeywordsBySentiment,
    SentimentByLocations,
    SentimentByPeriod,
    SentimentTopLanguages,
    SentimentTopAuthors,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
