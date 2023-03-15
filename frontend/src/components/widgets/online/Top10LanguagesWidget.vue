<template>
  <VolumeWidget
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'

export default {
  name: 'Top10LanguagesWidget',
  components: {VolumeWidget},
  props: {
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
    title: {type: String, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({
      topLanguages: get.TOP_LANGUAGES,
    }),
    labels() {
      return this.topLanguages.map((el) => el.feed_language__language)
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
    this[action.GET_TOP_LANGUAGES_WIDGET]({
      projectId: this.projectId,
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_LANGUAGES_WIDGET]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetId, 'author')
    },
  },
}
</script>
