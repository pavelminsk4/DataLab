<template>
  <section class="container">
    <table class="table">
      <thead>
        <tr>
          <th class="label" />
          <th class="chart" />
        </tr>
      </thead>
      <tbody>
        <tr v-for="(label, index) in labels" :key="label">
          <td class="label">{{ label || 'No name' }}</td>
          <td class="chart">
            <StackedBarChart
              :chart-values="chartValues[index]"
              :isShowTooltips="true"
              :iteractive-label="label"
              @click="getCurrentIndex(index)"
              @open-interactive-data="openInteractiveData"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
import StackedBarChart from '@components/charts/StackedBarChart'

export default {
  name: 'TopEntitiesBarChart',
  components: {StackedBarChart},
  props: {
    labels: {type: Array, required: true},
    chartValues: {type: Array, required: true},
  },
  data() {
    return {
      currentDataIndex: null,
    }
  },
  inject: {
    barHeight: {
      default: () => '35px',
    },
  },
  methods: {
    getCurrentIndex(index) {
      this.currentDataIndex = index
    },
    openInteractiveData(label, option) {
      this.$emit(
        'open-interactive-data-multi',
        label,
        option,
        this.currentDataIndex
      )
      this.$emit('open-interactive-data', label, option, this.currentDataIndex)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;

  height: 100%;

  .table {
    table-layout: fixed;
    width: 100%;
    height: 100%;
    .label {
      width: 15%;

      font-size: 12px;
      color: var(--typography-secondary-color);
    }
    tbody {
      tr {
        td {
          vertical-align: middle;
        }
        .chart {
          padding-left: 10px;
          .chart-container {
            width: 100%;
            height: v-bind(barHeight);
          }
        }
      }
    }
  }
}
</style>
