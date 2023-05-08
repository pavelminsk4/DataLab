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
import MostFrequentMediaTypes from '@/components/widgets/account-analysis/MostFrequentMediaTypes'
import MostFrequentPostTypes from '@/components/widgets/account-analysis/MostFrequentPostTypes'
import MostEngagingPostTypes from '@/components/widgets/account-analysis/MostEngagingPostTypesWidget'

export default {
  name: 'AccountAnalysisMainWidget',
  components: {
    ProfileTimeline,
    Summary,
    MostFrequentMediaTypes,
    MostFrequentPostTypes,
    MostEngagingPostTypes,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
