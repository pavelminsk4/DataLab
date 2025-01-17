<template>
  <VolumeWidget
    v-bind="$attrs"
    v-if="chartValues.length"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
    :is-legend-displayed="true"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'
import translate from '@lib/mixins/translate.js'

import VolumeWidget from '@components/widgets/VolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'GenderByLocation',
  components: {VolumeWidget},
  mixins: [translate],
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    genderByLocation() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.genderByLocation.data
      )
    },
    labels() {
      return Object.keys(this.genderByLocation)
    },
    currentWidgetData() {
      return Object.values(this.genderByLocation)
    },

    chartValues() {
      if (!this.currentWidgetData) return []

      let femalesData = []
      let malesData = []

      this.currentWidgetData.forEach((el) => {
        femalesData.push(el.female)
        malesData.push(el.male)
      })

      return [
        {
          label: this.translatedText('Male'),
          color: '#516BEE',
          data: malesData,
        },
        {
          label: this.translatedText('Female'),
          color: '#FD7271',
          data: femalesData,
        },
      ]
    },
    widgetId() {
      return this.socialWidgets.genderByLocation?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.genderByLocation) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_GENDER_BY_LOCATION]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: {
          author_dim_pivot: this.widgetDetails.author_dim_pivot || null,
          language_dim_pivot: this.widgetDetails.language_dim_pivot || null,
          country_dim_pivot: this.widgetDetails.country_dim_pivot || null,
          sentiment_dim_pivot: this.widgetDetails.sentiment_dim_pivot || null,
          source_dim_pivot: this.widgetDetails.source_dim_pivot || null,
          aggregation_period: this.widgetDetails.aggregation_period,
        },
      })
    }
  },
  methods: {
    ...mapActions([action.GET_GENDER_BY_LOCATION]),
  },
}
</script>
