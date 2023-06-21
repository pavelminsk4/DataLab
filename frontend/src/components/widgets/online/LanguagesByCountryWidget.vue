<template>
  <TopEntitiesStackedBarWidget
    :widgetData="widgetData"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'
import {PREDEFINED_COLORS} from '@/lib/constants'

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
      const chartValues = values.map((el) => {
        const max = el.reduce((a, b) => {
          return a + b[1]
        }, 0)

        return el.map((el, index) => {
          return {
            data: [(el[1] / max) * 100],
            backgroundColor: PREDEFINED_COLORS[index],
            borderRadius: 12,
            barThickness: 'flex',
            tooltip: el[0],
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
    if (!this.languagesByCountry.length) {
      this[action.GET_LANGUAGES_BY_COUNTRY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_LANGUAGES_BY_COUNTRY]),
  },
}
</script>
