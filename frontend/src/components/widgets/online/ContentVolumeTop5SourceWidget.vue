<template>
  <ContentVolumeWidget
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
    :content-volume-widget-data="contentVolumeTopSources"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'

export default {
  name: 'ContentVolumeTop5SourceWidget',
  components: {ContentVolumeWidget},
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
      contentVolumeTopSources: get.CONTENT_VOLUME_TOP_SOURCES,
    }),
    widgetWrapper() {
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
  },
  created() {
    if (!this.contentVolumeTopSources.length) {
      this[action.GET_CONTENT_VOLUME_TOP_SOURCES]({
        projectId: this.projectId,
        value: {
          author_dim_pivot:
            this.availableWidgets.content_volume_top_5_source_widget
              .author_dim_pivot || null,
          language_dim_pivot:
            this.availableWidgets.content_volume_top_5_source_widget
              .language_dim_pivot || null,
          country_dim_pivot:
            this.availableWidgets.content_volume_top_5_source_widget
              .country_dim_pivot || null,
          sentiment_dim_pivot:
            this.availableWidgets.content_volume_top_5_source_widget
              .sentiment_dim_pivot || null,
          source_dim_pivot:
            this.availableWidgets.content_volume_top_5_source_widget
              .source_dim_pivot || null,
          smpl_freq:
            this.availableWidgets.content_volume_top_5_source_widget
              .aggregation_period,
        },
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_SOURCES]),
  },
}
</script>
