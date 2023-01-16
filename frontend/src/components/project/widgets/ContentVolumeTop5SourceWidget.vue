<template>
  <WidgetsLayout
    v-if="contentVolumeTopSources"
    :title="widgets['content_volume_top_5_source_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart :widget-data="contentVolumeTopSources" class="line-chart" />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LineChart from '@/components/project/widgets/charts/LineChart'

export default {
  name: 'ContentVolumeTop5SourceWidget',
  components: {LineChart, WidgetsLayout},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
    widgets: {
      type: [Array, Object],
      default: () => [],
    },
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
    })
  },
  computed: {
    ...mapGetters({
      contentVolumeTopSources: get.CONTENT_VOLUME_TOP_SOURCES,
    }),
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
