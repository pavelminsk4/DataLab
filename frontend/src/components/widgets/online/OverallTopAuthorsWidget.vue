<template>
  <OverallTopWidget
    :widget-details="widgetDetails"
    :widget-data="overallTopAuthors"
    :table-header="tableHeader"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import OverallTopWidget from '@/components/widgets/OverallTopWidget'

export default {
  name: 'OverallTopAuthorsWidget',
  components: {OverallTopWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      overallTopAuthors: get.OVERALL_TOP_AUTHORS,
    }),
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
    // if (!this.overallTopAuthors.length) {
    this[action.GET_OVERALL_TOP_AUTHORS]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
    // }
  },
  methods: {
    ...mapActions([action.GET_OVERALL_TOP_AUTHORS]),
  },
}
</script>
