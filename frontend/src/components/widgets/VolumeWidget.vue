<template>
  <component
    :is="widgetWrapper"
    :title="title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
      :is-display-legend="isWidget"
      @open-sentiment-interactive-modal="openInteractiveModal"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'VolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    isWidget: {type: Boolean, default: true},
    title: {type: String, required: true},
    widgetId: {type: Number, required: true},
    chartType: {type: String, required: true},
    labels: {type: Array, required: true},
    chartValues: {type: Array, required: true, default: () => {}},
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
