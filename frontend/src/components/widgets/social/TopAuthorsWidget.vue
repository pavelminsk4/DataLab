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
      return this.socialWidgets.topAuthors
    },
    labels() {
      return this.topAuthors.map((el) => el.user_name)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.topAuthors.map((el) => el.user_count),
        },
      ]
    },
  },
  created() {
    if (!this.topAuthors.length) {
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
