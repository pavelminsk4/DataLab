<template>
  <TopSourcesWidget
    :widget-details="widgetDetails"
    :widget-data="widgetData"
    :table-header="tableHeader"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import TopSourcesWidget from '@components/widgets/TopSourcesWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'OverallTopSourcesWidget',
  components: {TopSourcesWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    widgetData() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.overallTopSources.data
      )
    },
    widgetId() {
      return this.onlineWidgets.overallTopSources?.id
    },
  },
  created() {
    this.tableHeader = [
      {name: '', width: '5%'},
      {
        name: 'Source',
        width: '30%',
        sortProperty: 'name',
        hasSort: true,
      },
      {
        name: 'Posts',
        width: '10%',
        sortProperty: 'posts',
        hasSort: true,
      },
      {name: 'Sentiment', width: '35%'},
      {
        name: 'Reach',
        width: '10%',
        sortProperty: 'reach',
        hasSort: true,
      },
      {
        name: 'Engagement',
        width: '10%',
        sortProperty: 'engagements',
        hasSort: true,
      },
    ]

    const hasCurrentData =
      this.widgetData.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_OVERALL_TOP_SOURCES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OVERALL_TOP_SOURCES]),
  },
}
</script>
