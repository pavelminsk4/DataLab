<template>
  <VolumeWidget
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
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
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
    title: {type: String, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
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
      projectId: this.projectId,
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_COUNTRIES_WIDGET]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetId, 'author')
    },
  },
}
</script>
