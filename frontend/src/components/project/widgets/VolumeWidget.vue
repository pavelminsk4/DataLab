<template>
  <WidgetsLayout
    :title="this.widgets['volume_widget'].title"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView :labels="labels" :values="values" :chart-type="chartType" />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import {defaultDate} from '@/lib/utilities'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

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
    isOpenWidget: {
      type: Boolean,
      required: true,
    },
    chartType: {
      type: String,
      required: true,
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
      this[action.GET_VOLUME_WIDGET]({
        projectId: this.projectId,
        value: {
          author_dim_pivot:
            this.widgets['volume_widget'].author_dim_pivot || null,
          language_dim_pivot:
            this.widgets['volume_widget'].language_dim_pivot || null,
          country_dim_pivot:
            this.widgets['volume_widget'].country_dim_pivot || null,
          sentiment_dim_pivot:
            this.widgets['volume_widget'].sentiment_dim_pivot || null,
          source_dim_pivot:
            this.widgets['volume_widget'].source_dim_pivot || null,
          smpl_freq: this.widgets['volume_widget'].aggregation_period,
        },
      })
    }
  },
  methods: {
    ...mapActions([action.GET_VOLUME_WIDGET]),
    defaultDate,
  },
}
</script>
