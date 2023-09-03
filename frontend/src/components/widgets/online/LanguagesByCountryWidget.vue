<template>
  <TopEntitiesStackedBarWidget
    v-if="!isAllFieldsEmpty(languagesByCountry)"
    :chart-values="widgetData.chartValues"
    :labels="widgetData.labels"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'
import {PREDEFINED_COLORS} from '@/lib/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import TopEntitiesStackedBarWidget from '@/components/widgets/TopEntitiesStackedBarWidget'

export default {
  name: 'LanguagesByCountryWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapState(['languagesByCountry']),
    widgetData() {
      const labels = Object.keys(this.languagesByCountry)
      const values = labels.map((label) => this.languagesByCountry[label])
      const chartValues = values.map((chartValue) => {
        const sumValues = chartValue.reduce((currSum, currValue) => {
          return currSum + Object.values(currValue)[1]
        }, 0)

        return chartValue.map((element, index) => {
          const elValues = Object.values(element)
          return {
            data: [(elValues[1] / sumValues) * 100],
            backgroundColor: PREDEFINED_COLORS[index],
            borderRadius: 12,
            barThickness: 'flex',
            label: elValues[0],
          }
        })
      })

      return {
        labels,
        chartValues,
      }
    },
  },
  created() {
    // if (isAllFieldsEmpty(this.languagesByCountry)) {
    this[action.GET_LANGUAGES_BY_COUNTRY]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
    // }
  },
  methods: {
    ...mapActions([action.GET_LANGUAGES_BY_COUNTRY]),
    isAllFieldsEmpty,
  },
}
</script>
