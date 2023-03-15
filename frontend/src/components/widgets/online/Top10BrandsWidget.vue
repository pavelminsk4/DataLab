<template>
  <VolumeWidget
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
    :labels="labels"
    :charts-data="chartsData"
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
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
    title: {type: String, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({
      topBrands: get.TOP_BRANDS,
    }),
    labels() {
      return this.topBrands.map((el) => el.feedlink__source1)
    },
    chartsData() {
      return [
        {
          color: '#516BEE',
          data: this.topBrands.map((el) => el.brand_count),
        },
      ]
    },
  },
  created() {
    this[action.GET_TOP_BRANDS_WIDGET]({
      projectId: this.projectId,
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_BRANDS_WIDGET]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetId, 'author')
    },
  },
}
</script>

<style scoped></style>
