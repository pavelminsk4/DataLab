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
import OptimalNumberOfHashtags from '@/components/widgets/account-analysis/OptimalNumberOfHashtags'
import TopHashtags from '@/components/widgets/account-analysis/TopHashtags'
import AverageEngagementsByDay from '@/components/widgets/account-analysis/AverageEngagementsByDay'
import OptimalPostTime from '@/components/widgets/account-analysis/OptimalPostTime'
import TopPostsByEngagements from '@/components/widgets/account-analysis/TopPostsByEngagements'
import BestTimesToPost from '@/components/widgets/account-analysis/BestTimesToPost'

import MentionTimeline from '@/components/widgets/account-analysis/mentions/MentionTimeline'
import MostFrequentMentionMediaTypes from '@/components/widgets/account-analysis/mentions/MostFrequentMentionMediaTypes'

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
    OptimalNumberOfHashtags,
    AverageEngagementsByDay,
    OptimalPostTime,
    TopPostsByEngagements,
    BestTimesToPost,
    MentionTimeline,
    MostFrequentMentionMediaTypes,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
