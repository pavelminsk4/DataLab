<template>
  <VolumeWidget
    v-if="!isAllFieldsEmpty(mostFrequentMentionMediaTypes)"
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
import {isAllFieldsEmpty} from '@/lib/utilities'

const {mapGetters, mapActions} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'mostFrequentMentionMediaTypes',
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      widgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mostFrequentMentionMediaTypes() {
      return this.widgets.mostFrequentMentionMediaTypes
    },
    labels() {
      return Object.keys(this.mostFrequentMentionMediaTypes).map(
        (label) => label.split('_')[1]
      )
    },
    chartValues() {
      return [
        {
          data: Object.values(this.mostFrequentMentionMediaTypes),
        },
      ]
    },
  },
  created() {
    if (isAllFieldsEmpty(this.mostFrequentMentionMediaTypes)) {
      this[action.GET_MOST_FREQUENT_MENTION_MEDIA_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_FREQUENT_MENTION_MEDIA_TYPES]),
    isAllFieldsEmpty,
  },
}
</script>
