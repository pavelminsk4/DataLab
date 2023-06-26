<template>
  <TopEntitiesStackedBarWidget
    v-if="!isAllFieldsEmpty(languagesByLocation)"
    :chart-values="widgetData.chartValues"
    :labels="widgetData.labels"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {PREDEFINED_COLORS} from '@/lib/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

const {mapActions, mapState} = createNamespacedHelpers('social/widgets')

import TopEntitiesStackedBarWidget from '@/components/widgets/TopEntitiesStackedBarWidget'

export default {
  name: 'LanguagesByLocationWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapState(['languagesByLocation']),
    widgetData() {
      const labels = Object.keys(this.languagesByLocation)
      const values = labels.map((label) => this.languagesByLocation[label])
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
    if (isAllFieldsEmpty(this.languagesByLocation.length)) {
      this[action.GET_LANGUAGES_BY_LOCATION]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_LANGUAGES_BY_LOCATION]),
    isAllFieldsEmpty,
  },
}
</script>
