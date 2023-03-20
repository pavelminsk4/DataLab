<template>
  <component
    :is="widgetWrapper"
    :title="title"
    style="--widget-layout-content-padding: 50px 100px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
    />
  </component>
</template>

<script>
import {mapState} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'KeywordsWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    isWidget: {type: Boolean, default: true},
    title: {type: String, required: true},
    widgetId: {type: Number, required: true},
    chartType: {type: String, required: true},
    keywordsValues: {type: Array, required: true},
  },
  computed: {
    ...mapState(['loading']),
    widgetWrapper() {
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
    labels() {
      return this.keywordsValues.map((item) => item.key)
    },
    values() {
      return this.keywordsValues.map((item) => item.value)
    },
    chartValues() {
      return [{data: this.values}]
    },
  },
}
</script>
