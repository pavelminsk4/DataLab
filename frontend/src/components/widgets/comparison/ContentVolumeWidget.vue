<template>
  <ContentVolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :content-volume-widget-data="widgetData"
    :colors="colors"
    :custom-labels="customLabels"
    :custom-values="customValues"
  />
</template>

<script>
import moment from 'moment'

import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'
import {COMPARISON_COLORS} from '@lib/constants'

export default {
  name: 'ComparisonContentVolumeWidget',
  components: {ContentVolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    widgetData() {
      const formattedWidgetData = []
      this.widgetDetails.widgetData.map((project) => {
        const value = {}
        value[project.project] = project.data.map((item) => {
          return {
            date: item.date,
            post_count: item.created_count,
          }
        })
        formattedWidgetData.push(value)
      })

      return formattedWidgetData
    },
    customLabels() {
      const dates = []
      this.widgetDetails.widgetData.map((project) => {
        project.data.map((data) => dates.push(data.date))
      })

      const sortedDates = dates.sort((a, b) => {
        return moment(a).diff(b)
      })

      return [...new Set(sortedDates)].map((date) => date)
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
  },
  created() {
    this.colors = COMPARISON_COLORS
  },
}
</script>
