<template>
  <WidgetsLayout
    v-if="topCountries && isGeneralWidget"
    :title="widgets['top_10_countries_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :values="values"
      :labels="labels"
      :chart-type="chartType"
      :is-display-legend="false"
    />
  </WidgetsLayout>

  <ChartsView
    v-else
    :values="values"
    :labels="labels"
    :chart-type="chartType"
    :is-display-legend="false"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'Top10CountriesWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    widgetId: {
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
      topCountries: get.TOP_COUNTRIES,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    values() {
      return this.topCountries.map((el) => el.country_count)
    },
    labels() {
      return this.topCountries.map((el) => el.feedlink__country)
    },
  },
  created() {
    this[action.GET_TOP_COUNTRIES_WIDGET]({
      projectId: this.projectId,
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_COUNTRIES_WIDGET]),
  },
}
</script>
