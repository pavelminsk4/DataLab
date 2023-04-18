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
  name: 'AuthorsByLanguageWidget',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    authorsByGender() {
      return this.socialWidgets.authorsByGender
    },
    labels() {
      return Object.keys(this.authorsByGender)
    },
    chartValues() {
      return [
        {
          colors: ['#EBEBF0', '#FD7271', '#516BEE'],
          data: Object.keys(this.authorsByGender).map(
            (key) => this.authorsByGender[key]
          ),
        },
      ]
    },
  },
  created() {
    if (!this.authorsByGender.length) {
      this[action.GET_AUTHORS_BY_GENDER]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_GENDER]),
  },
}
</script>
