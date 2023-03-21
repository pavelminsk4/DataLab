<template>
  <SummaryWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :summary-widget-data="summary"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {isAllEmptyFields} from '@lib/utilities'

import SummaryWidget from '@/components/widgets/SummaryWidget'

export default {
  name: 'OnlineSummaryWidget',
  components: {SummaryWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      summary: get.SUMMARY_WIDGET,
    }),
  },
  created() {
    if (isAllEmptyFields(this.summary)) {
      this[action.GET_SUMMARY_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGET]),
  },
}
</script>
