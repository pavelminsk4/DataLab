<template>
  <VolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialTopLanguagesWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topLanguages() {
      return (
        this.widgetDetails.widgetData || this.socialWidgets.topLanguages.data
      )
    },
    labels() {
      return this.topLanguages.map((el) => el.language)
    },
    chartValues() {
      return [
        {
          data: this.topLanguages.map((el) => el.language_count),
        },
      ]
    },
    widgetId() {
      return this.socialWidgets.topLanguages?.id
    },
  },
  created() {
    const hasCurrentData =
      this.topLanguages.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_TOP_LANGUAGES_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_LANGUAGES_WIDGET]),
  },
}
</script>
