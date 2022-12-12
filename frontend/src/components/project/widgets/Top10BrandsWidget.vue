<template>
  <WidgetsLayout
    v-if="topBrands"
    :title="widgets['top_10_brands_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <DoughnutChart :labels="labels" :values="values" />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import DoughnutChart from '@/components/project/widgets/charts/DoughnutChart'
export default {
  name: 'Top10BrandsWidget',
  components: {DoughnutChart, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    if (!this.topBrands.length) {
      this[action.GET_TOP_BRANDS_WIDGET](this.projectId)
    }
  },
  computed: {
    ...mapGetters({
      topBrands: get.TOP_BRANDS,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    values() {
      return this.topBrands.map((el) => el.brand_count)
    },
    labels() {
      return this.topBrands.map((el) => el.feedlink__source1)
    },
  },
  methods: {
    ...mapActions([action.GET_TOP_BRANDS_WIDGET]),
  },
}
</script>
