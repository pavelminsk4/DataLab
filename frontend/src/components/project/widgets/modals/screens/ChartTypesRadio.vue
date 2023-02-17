<template>
  <div class="chart-types">
    <BaseRadio
      v-for="(item, index) in typesOfCharts"
      :key="item + index"
      v-model="selectedValue"
      :id="item + index"
      :checked="item"
      :value="item"
      :label="item"
      @click="selectValue(item)"
    />
  </div>
</template>

<script>
import BaseRadio from '@/components/BaseRadio'
export default {
  name: 'ChartTypesRadio',
  components: {BaseRadio},
  data() {
    return {
      typesOfCharts: ['Line', 'Bar', 'Pie'],
      selectedValue: '',
    }
  },
  methods: {
    selectValue(item) {
      this.$emit('update-chart-type', item)
    },
  },
}
</script>

<style scoped>
.chart-types {
  margin-top: 60px;
}
</style>
