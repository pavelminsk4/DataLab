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

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'Top10LanguagesWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    topLanguages() {
      return (
        this.widgetDetails.widgetData || this.onlineWidgets.topLanguages.data
      )
    },
    widgetId() {
      return this.onlineWidgets.topLanguages.id
    },
    labels() {
      return this.topLanguages.map((el) => el.feed_language__language)
    },
    chartValues() {
      return [
        {
          data: this.topLanguages.map((el) => el.language_count),
        },
      ]
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
