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
  name: 'Top10AuthorsByVolumeWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      topAuthors: get.TOP_AUTHORS,
    }),
    labels() {
      return this.topAuthors.map((el) => el.entry_author)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.topAuthors.map((el) => el.author_posts_count),
        },
      ]
    },
  },
  created() {
    this[action.GET_TOP_AUTHORS_WIDGET]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
  },
}
</script>
