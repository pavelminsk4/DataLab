<template>
  <component
    :is="widgetWrapper"
    :title="customTitle || widgetDetails.title"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <section class="container">
      <table class="table">
        <thead>
          <tr>
            <th class="label" />
            <th class="chart" />
          </tr>
        </thead>
        <tbody>
          <tr v-for="(label, index) in widgetData.labels" :key="label">
            <td class="label">{{ label }}</td>
            <td class="chart">
              <ChartsView
                :chart-values="widgetData.chartValues[index]"
                :chart-type="chartType"
                :widget-details="widgetDetails"
                :tooltips="['en', 'fr']"
              />
            </td>
          </tr>
        </tbody>
      </table>
    </section>
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'TopEntitiesByStackedBar',
  components: {
    ChartsView,
    WidgetsLayout,
  },
  props: {
    widgetData: {type: Object, required: true},
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    customTitle: {type: String, default: ''},
  },
  computed: {
    chartType() {
      return (
        this.widgetDetails.chart_type || this.widgetDetails.defaultChartType
      )
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;

  height: 100%;
  padding: 20px;

  .table {
    table-layout: fixed;
    width: 100%;
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
            height: 35px;
            width: 100%;
          }
        }
      }
    }
  }
}
</style>
