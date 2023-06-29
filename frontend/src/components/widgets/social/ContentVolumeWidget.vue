<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
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
import {get} from '@store/constants'
import {action} from '@store/constants'
import {defaultDate} from '@/lib/utilities'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialContentVolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
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
      return this.widgetDetails.widgetData || this.socialWidgets.contentVolume
    },
    labels() {
      return this.contentVolumeWidgetData.map((el) => defaultDate(el.date))
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.contentVolumeWidgetData.map((el) => el.created_count),
        },
      ]
    },
  },
  created() {
    if (
      !this.widgetDetails.widgetData &&
      !this.contentVolumeWidgetData.length
    ) {
      this[action.GET_CONTENT_VOLUME_WIDGET]({
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
    ...mapActions([action.GET_CONTENT_VOLUME_WIDGET]),
  },
}
</script>
