<template>
  <VolumeWidget
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
    :labels="labels"
    :charts-data="chartsData"
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
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
    title: {type: String, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({
      topAuthors: get.TOP_AUTHORS,
    }),
    labels() {
      return this.topAuthors.map((el) => el.entry_author)
    },
    chartsData() {
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
      projectId: this.projectId,
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetId, 'author')
    },
  },
}
</script>

<style scoped></style>
