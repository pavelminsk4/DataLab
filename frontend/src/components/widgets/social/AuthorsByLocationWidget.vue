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
  name: 'AuthorsByLocationWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    authorsByLocation() {
      return this.socialWidgets.authorsByLocation
    },
    labels() {
      return this.authorsByLocation.map((el) => el.locationString)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.authorsByLocation.map((el) => el.user_count),
        },
      ]
    },
  },
  created() {
    if (!this.authorsByLocation.length) {
      this[action.GET_AUTHORS_BY_LOCATION]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_LOCATION]),
    openInteractiveModal(val) {
      this.$emit('open-interactive-data', val, this.widgetDetails.id, 'author')
    },
  },
}
</script>
