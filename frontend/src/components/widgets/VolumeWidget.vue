<template>
  <component
    :is="widgetWrapper"
    :title="title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView2
      :labels="labels"
      :chart-type="chartType"
      :charts-data="chartsData"
      :is-display-legend="isWidget"
      @open-sentiment-interactive-modal="openInteractiveModal"
    />
  </component>
</template>

<script>
import ChartsView2 from '@/components/charts/ChartsView2'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'VolumeWidget',
  components: {ChartsView2, WidgetsLayout},
  props: {
    isWidget: {type: Boolean, default: true},
    title: {type: String, required: true},
    widgetId: {type: Number, required: true},
    chartType: {type: String, required: true},
    labels: {type: Array, required: true},
    chartsData: {type: Array, required: true, default: () => {}},
  },
  computed: {
    widgetWrapper() {
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
  },
  methods: {
    openInteractiveModal(source, sentiment) {
      this.$emit('open-sentiment-interactive', source, sentiment, this.widgetId)
    },
  },
}
</script>

<style scoped></style>
