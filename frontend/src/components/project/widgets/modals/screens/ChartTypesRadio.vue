<template>
  <div class="chart-types">
    <BaseRadio
      v-for="(item, index) in availableTypes"
      :key="item + index"
      v-model="selectedValueProxy"
      :id="item + index"
      :value="item"
      :label="item"
    />
  </div>
</template>

<script>
import {modalWidgetsConfig} from '@/lib/configs/widgetsConfigs'
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
      return modalWidgetsConfig[this.widgetName].availableTypes
    },
    selectedValueProxy: {
      get() {
        return this.selectedValue || this.selected
      },
      set(val) {
        this.selectedValue = val
        this.$emit('update-chart-type', this.selectedValue)
      },
    },
  },
}
</script>

<style scoped>
.chart-types {
  margin-top: 60px;
}
</style>
