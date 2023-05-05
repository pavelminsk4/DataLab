<template>
  <div>Most frequent media types</div>
  <!-- <VolumeWidget /> -->
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

const {mapGetters, mapActions} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

// import VolumeWidget from '../VolumeWidget.vue'
export default {
  name: 'MostFrequentMediaTypes',
  // components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      widgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mostFrequentMediaTypes() {
      return this.widgets.mostFrequentMediaTypes
    },
    labels() {
      return 'labels'
    },
    chartValues() {
      return 'chartValues'
    },
  },
  created() {
    if (!this.mostFrequentMediaTypes.length) {
      this[action.GET_MOST_FREQUENT_POST_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_FREQUENT_POST_TYPES]),
  },
}
</script>
