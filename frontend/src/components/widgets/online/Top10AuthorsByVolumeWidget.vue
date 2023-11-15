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

import VolumeWidget from '@components/widgets/VolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'Top10AuthorsByVolumeWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    topAuthors() {
      return this.widgetDetails.widgetData || this.onlineWidgets.topAuthors.data
    },
    widgetId() {
      return this.onlineWidgets.topAuthors.id
    },
    labels() {
      return this.topAuthors.map((el) => el.entry_author)
    },
    chartValues() {
      return [
        {
          data: this.topAuthors.map((el) => el.author_posts_count),
        },
      ]
    },
  },
  created() {
    const hasCurrentData =
      this.topAuthors.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_TOP_AUTHORS_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
  },
}
</script>
