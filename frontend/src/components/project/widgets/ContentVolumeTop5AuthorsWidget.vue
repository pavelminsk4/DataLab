<template>
  <WidgetsLayout
    v-if="contentVolumeTopAuthors"
    :title="widgets['content_volume_top_5_authors_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart :widget-data="contentVolumeTopAuthors" class="line-chart" />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LineChart from '@/components/project/widgets/charts/LineChart'

export default {
  name: 'ContentVolumeTop5AuthorsWidget',
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
