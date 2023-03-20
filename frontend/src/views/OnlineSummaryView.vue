<template>
  <SummaryScreen
    v-if="selectedWidgets"
    :number-of-posts="numberOfPosts"
    :selected-widgets="selectedWidgets"
    :current-project="currentProject"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SummaryScreen from '@/components/project/screens/SummaryScreen.vue'

import {snakeToPascal} from '@lib/utilities'
import {modalWidgetsConfig} from '@/lib/configs/widgetsConfigs'

export default {
  components: {SummaryScreen},
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  data() {
    return {
      summaryWidgets: [
        'summary_widget',
        'content_volume_top_5_source_widget',
        'sentiment_for_period_widget',
        'volume_widget',
        'top_10_countries_widget',
        'top_10_authors_by_volume_widget',
        'top_keywords',
      ],
    }
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      numberOfPosts: get.POSTS_NUMBER,
    }),
    selectedWidgets() {
      if (!this.availableWidgets) return
      return this.summaryWidgets.map((widgetName) => {
        return {
          static: false,
          name: widgetName,
          widgetName: snakeToPascal(widgetName),
          isShow: this.availableWidgets[widgetName]?.is_active,
          isWidget: true,
          widgetId: this.availableWidgets[widgetName]?.id,
          actionName: modalWidgetsConfig[widgetName].actionName,
          isChartShow: modalWidgetsConfig[widgetName].isChartShow,
          title: this.availableWidgets[widgetName]?.title,
          chartType:
            this.availableWidgets[widgetName]?.chart_type ||
            modalWidgetsConfig[widgetName]?.defaultChartType,
          hasAggregationPeriod:
            modalWidgetsConfig[widgetName].hasAggregationPeriod,
        }
      })
    },
  },
  async created() {
    if (!this.availableWidgets) {
      await this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)
    }
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
  },
}
</script>
