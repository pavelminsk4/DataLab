<template>
  <WidgetsLayout
    v-if="topCountries"
    :title="widgets['top_10_countries_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <HorizontalBarChart :chart-values="values" :chart-labels="labels" />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import HorizontalBarChart from '@/components/project/widgets/charts/HorizontalBarChart'

export default {
  name: 'Top10CountriesWidget',
  components: {HorizontalBarChart, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_TOP_COUNTRIES_WIDGET](this.projectId)
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
  methods: {
    ...mapActions([action.GET_TOP_COUNTRIES_WIDGET]),
  },
}
</script>
