<template>
  <WidgetsLayout
    v-if="topAuthors && isGeneralWidget"
    :title="widgets['top_10_authors_by_volume_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView :labels="labels" :values="values" :chart-type="chartType" />
  </WidgetsLayout>

  <ChartsView
    v-else
    :labels="labels"
    :values="values"
    :chart-type="chartType"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'Top10AuthorsByVolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    chartType: {
      type: String,
      required: true,
    },
    isGeneralWidget: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    ...mapGetters({
      topAuthors: get.TOP_AUTHORS,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    values() {
      return this.topAuthors.map((el) => el.author_posts_count)
    },
    labels() {
      return this.topAuthors.map((el) => el.entry_author)
    },
  },
  created() {
    this[action.GET_TOP_AUTHORS_WIDGET](this.projectId)
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
  },
}
</script>
