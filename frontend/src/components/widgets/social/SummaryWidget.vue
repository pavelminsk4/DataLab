<template>
  <SummaryWidget
    v-bind="$attrs"
    :title="availableWidgets.summary.title"
    :project-id="projectId"
    :widget-id="widgetId"
    :summary-widget-data="summary"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'
import {action} from '@store/constants'
import {isAllEmptyFields} from '@lib/utilities'

import SummaryWidget from '@/components/widgets/SummaryWidget'

const {mapActions, mapGetters: mapGettersSocial} =
  createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialSummaryWidget',
  components: {SummaryWidget},
  props: {
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
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
    if (isAllEmptyFields(this.summary)) {
      this[action.GET_SUMMARY_WIDGET]({
        projectId: this.projectId,
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGET]),
  },
}
</script>
