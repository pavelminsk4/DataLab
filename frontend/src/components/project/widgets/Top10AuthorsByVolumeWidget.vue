<template>
  <WidgetsLayout
    v-if="topAuthors"
    :title="widgets['top_10_authors_by_volume_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <PieChart :labels="labels" :values="values" />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import PieChart from '@/components/project/widgets/charts/PieChart'

export default {
  name: 'Top10AuthorsByVolumeWidget',
  components: {PieChart, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_TOP_AUTHORS_WIDGET](this.projectId)
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
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
  },
}
</script>
