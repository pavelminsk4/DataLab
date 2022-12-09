<template>
  <WidgetsLayout
    :title="availableWidgets['top_10_languages_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <Doughnut
      :chart-options="chartOptions"
      :chart-data="chartData"
      :plugins="plugins"
      class="doughnut-chart-widget"
    />
  </WidgetsLayout>
</template>

<script>
import {Doughnut} from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from 'chart.js'

import ChartDataLabels from 'chartjs-plugin-datalabels'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  ChartDataLabels
)

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

export default {
  name: 'Top10LanguagesWidget',
  components: {
    WidgetsLayout,
    Doughnut,
  },
  data() {
    return {
      plugins: [ChartDataLabels],
    }
  },
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_TOP_LANGUAGES_WIDGET](this.projectId)
  },
  computed: {
    ...mapGetters({
      topLanguages: get.TOP_LANGUAGES,
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    labels() {
      return this.topLanguages.map((el) => el.feed_language__language)
    },
    values() {
      return this.topLanguages.map((el) => el.language_count)
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            backgroundColor: [
              '#055FFC',
              '#7A9EF9',
              '#47F9B9',
              '#47F979',
              '#95F947',
              '#F5F947',
              '#F6AA37',
              '#F63737',
              '#F63787',
              '#D930F4',
            ],
            cutout: '75%',
            borderColor: 'transparent',
            spacing: 10,
            data: this.values,
          },
        ],
      }
    },
    chartOptions() {
      return {
        plugins: {
          legend: {
            position: 'right',
            labels: {
              color: 'white',
              font: {
                size: 12,
              },
            },
          },
          datalabels: {
            color: 'white',
            textAlign: 'center',
            font: {
              size: 8,
            },
          },
        },
        responsive: true,
        maintainAspectRatio: false,
      }
    },
  },
  methods: {
    ...mapActions([action.GET_TOP_LANGUAGES_WIDGET]),
  },
}
</script>

<style scoped>
.doughnut-chart-widget {
  width: 100%;
  margin-top: 25px;

  cursor: pointer;
}
</style>
