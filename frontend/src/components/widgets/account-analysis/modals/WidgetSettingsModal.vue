<template>
  <BaseModal
    :title="widgetDetails.title"
    :is-general-padding="false"
    style="--base-modal-content-padding: 0px"
  >
    <WidgetSettingsScreen
      :widget-details="widgetDetails"
      @save-general-settings="saveGeneralChanges"
      @save-dimensions-settings="saveDimensionsForWidget"
      @update-chart-type="($event) => (newChartType = $event)"
      @change-aggregation-period="changeAggregationPeriod"
      @save-chart-settings="saveChartType"
    >
      <AccountAnalysisMainWidget
        :widgetDetails="widgetDetails"
        :is-settings="true"
        :new-chart-type="newChartType"
        class="widget-view"
      />
    </WidgetSettingsScreen>
  </BaseModal>
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import WidgetSettingsScreen from '@/components/widgets/screens/WidgetSettingsScreen'
import BaseModal from '@/components/modals/BaseModal'
import AccountAnalysisMainWidget from '@/components/widgets/account-analysis/AccountAnalysisMainWidget'

const {mapActions} = createNamespacedHelpers('accountAnalysis')

const {mapActions: mapAccountAnalysisWidgetsActions} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'AccountAnalysisWidgetSettingsModal',
  components: {
    WidgetSettingsScreen,
    BaseModal,
    AccountAnalysisMainWidget,
  },
  emits: ['open-interactive-widget', 'open-sentiment-interactive'],
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      newChartType: '',
    }
  },
  computed: {
    ...mapGetters({
      selectedDimensions: get.SELECTED_DIMENSIONS,
    }),
    widgetName() {
      return this.widgetDetails.name
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.POST_DIMENSIONS_FOR_WIDGET,
    ]),
    ...mapAccountAnalysisWidgetsActions([
      action.GET_PROFILE_TIMELINE,
      action.GET_SUMMARY,
      action.GET_MOST_FREQUENT_POST_TYPES,
      action.GET_MOST_FREQUENT_MEDIA_TYPES,
      action.GET_MOST_ENGAGING_POST_TYPES,
      action.GET_MOST_ENGAGING_MEDIA_TYPES,
      action.GET_FOLLOWER_GROWTH,
      action.GET_OPTIMAL_POST_LENGTH,
    ]),

    async saveGeneralChanges(newSettings) {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.widgetDetails.projectId,
        widgetsList: {
          [this.widgetName]: {
            id: this.widgetDetails.id,
            title: newSettings.newWidgetTitle || this.widgetDetails.title,
            description: newSettings.newWidgetDescription,
            aggregation_period:
              newSettings.newAggregationPeriod ||
              this.widgetDetails.aggregation_period,
          },
        },
      })

      this.updateCurrentWidget(newSettings)
    },

    async saveDimensionsForWidget() {
      await this[action.POST_DIMENSIONS_FOR_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        data: {
          aggregation_period: this.widgetDetails.aggregation_period,
          author_dim_pivot: this.selectedDimensions.authors,
          language_dim_pivot: this.selectedDimensions.languages,
          country_dim_pivot: this.selectedDimensions.countries,
          sentiment_dim_pivot: this.selectedDimensions.sentiments,
          source_dim_pivot: this.selectedDimensions.sources,
        },
      })

      await this[this.widgetDetails.actionName]({
        projectId: this.widgetDetails.projectId,
        value: {
          aggregation_period: this.widgetDetails.aggregation_period,
          author_dim_pivot: this.widgetDetails.author_dim_pivot || null,
          language_dim_pivot: this.widgetDetails.language_dim_pivot || null,
          country_dim_pivot: this.widgetDetails.country_dim_pivot || null,
          sentiment_dim_pivot: this.widgetDetails.sentiment_dim_pivot || null,
          source_dim_pivot: this.widgetDetails.source_dim_pivot || null,
        },
        widgetId: this.widgetDetails.id,
      })
    },

    async saveChartType() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.widgetDetails.projectId,
        widgetsList: {
          [this.widgetName]: {
            id: this.widgetDetails.id,
            chart_type: this.newChartType,
          },
        },
      })
    },

    updateCurrentWidget(newSettings) {
      this[this.widgetDetails.actionName]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: {
          author_dim_pivot: this.widgetDetails.author_dim_pivot || null,
          language_dim_pivot: this.widgetDetails.language_dim_pivot || null,
          country_dim_pivot: this.widgetDetails.country_dim_pivot || null,
          sentiment_dim_pivot: this.widgetDetails.sentiment_dim_pivot || null,
          source_dim_pivot: this.widgetDetails.source_dim_pivot || null,
          aggregation_period:
            newSettings?.newAggregationPeriod ||
            this.widgetDetails.aggregation_period,
        },
      })
    },

    async changeAggregationPeriod(aggregationPeriod) {
      await this[this.widgetDetails.actionName]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: {
          aggregation_period: aggregationPeriod,
        },
      })
    },
  },
}
</script>
