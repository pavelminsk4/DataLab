<template>
  <div class="chart-types">
    <BaseRadio
      v-for="(item, index) in availableTypes"
      :key="item.name + index"
      v-model="selectedValueProxy"
      :id="item.name + index"
      :value="item.componentName"
      :label="item.name"
      class="radio-button"
    />
  </div>
</template>

<script>
import {widgetsConfig} from '@/lib/configs/widgetsConfigs'
import BaseRadio from '@/components/BaseRadio'

export default {
  name: 'ChartTypesRadio',
  components: {BaseRadio},
  props: {
    selected: {
      type: String,
      default: '',
    },
    widgetName: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      selectedValue: '',
    }
  },
  computed: {
    availableTypes() {
      return widgetsConfig[this.widgetName].availableTypes
    },
    selectedValueProxy: {
      get() {
        return this.selectedValue || this.selected
      },
      set(val) {
        this.selectedValue = val
        this.$emit('update-chart-type', this.selectedValue, 'newChartType')
      },
    },
  },
}
</script>

<style scoped>
.chart-types {
  margin-top: 20px;
}

.radio-button {
  margin: 12px 0;
}
</style>
