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
  name: 'SocialTopAuthorsWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topAuthors() {
      return this.widgetDetails.widgetData || this.socialWidgets.topAuthors.data
    },
    labels() {
      return this.topAuthors.map((el) => el.user_name)
    },
    chartValues() {
      return [
        {
          data: this.topAuthors.map((el) => el.user_count),
        },
      ]
    },
    widgetId() {
      return this.socialWidgets.topAuthors?.id
    },
  },
  created() {
    const hasCurrentData =
      this.topAuthors.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_TOP_AUTHORS_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
  },
}
</script>
