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
  name: 'AuthorsByLanguageWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      authorsByLanguage: get.AUTHORS_BY_LANGUAGE,
    }),
    labels() {
      return this.authorsByLanguage.map((el) => el.feed_language__language)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.authorsByLanguage.map((el) => el.author_count),
        },
      ]
    },
  },
  created() {
    this[action.GET_AUTHORS_BY_LANGUAGE]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_LANGUAGE]),
  },
}
</script>
