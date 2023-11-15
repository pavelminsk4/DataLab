<template>
  <Doughnut :data="chartData" :options="chartOptions" />
</template>

<script>
import {Doughnut} from 'vue-chartjs'
import {defaultDate} from '@/lib/utilities'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'
import translate from '@lib/mixins/translate.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
ChartJS.defaults.font = {
  family: 'Poppins',
  weight: 'normal',
  size: 14,
}

export default {
  name: 'DoughnutChart',
  mixins: [translate],
  components: {Doughnut},
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Object, default: () => {}},
    hasAnimation: {type: Boolean, default: true},
    isSentimentChart: {type: Boolean, default: false},
  },
  computed: {
    colors() {
      const defaultColors = [
        '#6AC7F0',
        '#CDC6FF',
        '#01A4EE',
        '#FFBB01',
        '#00CC87',
        '#551EB9',
        '#7C59ED',
        '#FFE499',
        '#7ACCB0',
        '#8779B2',
      ]
      return this.chartValues[0].colors || defaultColors
    },
    chartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          easing: 'easeInOutQuad',
          duration: this.hasAnimation ? 520 : 0,
        },
        onClick: (e, dataOptions) => {
          this.$emit(
            'open-interactive-data',
            this.labels[dataOptions[0].index],
            dataOptions[0].element.$datalabels[0].$context.dataset.label?.toLowerCase() ||
              this.chartValues[0].label
          )
        },
        onHover: (event, chartElement) => {
          const target = event.native ? event.native.target : event.target
          target.style.cursor = chartElement[0] ? 'pointer' : 'default'
        },
        plugins: {
          datalabels: {
            display: false,
          },
          legend: {
            position: 'bottom',
            labels: {font: {size: 16}},
          },
          tooltip: {
            xAlign: 'center',
            yAlign: 'bottom',
            titleFont: {weight: 'normal'},
            titleColor: 'black',
            titleAlign: 'center',
            bodyAlign: 'center',
            bodyColor: 'black',
            backgroundColor: 'rgba(255, 255, 255, 0.96)',
            displayColors: !!this.chartValues[0]?.colors,
            callbacks: {
              title(context) {
                return context[0].label
              },
              label(context) {
                return 'Results: ' + context.formattedValue
              },
            },
          },
        },
      }
    },
    chartData() {
      const isDate = !isNaN(new Date(this.labels[0]))
      let currentLabels = [...this.labels]
      if (isDate) {
        currentLabels = currentLabels.map((date) =>
          defaultDate(date, this.platformLanguage)
        )
      }
      return {
        labels: this.isSentimentChart
          ? currentLabels.map((label) => this.translatedText(label))
          : currentLabels,
        datasets: [
          {
            backgroundColor: this.colors,
            data: this.chartValues[0].data,
            options: {plugins: {datalabels: {display: false}}},
          },
        ],
      }
    },
  },
}
</script>
