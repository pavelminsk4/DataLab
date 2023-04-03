<template>
  <OverallTopWidget :widget-details="widgetDetails" :widget-data="widgetData" />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import OverallTopWidget from '@/components/widgets/OverallTopWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')
export default {
  components: {OverallTopWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    widgetData() {
      return this.socialWidgets.overallTopAuthors
    },
  },
  created() {
    if (!this.widgetData.length) {
      this[action.GET_OVERALL_TOP_AUTHORS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OVERALL_TOP_AUTHORS]),
  },
}
</script>

<style lang="scss" scoped></style>
