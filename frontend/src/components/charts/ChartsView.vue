<template>
  <BaseSpinner v-if="loading" class="spinner" />

  <component
    v-else
    :is="chartType"
    :labels="labels"
    :chart-values="chartValues"
    :tooltip-Labels="tooltipLabels"
    :isLegendDisplayed="isLegendDisplayed"
    :has-animation="widgets.hasAnimation"
    :is-interactive-data-shown="isInteractiveDataShown"
    :is-sentiment-chart="isSentimentChart"
    @open-interactive-data="openInteractiveData"
  />
</template>

<script>
import {mapState, mapActions} from 'vuex'
import {action} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

import BaseSpinner from '@components/BaseSpinner'
import BarChart from '@components/charts/BarChart'
import PieChart from '@components/charts/PieChart'
import LineChart from '@components/charts/LineChart'
import MultiLineChart from '@components/charts/MultiLineChart'
import MultiRadarChart from '@components/charts/MultiRadarChart'
import RadarChart from '@components/charts/RadarChart'
import HorizontalBarChart from '@components/charts/HorizontalBarChart'
import DoughnutChart from '@components/charts/DoughnutChart'
import WordCloudChart from '@components/charts/WordCloudChart'
import WorldMapChart from '@components/charts/WorldMapChart'
import ColoredWordCloudChart from '@components/charts/ColoredWordCloudChart'
import StackedBarChart from '@components/charts/StackedBarChart'
import BarLineChart from '@components/charts/BarLineChart'
import HeatmapChart from '@components/charts/HeatmapChart'
import TopEntitiesBarChart from '@components/charts/TopEntitiesBarChart'
import MultiTopEntitiesBarChart from '@components/charts/MultiTopEntitiesBarChart'

export default {
  name: 'ChartsView',
  components: {
    BaseSpinner,
    MultiLineChart,
    BarChart,
    PieChart,
    LineChart,
    HorizontalBarChart,
    MultiRadarChart,
    RadarChart,
    DoughnutChart,
    WordCloudChart,
    WorldMapChart,
    ColoredWordCloudChart,
    StackedBarChart,
    BarLineChart,
    HeatmapChart,
    TopEntitiesBarChart,
    MultiTopEntitiesBarChart,
  },
  props: {
    labels: {type: Array, default: () => []},
    chartType: {type: String, required: true},
    widgetDetails: {type: Object, required: true},
    chartValues: {type: Array, default: () => []},
    isLegendDisplayed: {type: Boolean, default: true},
    tooltipLabels: {type: [Array, String], required: false},
    isInteractiveDataShown: {type: Boolean, default: true},
    isSentimentChart: {type: Boolean, default: false},
    hasSwithcer: {type: Boolean, default: false},
    switcherValue: {type: String, default: ''},
    projectId: {type: [Number, String], required: false},
    widgetId: {type: [Number, String], required: false},
  },
  data() {
    return {
      interactiveDetails: {},
    }
  },
  computed: {
    ...mapState(['loading', 'widgets', 'inreractiveDataModal']),
    endOfTheDate() {
      return {
        Hour: (date) => {
          date.setMinutes(59, 59)
          return date
        },
        Day: (date) => {
          date.setHours(23, 59, 59)
          return date
        },
        Month: (date) => {
          const currentMonth = date.getMonth()
          date.setMonth(currentMonth + 1, 0)
          date.setHours(23, 59, 59)
          return date
        },
        Year: (date) => {
          date.setMonth(11, 31)
          date.setHours(23, 59, 59)
          return date
        },
      }
    },
  },
  methods: {
    capitalizeFirstLetter,
    ...mapActions([
      action.UPDATE_INTERACTIVE_DATA,
      action.SHOW_INTERACTIVE_DATA_MODAL,
      action.POST_INTERACTIVE_WIDGETS,
    ]),
    showIteractiveModalData(data, dataIndex) {
      const pages = {page_number: 1, posts_per_page: 4}

      if (this.widgetDetails.currentModule === 'Comparison') {
        const comparisonInteractiveData = {
          isShow: true,
          projectId:
            this.projectId ||
            this.widgetDetails?.widgetData[dataIndex].project_id,
          widgetId:
            this.widgetId ||
            this.widgetDetails?.widgetData[dataIndex].widget_id,
        }

        if (this.hasSwithcer) {
          return this[action.SHOW_INTERACTIVE_DATA_MODAL]({
            value: {
              ...comparisonInteractiveData,
              data: {
                ...data,
                second_value: [this.switcherValue],
                ...pages,
              },
            },
            moduleType: capitalizeFirstLetter(this.widgetDetails.module),
          })
        }

        return this[action.SHOW_INTERACTIVE_DATA_MODAL]({
          value: {
            ...comparisonInteractiveData,
            data: {
              ...data,
              ...pages,
            },
          },
          moduleType: capitalizeFirstLetter(this.widgetDetails.module),
        })
      }

      const interactiveData = {
        isShow: true,
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      }

      return this[action.SHOW_INTERACTIVE_DATA_MODAL]({
        value: {
          ...interactiveData,
          data: {
            ...data,
            ...pages,
          },
        },
        moduleType: this.widgetDetails.moduleName,
      })
    },

    openInteractiveData(firstValue, secondValue, dataIndex) {
      let startOfTheDay = new Date(firstValue)
      let optimalPostWidgetData = null
      let aggregationPeriod = this.capitalizeFirstLetter(
        this.widgetDetails.aggregation_period
      )

      if (firstValue.includes('from')) {
        optimalPostWidgetData = firstValue.split(' ').filter((value) => {
          if (+value === 0) return value
          return +value
        })
      }

      if (
        startOfTheDay.toString() !== 'Invalid Date' &&
        !firstValue.includes('from')
      ) {
        if (aggregationPeriod !== 'Hour') {
          startOfTheDay.setHours(0, 0, 0)
        }
        let endOfTheDay = this.endOfTheDate[aggregationPeriod](
          new Date(firstValue)
        )
        const data = {
          data: {
            first_value: Array.isArray(secondValue)
              ? secondValue
              : [secondValue],
            second_value: [],
            dates: [
              startOfTheDay.toLocaleString('sv-SE'),
              endOfTheDay.toLocaleString('sv-SE'),
            ],
          },
          dataIndex,
        }
        this.interactiveDetails = data
        this.showIteractiveModalData(data.data, data.dataIndex)
      } else {
        const data = {
          data: {
            first_value: optimalPostWidgetData || [
              firstValue.replace(/ posts/gi, ''),
            ],
            second_value: [secondValue],
            dates: [],
          },
          dataIndex,
        }
        this.interactiveDetails = data
        this.showIteractiveModalData(data.data, data.dataIndex)
      }
    },
  },
  watch: {
    'inreractiveDataModal.areResultsUpdated'() {
      this.showIteractiveModalData(
        this.interactiveDetails.data,
        this.interactiveDetails.dataIndex
      )

      this[action.UPDATE_INTERACTIVE_DATA](false)
    },
  },
}
</script>

<style lang="scss" scoped>
.spinner {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;

  width: 100%;
  height: 100%;
}
</style>
