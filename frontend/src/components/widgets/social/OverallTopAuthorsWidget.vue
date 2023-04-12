<template>
  <OverallTopWidget
    :widget-details="widgetDetails"
    :widget-data="widgetData"
    :table-header="tableHeader"
  />
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
    this.tableHeader = [
      {name: '', width: '5%'},
      {name: 'Author', width: '15%'},
      {name: 'Gender', width: '15%'},
      {name: 'Media Type', width: '10%'},
      {name: 'Posts', width: '10%'},
      {name: 'Sentiment', width: '25%'},
      {name: 'Reach', width: '10%'},
      {name: 'Engagement', width: '10%'},
    ]
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
