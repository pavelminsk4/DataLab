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

import OverallTopWidget from '@components/widgets/OverallTopWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'OverallTopAuthorsWidget',
  components: {OverallTopWidget},
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
        this.onlineWidgets.overallTopAuthors.data
      )
    },
    widgetId() {
      return this.onlineWidgets.overallTopAuthors?.id
    },
  },
  created() {
    this.tableHeader = [
      {name: '', width: '5%'},
      {name: 'Author', width: '30%', sortProperty: 'name', hasSort: true},
      {name: 'Posts', width: '10%', sortProperty: 'posts', hasSort: true},
      {name: 'Sentiment', width: '35%'},
      {name: 'Reach', width: '10%', sortProperty: 'reach', hasSort: true},
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
