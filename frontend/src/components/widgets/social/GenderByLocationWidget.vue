<template>
  <VolumeWidget
    v-bind="$attrs"
    v-if="chartValues.length"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
    :is-display-legend="true"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'GenderByLocation',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    genderByLocation() {
      return this.socialWidgets.genderByLocation
    },
    labels() {
      return Object.keys(this.genderByLocation)
    },
    currentWidgetData() {
      return Object.values(this.genderByLocation)
    },

    chartValues() {
      if (!this.currentWidgetData) return []

      let female = []
      let male = []
      let unidentified = []

      this.currentWidgetData.forEach((el) => {
        female.push(el.female)
        male.push(el.male)
        unidentified.push(el.female)
      })

      return [
        {
          label: 'Male',
          color: '#516BEE',
          data: female,
        },
        {
          label: 'Female',
          color: '#FD7271',
          data: male,
        },
        {
          label: 'Undefined',
          color: '#B0B5B8',
          data: unidentified,
        },
      ]
    },
  },
  created() {
    if (!this.genderByLocation.length) {
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
