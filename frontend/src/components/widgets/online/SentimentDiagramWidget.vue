<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-values="chartValues"
      :chart-type="chartType"
      :is-display-legend="!isSettings"
    />
  </component>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'SentimentDiagram',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      sentimentDiagram: get.SENTIMENT_DIAGRAM,
    }),
    chartType() {
      return (
        this.newChartType ||
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType
      )
    },
    labels() {
      return ['Positive', 'Negative', 'Neutral'].map((el) => el + ' posts')
    },
    chartValues() {
      return [
        {
          data: Object.values(this.sentimentDiagram),
          colors: ['#00b884', '#ed2549', '#516bee'],
        },
      ]
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  created() {
    this[action.GET_SENTIMENT_DIAGRAM]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_DIAGRAM]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetDetails.id, 'author')
    },
  },
}
</script>
