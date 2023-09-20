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

import VolumeWidget from '@/components/widgets/VolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'Top10CountriesWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    topCountries() {
      return (
        this.widgetDetails.widgetData || this.onlineWidgets.topCountries.data
      )
    },
    labels() {
      return this.topCountries.map((el) => el.feedlink__country)
    },
    chartValues() {
      return [
        {
          data: this.topCountries.map((el) => el.country_count),
        },
      ]
    },
    widgetId() {
      return this.onlineWidgets.topCountries.id
    },
  },
  created() {
    const hasCurrentData =
      this.topCountries.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      console.log('????')
      this[action.GET_TOP_COUNTRIES_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_COUNTRIES_WIDGET]),
  },
}
</script>
