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

const {mapGetters, mapActions} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

import VolumeWidget from '@/components/widgets/VolumeWidget'
export default {
  name: 'MostFrequentPostTypes',
  mixins: [translate],
  components: {VolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      widgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mostFrequentPostTypes() {
      return this.widgets.mostFrequentPostTypes
    },
    labels() {
      return Object.keys(this.mostFrequentPostTypes).map((label) =>
        this.translatedText(label.split('_')[1])
      )
    },
    chartValues() {
      return [
        {
          data: Object.values(this.mostFrequentPostTypes),
        },
      ]
    },
  },
  created() {
    if (isAllFieldsEmpty(this.mostFrequentPostTypes)) {
      this[action.GET_MOST_FREQUENT_POST_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_FREQUENT_POST_TYPES]),
    isAllFieldsEmpty,
  },
}
</script>
