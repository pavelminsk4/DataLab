<template>
  <VolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import VolumeWidget from '@components/widgets/VolumeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialTopLocationsWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topLocations() {
      return (
        this.widgetDetails.widgetData || this.socialWidgets?.topLocations.data
      )
    },
    labels() {
      return this.topLocations.map((el) => el.locationString)
    },
    chartValues() {
      return [
        {
          data: this.topLocations.map((el) => el.locations_count),
        },
      ]
    },
    widgetId() {
      return this.socialWidgets?.topLocations?.id
    },
  },
  created() {
    const hasCurrentData =
      this.topLocations.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_TOP_LOCATIONS_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_LOCATIONS_WIDGET]),
  },
}
</script>
