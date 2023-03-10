<template>
  <WidgetsLayout
    v-if="isGeneralWidget"
    :title="this.widgets.content_volume.title"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :values="values"
      :chart-type="chartType"
      :is-display-legend="false"
    />
  </WidgetsLayout>

  <ChartsView
    v-else
    :labels="labels"
    :values="values"
    :chart-type="chartType"
    :is-display-legend="false"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'
import {action} from '@store/modules/social/constants'
import {defaultDate} from '@/lib/utilities'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

const {mapActions} = createNamespacedHelpers('social')

export default {
  name: 'VolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    volume: {
      type: [Array, Object],
      default: () => [],
    },
    projectId: {
      type: [String, Number],
      required: true,
    },
    widgetId: {
      type: Number,
      required: true,
    },
    isOpenWidget: {
      type: Boolean,
      required: true,
    },
    chartType: {
      type: String,
      required: true,
    },
    isGeneralWidget: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
      volumeWidgetData: get.VOLUME_WIDGET,
    }),
    volumeData() {
      return Object.values(this.volume)
    },
    labels() {
      return this.volumeData.map((el) => this.defaultDate(el.date))
    },
    isLineChart() {
      return this.volumeValues?.length > 7
    },
    values() {
      return this.volumeData.map((el) => el.created_count)
    },
  },
  created() {
    if (this.isOpenWidget && !this.volume.length) {
      this[action.GET_CONTENT_VOLUME_WIDGET]({
        projectId: this.projectId,
        value: {
          author_dim_pivot:
            this.widgets.content_volume.author_dim_pivot || null,
          language_dim_pivot:
            this.widgets.content_volume.language_dim_pivot || null,
          country_dim_pivot:
            this.widgets.content_volume.country_dim_pivot || null,
          sentiment_dim_pivot:
            this.widgets.content_volume.sentiment_dim_pivot || null,
          source_dim_pivot:
            this.widgets.content_volume.source_dim_pivot || null,
          smpl_freq: this.widgets.content_volume.aggregation_period,
        },
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_WIDGET]),
    defaultDate,
  },
}
</script>
