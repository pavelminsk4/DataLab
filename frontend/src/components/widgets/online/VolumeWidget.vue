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
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {defaultDate} from '@/lib/utilities'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

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
      onlineWidgets: get.ONLINE_WIDGETS,
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
    contentVolumeWidgetData() {
      return this.widgetDetails.widgetData || this.onlineWidgets.volume.data
    },
    labels() {
      return this.contentVolumeWidgetData.map((el) => el.date)
    },
    chartValues() {
      return [
        {
          data: this.contentVolumeWidgetData.map((el) => el.created_count),
        },
      ]
    },
    widgetId() {
      return this.onlineWidgets.volume?.id
    },
  },
  created() {
    const hasCurrentData =
      this.contentVolumeWidgetData.length &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
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
