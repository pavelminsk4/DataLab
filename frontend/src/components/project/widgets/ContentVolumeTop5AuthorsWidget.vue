<template>
  <WidgetsLayout
    v-if="contentVolumeTopAuthors && isGeneralWidget"
    :title="widgets['content_volume_top_5_authors_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :chart-type="chartType"
      :widget-data="contentVolumeTopAuthors"
      class="line-chart"
    />
  </WidgetsLayout>

  <ChartsView
    v-else
    :chart-type="chartType"
    :widget-data="contentVolumeTopAuthors"
    class="line-chart"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'ContentVolumeTop5AuthorsWidget',
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
  created() {
    this[action.GET_CONTENT_VOLUME_TOP_AUTHORS]({
      projectId: this.projectId,
      value: {
        author_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .author_dim_pivot || null,
        language_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .language_dim_pivot || null,
        country_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .country_dim_pivot || null,
        sentiment_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .sentiment_dim_pivot || null,
        source_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .source_dim_pivot || null,
        smpl_freq:
          this.widgets['content_volume_top_5_authors_widget']
            .aggregation_period,
      },
      widgetId: this.widgetId,
    })
  },
  computed: {
    ...mapGetters({
      contentVolumeTopAuthors: get.CONTENT_VOLUME_TOP_AUTHORS,
    }),
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_AUTHORS]),
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
