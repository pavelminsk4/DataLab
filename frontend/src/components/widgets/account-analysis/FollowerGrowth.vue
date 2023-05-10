<template>
  <div>Follower growth s</div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'FollowerGrowth',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    followerGrowth() {
      console.log(this.widgetDetails)
      return this.accountAnalysisWidgets.followerGrowth
    },
  },
  created() {
    if (!this.followerGrowth.length) {
      this[action.GET_FOLLOWER_GROWTH]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_FOLLOWER_GROWTH]),
  },
}
</script>

<style lang="scss" scoped></style>
