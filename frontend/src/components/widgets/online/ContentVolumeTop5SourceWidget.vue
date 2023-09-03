<template>
  <ContentVolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
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
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      contentVolumeTopSources: get.CONTENT_VOLUME_TOP_SOURCES,
    }),
  },
  created() {
    // if (!this.contentVolumeTopSources.length) {
    this[action.GET_CONTENT_VOLUME_TOP_SOURCES]({
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
    // }
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_SOURCES]),
  },
}
</script>
