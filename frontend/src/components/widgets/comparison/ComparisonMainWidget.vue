<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import ContentVolume from '@/components/widgets/comparison/ContentVolumeWidget'

export default {
  name: 'ComparisonMainWidget',
  components: {ContentVolume},
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
