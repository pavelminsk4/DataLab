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
import {isAllFieldsEmpty} from '@/lib/utilities'
import translate from '@/lib/mixins/translate.js'

import VolumeWidget from '@/components/widgets/VolumeWidget'

const {mapGetters, mapActions} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'MostFrequentMediaTypes',
  mixins: [translate],
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      widgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mostFrequentMediaTypes() {
      return this.widgets.mostFrequentMediaTypes
    },
    labels() {
      return Object.keys(this.mostFrequentMediaTypes).map((label) =>
        this.translatedText(label.split('_')[1])
      )
    },
    chartValues() {
      return [
        {
          data: Object.values(this.mostFrequentMediaTypes),
        },
      ]
    },
  },
  created() {
    if (isAllFieldsEmpty(this.mostFrequentMediaTypes)) {
      this[action.GET_MOST_FREQUENT_MEDIA_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_FREQUENT_MEDIA_TYPES]),
    isAllFieldsEmpty,
  },
}
</script>
