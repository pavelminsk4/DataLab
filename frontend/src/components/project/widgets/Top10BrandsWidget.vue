<template>
  <WidgetsLayout
    v-if="isGeneralWidget"
    :title="widgets['top_10_brands_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :values="values"
      :chart-type="chartType"
      :is-display-legend="false"
    />
  </WidgetsLayout>

  <ChartsView
    v-else
    :labels="labels"
    :values="values"
    :chart-type="chartType"
    :is-display-legend="false"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'Top10BrandsWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    widgetId: {
      type: Number,
      required: true,
    },
    chartType: {
      type: String,
      required: true,
    },
    isGeneralWidget: {
      type: Boolean,
      default: true,
    },
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
  created() {
    this[action.GET_TOP_BRANDS_WIDGET]({
      projectId: this.projectId,
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_TOP_BRANDS_WIDGET]),
  },
}
</script>
