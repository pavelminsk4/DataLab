<template>
  <component
    v-if="chartValues.length"
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    style="--widget-layout-content-padding: 5px 100px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div class="colored-keywords-wrapper">
      <ChartsView
        :chart-type="chartType"
        :chart-values="chartValues"
        :widget-details="widgetDetails"
      />
    </div>
  </component>
</template>

<script>
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'ColoredKeywordsWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    chartValues: {type: Array, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    chartType() {
      return (
        this.newChartType ||
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType ||
        'ColoredWordCloudChart'
      )
    },
  },
}
</script>

<style scoped>
.colored-keywords-wrapper {
  display: flex;

  height: 80%;
  min-height: 350px;
  padding: 50px;
}
</style>
