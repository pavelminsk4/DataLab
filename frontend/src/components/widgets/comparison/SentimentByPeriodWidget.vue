<template>
  <WidgetContainerWithSwitcher :tabs="tabs" @switch-tab="switchTab">
    <ContentVolumeWidget
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :content-volume-widget-data="widgetData"
      :colors="colors"
      :has-swithcer="true"
      :switcher-value="activeTab"
      :custom-labels="customLabels"
      :custom-values="customValues"
    />
  </WidgetContainerWithSwitcher>
</template>

<script>
import moment from 'moment'
import {COMPARISON_COLORS, SENTIMENT} from '@lib/constants'
import {defaultDate} from '@lib/utilities'

import WidgetContainerWithSwitcher from '@components/widgets/WidgetContainerWithSwitcher'
import ContentVolumeWidget from '@components/widgets/ContentVolumeWidget'

export default {
  name: 'ComparisonSentimentByPeriodWidget',
  components: {ContentVolumeWidget, WidgetContainerWithSwitcher},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      activeTab: SENTIMENT.NEUTRAL,
    }
  },
  computed: {
    tabs() {
      return [SENTIMENT.NEUTRAL, SENTIMENT.POSITIVE, SENTIMENT.NEGATIVE]
    },
    customLabels() {
      const dates = []
      this.widgetDetails.widgetData.map((project) => {
        project.data.map((data) => dates.push(Object.keys(data)[0]))
      })

      const sortedDates = dates.sort((a, b) => {
        return moment(a).diff(b)
      })

      return [...new Set(sortedDates)].map((date) =>
        this.defaultDate(date, this.platformLanguage)
      )
    },
    widgetData() {
      const formattedWidgetData = []
      this.widgetDetails.widgetData.map((project) => {
        const value = {}
        value[project.project] = project.data.map((el) => {
          const date = Object.keys(el)[0]
          return {
            date: date,
            post_count: el[date][this.activeTab],
          }
        })

        formattedWidgetData.push(value)
      })
      return formattedWidgetData
    },
    customValues() {
      const values = []
      const defaultLineColors = [
        '#7C59ED',
        '#CDC6FF',
        '#551EB9',
        '#6AC7F0',
        '#00CC87',
        '#FD7271',
        '#FFBB01',
        '#7ACCB0',
        '#01A4EE',
        '#FFE499',
      ]

      const lineColors = this.colors.length ? this.colors : defaultLineColors

      this.widgetData.forEach((volumeData, index) => {
        values.push({
          label: Object.keys(volumeData)[0],
          color: lineColors[index],
          data: this.customLabels.reduce((totalData, amount) => {
            const currentValues = volumeData[Object.keys(volumeData)]
            const isThereDate = currentValues.some(
              (date) =>
                this.defaultDate(date.date, this.platformLanguage) === amount
            )

            if (isThereDate) {
              const index = currentValues.findIndex(
                (value) =>
                  this.defaultDate(value.date, this.platformLanguage) === amount
              )
              totalData.push(currentValues[index].post_count)
            } else {
              totalData.push(0)
            }
            return totalData
          }, []),
        })
      })

      return values
    },
    colors() {
      return COMPARISON_COLORS
    },
  },
  methods: {
    defaultDate,
    switchTab(tab) {
      this.activeTab = tab
    },
  },
}
</script>
