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
  name: 'SourcesByCountryWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sourcesByCountry: get.SOURCES_BY_COUNTRY,
    }),
    labels() {
      return this.sourcesByCountry.map((el) => el.feedlink__country)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.sourcesByCountry.map((el) => el.source_count),
        },
      ]
    },
  },
  created() {
    this[action.GET_SOURCES_BY_COUNTRY]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_SOURCES_BY_COUNTRY]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetDetails.id, 'author')
    },
  },
}
</script>
