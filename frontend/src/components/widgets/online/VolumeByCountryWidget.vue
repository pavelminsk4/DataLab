<template>
  <CountriesWidget
    :widget-details="widgetDetails"
    :chart-values="chartValues"
    :new-chart-type="newChartType"
    :is-settings="isSettings"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import CountriesWidget from '@components/widgets/CountriesWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'AuthorsByCountryWidget',
  components: {CountriesWidget},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    authorsByCountry() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.authorsByCountry.data
      )
    },
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
    widgetId() {
      return this.onlineWidgets.authorsByCountry?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.authorsByCountry) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_AUTHORS_BY_COUNTRY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_COUNTRY]),
    isAllFieldsEmpty,
  },
}
</script>
