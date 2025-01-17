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
import {action, get} from '@store/constants'
import {PREDEFINED_COLORS} from '@lib/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

import TopEntitiesStackedBarWidget from '@components/widgets/TopEntitiesStackedBarWidget'

export default {
  name: 'LanguagesByLocationWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    languagesByLocation() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.languagesByLocation.data
      )
    },
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
            data: [Number(((elValues[1] / sumValues) * 100).toFixed(2))],
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
    widgetId() {
      return this.socialWidgets.languagesByLocation?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.languagesByLocation) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
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
