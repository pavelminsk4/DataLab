<template>
  <ContentVolumeWidget
    :title="widgetDetails.title"
    :chartType="widgetDetails.chartType"
    :widget-id="widgetDetails.widgetId"
    :is-widget="isWidget"
    :content-volume-widget-data="contentVolumeTopAuthors"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialContentVolumeTopAuthorsWidget',
  components: {ContentVolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
    projectId: {type: Number, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    contentVolumeTopAuthors() {
      return this.socialWidgets.contentVolumeTopAuthors
    },
  },
  created() {
    if (!this.contentVolumeTopAuthors.length) {
      this[action.GET_CONTENT_VOLUME_TOP_AUTHORS]({
        projectId: this.projectId,
        value: {
          author_dim_pivot: this.widgetDetails.author_dim_pivot || null,
          language_dim_pivot: this.widgetDetails.language_dim_pivot || null,
          country_dim_pivot: this.widgetDetails.country_dim_pivot || null,
          sentiment_dim_pivot: this.widgetDetails.sentiment_dim_pivot || null,
          source_dim_pivot: this.widgetDetails.source_dim_pivot || null,
          smpl_freq: this.widgetDetails.aggregation_period,
        },
        widgetId: this.widgetDetails.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_AUTHORS]),
  },
}
</script>
