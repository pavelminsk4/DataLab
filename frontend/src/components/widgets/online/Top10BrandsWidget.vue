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
  name: 'Top10BrandsWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    topBrands() {
      return this.widgetDetails.widgetData || this.onlineWidgets.topBrands.data
    },
    labels() {
      return this.topBrands.map((el) => el.feedlink__source1)
    },
    chartValues() {
      return [
        {
          data: this.topBrands.map((el) => el.brand_count),
        },
      ]
    },
  },
  created() {
    const hasCurrentData =
      this.topBrands.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_TOP_BRANDS_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_BRANDS_WIDGET]),
  },
}
</script>
