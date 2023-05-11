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
import FollowerGrowth from '@/components/widgets/account-analysis/FollowerGrowth'
import MostFrequentMediaTypes from '@/components/widgets/account-analysis/MostFrequentMediaTypes'
import MostFrequentPostTypes from '@/components/widgets/account-analysis/MostFrequentPostTypes'
import MostEngagingPostTypes from '@/components/widgets/account-analysis/MostEngagingPostTypes'
import MostEngagingMediaTypes from '@/components/widgets/account-analysis/MostEngagingMediaTypes'
import OptimalPostLength from '@/components/widgets/account-analysis/OptimalPostLength'
import TopHashtags from '@/components/widgets/account-analysis/TopHashtags'

export default {
  name: 'AccountAnalysisMainWidget',
  components: {
    ProfileTimeline,
    Summary,
    MostFrequentMediaTypes,
    MostFrequentPostTypes,
    MostEngagingPostTypes,
    FollowerGrowth,
    OptimalPostLength,
    MostEngagingMediaTypes,
    TopHashtags,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
