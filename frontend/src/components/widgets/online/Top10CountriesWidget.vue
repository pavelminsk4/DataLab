<template>
  <VolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'

export default {
  name: 'Top10CountriesWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      topCountries: get.TOP_COUNTRIES,
    }),
    labels() {
      return this.topCountries.map((el) => el.feedlink__country)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.topCountries.map((el) => el.country_count),
        },
      ]
    },
  },
  created() {
    this[action.GET_TOP_COUNTRIES_WIDGET]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_COUNTRIES_WIDGET]),
  },
}
</script>
