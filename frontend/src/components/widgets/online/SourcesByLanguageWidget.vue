<template>
  <VolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'

export default {
  name: 'SourcesByLanguageWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sourcesByLanguage: get.SOURCES_BY_LANGUAGE,
    }),
    labels() {
      return this.sourcesByLanguage.map((el) => el.feed_language__language)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.sourcesByLanguage.map((el) => el.source_count),
        },
      ]
    },
  },
  created() {
    this[action.GET_SOURCES_BY_LANGUAGE]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_SOURCES_BY_LANGUAGE]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetDetails.id, 'author')
    },
  },
}
</script>
