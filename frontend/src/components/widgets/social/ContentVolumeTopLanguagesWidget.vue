<template>
  <ContentVolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :content-volume-widget-data="contentVolumeTopLanguages"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialContentVolumeTopLanguagesWidget',
  components: {ContentVolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    contentVolumeTopLanguages() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.contentVolumeTopLanguages.data
      )
    },
    widgetId() {
      return this.socialWidgets.contentVolumeTopLanguages?.id
    },
  },
  created() {
    const hasCurrentData =
      this.contentVolumeTopLanguages.length &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_CONTENT_VOLUME_TOP_LANGUAGES]({
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
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_LANGUAGES]),
  },
}
</script>
