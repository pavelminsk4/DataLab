<template>
  <apex-chart
    type="heatmap"
    height="350"
    :options="options"
    :series="chartValues"
    @click="showInteractiveData"
    @dataPointMouseEnter="hoverMouse"
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
    tooltipLabels: {type: [Array, String], required: false},
  },
  created() {
    this.xAxis = this.chartValues[0].data.map((_value, index) => {
      const hours = index % 12 || 12
      const meridiem = index > 12 ? 'PM' : 'AM'
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
      tooltip: {
        y: {
          formatter: undefined,
          title: {
            formatter: (seriesName) =>
              this.tooltipLabels ? `${this.tooltipLabels}:` : seriesName,
          },
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
  methods: {
    showInteractiveData(event, chartContext, config) {
      this.$emit(
        'open-interactive-data',
        this.chartValues[config.seriesIndex].name,
        config.dataPointIndex
      )
    },
    hoverMouse(event) {
      event.target.style.cursor = 'pointer'
    },
  },
}
</script>
