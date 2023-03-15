<template>
  <VolumeWidget
    :title="widgetDetails.title"
    :chartType="widgetDetails.chartType"
    :widget-id="widgetDetails.widgetId"
    :is-widget="isWidget"
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
    projectId: {type: Number, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topLanguages() {
      return this.socialWidgets.topLanguages
    },
    labels() {
      return this.topLanguages.map((el) => el.language)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.topLanguages.map((el) => el.language_count),
        },
      ]
    },
  },
  created() {
    if (!this.topLanguages.length) {
      this[action.GET_TOP_LANGUAGES_WIDGET]({
        projectId: this.projectId,
        widgetId: this.widgetDetails.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_LANGUAGES_WIDGET]),
    openInteractiveModal(val) {
      this.$emit(
        'open-interactive-data',
        val,
        this.widgetDetails.widgetId,
        'author'
      )
    },
  },
}
</script>
