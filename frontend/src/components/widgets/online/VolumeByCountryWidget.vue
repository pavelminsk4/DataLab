<template>
  <CountriesWidget
    :widget-details="widgetDetails"
    :chart-values="chartValues"
    :new-chart-type="newChartType"
    :is-settings="isSettings"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import CountriesWidget from '@/components/widgets/CountriesWidget'

export default {
  name: 'AuthorsByCountryWidget',
  components: {CountriesWidget},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({authorsByCountry: get.AUTHORS_BY_COUNTRY}),
    chartValues() {
      let newChartValues = []

      this.authorsByCountry.forEach((element) => {
        newChartValues.push({
          country: element.feedlink__country,
          count: element.author_count,
        })
      })

      return newChartValues
    },
  },
  created() {
    this[action.GET_AUTHORS_BY_COUNTRY]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_COUNTRY]),
  },
}
</script>
