<template>
  <component
    :is="widgetWrapper"
    :title="title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-values="chartValues"
      :chart-type="chartType"
      :is-display-legend="isWidget"
    />
  </component>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import {defaultDate} from '@/lib/utilities'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'SentimentForPeriodWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    isWidget: {type: Boolean, default: true},
    title: {type: String, required: true},
    widgetId: {type: Number, required: true},
    projectId: {type: Number, required: true},
    chartType: {type: String, required: true},
    availableWidgets: {type: Object, required: true, default: () => {}},
  },
  computed: {
    ...mapGetters({
      sentimentForPeriod: get.SENTIMENT_FOR_PERIOD,
    }),
    widgetWrapper() {
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
    labels() {
      let labelsCollection = []

      this.sentimentForPeriod.forEach((sentiment) => {
        Object.keys(sentiment).forEach((i) => {
          labelsCollection.push(i)
        })
      })

      return labelsCollection.map((el) => this.defaultDate(el))
    },
    chartValues() {
      let neutral = []
      let positive = []
      let negative = []

      this.sentimentForPeriod.forEach((sentiment) => {
        Object.values(sentiment).forEach((data) => {
          neutral.push(data.neutral)
          positive.push(data.positive)
          negative.push(data.negative)
        })
      })

      return [
        {label: 'Neutral', color: '#516BEE', data: neutral},
        {label: 'Positive', color: '#00B884', data: positive},
        {label: 'Negative', color: '#ED2549', data: negative},
      ]
    },
  },
  created() {
    this[action.GET_SENTIMENT_FOR_PERIOD]({
      projectId: this.projectId,
      value: {
        author_dim_pivot:
          this.availableWidgets.sentiment_for_period_widget.author_dim_pivot ||
          null,
        language_dim_pivot:
          this.availableWidgets.sentiment_for_period_widget
            .language_dim_pivot || null,
        country_dim_pivot:
          this.availableWidgets.sentiment_for_period_widget.country_dim_pivot ||
          null,
        sentiment_dim_pivot:
          this.availableWidgets.sentiment_for_period_widget
            .sentiment_dim_pivot || null,
        source_dim_pivot:
          this.availableWidgets.sentiment_for_period_widget.source_dim_pivot ||
          null,
        smpl_freq:
          this.availableWidgets.sentiment_for_period_widget.aggregation_period,
      },
      widgetId: this.widgetId,
    })
  },
  methods: {
    defaultDate,
    ...mapActions([action.GET_SENTIMENT_FOR_PERIOD]),
  },
}
</script>
