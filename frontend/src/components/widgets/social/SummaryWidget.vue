<template>
  <SummaryWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :summary-widget-data="summary"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'
import {action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import SummaryWidget from '@/components/widgets/SummaryWidget'

const {mapActions, mapGetters: mapGettersSocial} =
  createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialSummaryWidget',
  components: {SummaryWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGettersSocial({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    summary() {
      return this.socialWidgets.summary
    },
  },
  async created() {
    if (isAllFieldsEmpty(this.summary)) {
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
