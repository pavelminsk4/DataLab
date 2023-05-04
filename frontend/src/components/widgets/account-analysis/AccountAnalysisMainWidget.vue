<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import ProfileTimeline from '@/components/widgets/account-analysis/ProfileTimeline'

export default {
  name: 'AccountAnalysisMainWidget',
  components: {ProfileTimeline},
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
