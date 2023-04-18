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
    authorsByLanguage() {
      return this.socialWidgets.authorsByLanguage
    },
    labels() {
      return this.authorsByLanguage.map((el) => el.language)
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.authorsByLanguage.map((el) => el.user_count),
        },
      ]
    },
  },
  created() {
    if (!this.authorsByLanguage.length) {
      this[action.GET_AUTHORS_BY_LANGUAGE]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_LANGUAGE]),
  },
}
</script>
