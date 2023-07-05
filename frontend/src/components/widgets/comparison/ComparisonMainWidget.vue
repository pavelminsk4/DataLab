<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import ContentVolume from '@/components/widgets/comparison/ContentVolumeWidget'
import TopAuthors from '@/components/widgets/comparison/TopAuthorsWidget'
import Sentiment from '@/components/widgets/comparison/SentimentWidget'

export default {
  name: 'ComparisonMainWidget',
  components: {ContentVolume, TopAuthors, Sentiment},
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
