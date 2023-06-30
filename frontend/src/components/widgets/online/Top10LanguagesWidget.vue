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
  name: 'Top10LanguagesWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
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
          data: this.topLanguages.map((el) => el.language_count),
        },
      ]
    },
  },
  created() {
    this[action.GET_TOP_LANGUAGES_WIDGET]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_LANGUAGES_WIDGET]),
  },
}
</script>
