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
  name: 'Top10BrandsWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      topBrands: get.TOP_BRANDS,
    }),
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
    this[action.GET_TOP_BRANDS_WIDGET]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_BRANDS_WIDGET]),
  },
}
</script>
