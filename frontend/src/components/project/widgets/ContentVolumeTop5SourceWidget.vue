<template>
  <WidgetsLayout
    v-if="contentVolumeTopSources && isGeneralWidget"
    :title="widgets['content_volume_top_5_source_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :widget-data="contentVolumeTopSources"
      :chart-type="chartType"
    />
  </WidgetsLayout>

  <ChartsView
    v-else
    :widget-data="contentVolumeTopSources"
    :chart-type="chartType"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'ContentVolumeTop5SourceWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
    widgetId: {
      type: Number,
      required: true,
    },
    widgets: {
      type: [Array, Object],
      default: () => [],
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
      contentVolumeTopSources: get.CONTENT_VOLUME_TOP_SOURCES,
    }),
  },
  created() {
    this[action.GET_CONTENT_VOLUME_TOP_SOURCES]({
      projectId: this.projectId,
      value: {
        author_dim_pivot:
          this.widgets['content_volume_top_5_source_widget'].author_dim_pivot ||
          null,
        language_dim_pivot:
          this.widgets['content_volume_top_5_source_widget']
            .language_dim_pivot || null,
        country_dim_pivot:
          this.widgets['content_volume_top_5_source_widget']
            .country_dim_pivot || null,
        sentiment_dim_pivot:
          this.widgets['content_volume_top_5_source_widget']
            .sentiment_dim_pivot || null,
        source_dim_pivot:
          this.widgets['content_volume_top_5_source_widget'].source_dim_pivot ||
          null,
        smpl_freq:
          this.widgets['content_volume_top_5_source_widget'].aggregation_period,
      },
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_SOURCES]),
  },
}
</script>

<style scoped>
.line-chart {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
</style>
