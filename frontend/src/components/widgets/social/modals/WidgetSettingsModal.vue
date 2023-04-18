<template>
  <BaseModal
    :title="widgetDetails.title"
    :is-general-padding="false"
    style="--base-modal-content-padding: 0px"
  >
    <WidgetSettingsScreen
      :widget-details="widgetDetails"
      @save-dimensions-settings="saveDimensionsChanges"
      @change-aggregation-period="changeAggregationPeriod"
      @save-general-settings="saveGeneralChanges"
      @update-chart-type="($event) => (newChartType = $event)"
      @save-chart-settings="saveChartType"
    >
      <SocialMainWidget
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
import SocialMainWidget from '@/components/widgets/social/SocialMainWidget'

const {mapActions} = createNamespacedHelpers('social')

const {mapActions: mapSocialWidgetsActions} =
  createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialWidgetSettingsModal',
  components: {
    WidgetSettingsScreen,
    BaseModal,
    SocialMainWidget,
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
    ...mapSocialWidgetsActions([
      action.GET_SUMMARY_WIDGET,
      action.GET_TOP_AUTHORS_WIDGET,
      action.GET_TOP_LOCATIONS_WIDGET,
      action.GET_TOP_LANGUAGES_WIDGET,
      action.GET_CONTENT_VOLUME_WIDGET,
      action.GET_CONTENT_VOLUME_TOP_AUTHORS,
      action.GET_CONTENT_VOLUME_TOP_LANGUAGES,
      action.GET_CONTENT_VOLUME_TOP_LOCATIONS,
      action.GET_SENTIMENT_FOR_PERIOD,
      action.GET_GENDER_VOLUME_WIDGET,
      action.GET_SENTIMENT_BY_GENDER,
      action.GET_SENTIMENT_TOP_AUTHORS,
      action.GET_SENTIMENT_TOP_LOCATIONS,
      action.GET_SENTIMENT_TOP_LANGUAGES,
      action.GET_TOP_KEYWORDS_WIDGET,
      action.GET_SENTIMENT_DIAGRAM,
      action.GET_TOP_SHARING_SOURCES,
      action.GET_OVERALL_TOP_AUTHORS,
      action.GET_TOP_AUTHORS_BY_GENDER,
      action.GET_SENTIMENT_NUMBER_OF_RESULT,
      action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET,
      action.GET_AUTHORS_BY_LANGUAGE,
      action.GET_AUTHORS_BY_LOCATION,
      action.GET_AUTHORS_BY_SENTIMENT,
      action.GET_AUTHORS_BY_GENDER,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
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
