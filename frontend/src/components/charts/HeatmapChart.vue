<template>
  <apex-chart
    type="heatmap"
    height="350"
    :options="options"
    :series="chartValues"
  />
</template>

<script>
import VueApexCharts from 'vue3-apexcharts'

export default {
  name: 'HeatmapChart',
  components: {
    apexChart: VueApexCharts,
  },
  props: {
    chartValues: {type: Array, required: true},
  },
  created() {
    this.xAxis = this.chartValues[0].data.map((_value, index) => {
      const hours = index === 0 ? 12 : index % 12
      const meridiem = hours > 12 ? 'PM' : 'AM'
      return `${hours} ${meridiem}`
    })

    this.options = {
      chart: {
        height: 350,
        type: 'heatmap',
        toolbar: {
          show: false,
        },
      },
      dataLabels: {
        enabled: false,
      },
      colors: ['#7300FF'],
      title: {
        enabled: false,
      },
      xaxis: {
        axisTicks: {
          show: false,
        },
        categories: this.xAxis,
        tooltip: {
          enabled: false,
        },
      },
      grid: {
        show: true,
        position: 'front',
        xaxis: {
          lines: {
            show: true,
          },
        },
        yaxis: {
          lines: {
            show: true,
          },
        },
      },
    }
  },
}
</script>

<style lang="scss" scoped></style>
