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

import VolumeWidget from '@/components/widgets/VolumeWidget'

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
      return this.socialWidgets.topLocations
    },
    labels() {
      return this.topLocations.map((el) => el.locationString)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.topLocations.map((el) => el.locations_count),
        },
      ]
    },
  },
  created() {
    if (!this.topLocations.length) {
      this[action.GET_TOP_LOCATIONS_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_LOCATIONS_WIDGET]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetDetails.id, 'author')
    },
  },
}
</script>
