<template>
  <WidgetsLayout
    :title="availableWidgets['top_10_languages_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView :labels="labels" :values="values" :chart-type="chartType" />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'Top10LanguagesWidget',
  components: {
    ChartsView,
    WidgetsLayout,
  },
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    chartType: {
      type: String,
      required: true,
    },
  },
  created() {
    this[action.GET_TOP_LANGUAGES_WIDGET](this.projectId)
  },
  computed: {
    ...mapGetters({
      topLanguages: get.TOP_LANGUAGES,
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    labels() {
      return this.topLanguages.map((el) => el.feed_language__language)
    },
    values() {
      return this.topLanguages.map((el) => el.language_count)
    },
  },
  methods: {
    ...mapActions([action.GET_TOP_LANGUAGES_WIDGET]),
  },
}
</script>
