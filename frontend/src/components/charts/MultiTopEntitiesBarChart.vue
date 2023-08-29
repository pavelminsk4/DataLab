<template>
  <div class="multi-container">
    <div
      v-for="({columnsLabels, labels, values}, index) in chartValues"
      :key="columnsLabels"
      class="column-container"
      @click="getCurrentIndex(index)"
    >
      <TopEntitiesBarChart
        v-bind="$attrs"
        :labels="labels"
        :chart-values="values"
        @open-interactive-data-multi="openInteractiveData"
      />

      <div class="column-name">{{ columnsLabels }}</div>
    </div>

    <BaseLegends v-if="labels.length" :legends="labels" />
  </div>
</template>

<script>
import TopEntitiesBarChart from '@/components/charts/TopEntitiesBarChart'
import BaseLegends from '@/components/charts/BaseLegends'

export default {
  name: 'MultiTopEntitiesBarChart',
  components: {BaseLegends, TopEntitiesBarChart},
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Array, required: true},
  },
  data() {
    return {
      currentDataIndex: null,
    }
  },
  methods: {
    getCurrentIndex(index) {
      this.currentDataIndex = index
    },
    openInteractiveData(label, option) {
      this.$emit('open-interactive-data', label, option, this.currentDataIndex)
    },
  },
}
</script>

<style lang="scss" scoped>
.multi-container {
  position: relative;

  display: flex;
  justify-content: space-around;

  gap: 24px;
  width: 100%;
  height: 90%;
}

.column-container {
  display: flex;
  flex-direction: column;
  align-items: center;

  gap: 12px;
}

.column-name {
  font-size: 16px;
  font-weight: 500;
  color: var(--typography-primary-color);
}
</style>
