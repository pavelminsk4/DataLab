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

export default {
  name: 'ComparisonMainWidget',
  components: {
    ContentVolume,
    TopAuthors,
    Sentiment,
    TopKeywords,
    Summary,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
