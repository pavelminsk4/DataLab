<template>
  <FollowerGrowthWidget
    v-if="!isAllEmptyFields(followerGrowth)"
    :widget-data="followerGrowth"
    :widget-details="widgetDetails"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import FollowerGrowthWidget from '@/components/widgets/FollowerGrowthWidget'
import {isAllEmptyFields} from '@lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'FollowerGrowth',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {
    FollowerGrowthWidget,
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    followerGrowth() {
      return this.accountAnalysisWidgets.followerGrowth
    },
  },
  created() {
    if (isAllEmptyFields(this.followerGrowth)) {
      this[action.GET_FOLLOWER_GROWTH]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_FOLLOWER_GROWTH]),
    isAllEmptyFields,
  },
}
</script>
