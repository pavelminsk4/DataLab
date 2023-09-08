<template>
  <ContentVolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :content-volume-widget-data="contentVolumeTopAuthors"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'ContentVolumeTop5AuthorsWidget',
  components: {ContentVolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    contentVolumeTopAuthors() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.contentVolumeTopAuthors.data
      )
    },
    widgetId() {
      return this.onlineWidgets.contentVolumeTopAuthors?.id
    },
  },
  created() {
    const hasCurrentData =
      this.contentVolumeTopAuthors.length &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_CONTENT_VOLUME_TOP_AUTHORS]({
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
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_AUTHORS]),
  },
}
</script>
