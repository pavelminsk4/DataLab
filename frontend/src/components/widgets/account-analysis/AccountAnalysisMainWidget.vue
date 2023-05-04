<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import ProfileTimeline from '@/components/widgets/account-analysis/ProfileTimeline'
import Summary from '@/components/widgets/account-analysis/AccountAnalysisSummary'

export default {
  name: 'AccountAnalysisMainWidget',
  components: {ProfileTimeline, Summary},
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
