<template>
  <SentimentColumnsStackedBarsWidget
    v-if="widgetDetails.widgetData"
    :widget-details="widgetDetails"
  />
</template>

<script>
import SentimentColumnsStackedBarsWidget from '@/components/widgets/SentimentColumnsStackedBarsWidget'

export default {
  name: 'ComparisonSentimentByAuthorsWidget',
  components: {SentimentColumnsStackedBarsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '32px',
  },
}
</script>
