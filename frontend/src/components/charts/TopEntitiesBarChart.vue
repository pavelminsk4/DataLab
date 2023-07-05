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
          <td class="label">{{ label }}</td>
          <td class="chart">
            <StackedBarChart
              :chart-values="chartValues[index]"
              :isShowTooltips="true"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
import StackedBarChart from '@/components/charts/StackedBarChart'

export default {
  name: 'TopEntitiesBarChart',
  components: {StackedBarChart},
  props: {
    labels: {type: Array, required: true},
    chartValues: {type: Array, required: true},
  },
  inject: {
    barHeight: {
      default: () => '35px',
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
  padding: 20px;

  .table {
    table-layout: fixed;
    width: 100%;
    height: 100%;
    .label {
      width: 15%;
    }
    tbody {
      tr {
        td {
          vertical-align: middle;
        }
        .chart {
          width: 85%;
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
