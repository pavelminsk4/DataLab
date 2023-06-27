<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    :widget-details="widgetDetails"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-values="chartValues"
      :chart-type="chartType"
      :widget-details="widgetDetails"
      :is-legend-displayed="!isSettings"
    />
  </component>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {defaultDate} from '@/lib/utilities'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'VolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      volumeWidget: get.VOLUME_WIDGET,
    }),
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    chartType() {
      return (
        this.newChartType ||
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType
      )
    },
    volumeData() {
      return Object.values(this.volumeWidget)
    },
    labels() {
      return this.volumeData.map((el) => this.defaultDate(el.date))
    },
    chartValues() {
      return [
        {color: '#516BEE', data: this.volumeData.map((el) => el.created_count)},
      ]
    },
  },
  created() {
    if (!this.volumeWidget.length) {
      this[action.GET_VOLUME_WIDGET]({
        projectId: this.widgetDetails.projectId,
        value: {
          author_dim_pivot: this.widgetDetails.author_dim_pivot || null,
          language_dim_pivot: this.widgetDetails.language_dim_pivot || null,
          country_dim_pivot: this.widgetDetails.country_dim_pivot || null,
          sentiment_dim_pivot: this.widgetDetails.sentiment_dim_pivot || null,
          source_dim_pivot: this.widgetDetails.source_dim_pivot || null,
          aggregation_period: this.widgetDetails.aggregation_period,
        },
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_VOLUME_WIDGET]),
    defaultDate,
  },
}
</script>
