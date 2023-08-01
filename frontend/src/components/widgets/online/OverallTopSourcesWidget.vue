<template>
  <TopSourcesWidget
    :widget-details="widgetDetails"
    :widget-data="overallTopSources"
    :table-header="tableHeader"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import TopSourcesWidget from '@/components/widgets/TopSourcesWidget'

export default {
  name: 'OverallTopSourcesWidget',
  components: {TopSourcesWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      overallTopSources: get.OVERALL_TOP_SOURCES,
    }),
  },
  created() {
    this[action.GET_OVERALL_TOP_SOURCES]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
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
  },
  methods: {
    ...mapActions([action.GET_OVERALL_TOP_SOURCES]),
  },
}
</script>
