<template>
  <BaseModal
    :title="`${widgetDetails.title} Settings`"
    :is-general-padding="false"
    style="--base-modal-content-padding: 0px"
    @close="closeSettingsModal"
  >
    <WidgetSettingsScreen
      :widget-details="widgetDetails"
      @save-general-settings="saveGeneralChanges"
      @save-filters-settings="saveFiltersChanges"
      @update-chart-type="($event) => (newChartType = $event)"
      @change-aggregation-period="changeAggregationPeriod"
      @save-chart-settings="saveChartType"
    >
      <OnlineMainWidget
        :widgetDetails="widgetDetails"
        :is-settings="true"
        :new-chart-type="newChartType"
        class="widget-view"
      />
    </WidgetSettingsScreen>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetSettingsScreen from '@/components/widgets/screens/WidgetSettingsScreen'
import OnlineMainWidget from '@/components/widgets/online/OnlineMainWidget'
import BaseModal from '@/components/modals/BaseModal'

export default {
  name: 'OnlineWidgetSettingsModal',
  components: {
    WidgetSettingsScreen,
    BaseModal,
    OnlineMainWidget,
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
      selectedFilters: get.SELECTED_FILTERS,
    }),
    widgetName() {
      return this.widgetDetails.name
    },
  },
  methods: {
    ...mapActions([
      action.GET_VOLUME_WIDGET,
      action.GET_SUMMARY_WIDGET,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
      action.GET_TOP_AUTHORS_WIDGET,
      action.GET_TOP_BRANDS_WIDGET,
      action.GET_TOP_COUNTRIES_WIDGET,
      action.GET_TOP_LANGUAGES_WIDGET,
      action.GET_SENTIMENT_TOP_SOURCES,
      action.GET_SENTIMENT_TOP_COUNTRIES,
      action.GET_SENTIMENT_TOP_AUTHORS,
      action.GET_SENTIMENT_TOP_LANGUAGES,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_SENTIMENT_FOR_PERIOD,
      action.GET_CONTENT_VOLUME_TOP_AUTHORS,
      action.GET_CONTENT_VOLUME_TOP_COUNTRIES,
      action.GET_CONTENT_VOLUME_TOP_SOURCES,
      action.GET_SELECTED_FILTERS,
      action.GET_TOP_KEYWORDS_WIDGET,
      action.GET_SENTIMENT_TOP_KEYWORDS,
      action.GET_AUTHORS_BY_COUNTRY,
      action.GET_SENTIMENT_DIAGRAM,
      action.GET_SENTIMENT_NUMBER_OF_RESULT,
      action.GET_OVERALL_TOP_SOURCES,
      action.GET_SOURCES_BY_COUNTRY,
      action.GET_TOP_SHARING_SOURCES,
      action.GET_SOURCES_BY_LANGUAGE,
      action.GET_OVERALL_TOP_AUTHORS,
      action.GET_AUTHORS_BY_LANGUAGE,
      action.GET_AUTHORS_BY_SENTIMENT,
      action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET,
      action.POST_FILTERS_FOR_WIDGET,
    ]),

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

    async saveFiltersChanges() {
      await this[action.POST_FILTERS_FOR_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        data: {
          aggregation_period: this.widgetDetails.aggregation_period,
          author_dim_pivot: this.selectedFilters.authors,
          language_dim_pivot: this.selectedFilters.languages,
          country_dim_pivot: this.selectedFilters.countries,
          sentiment_dim_pivot: this.selectedFilters.sentiments,
          source_dim_pivot: this.selectedFilters.sources,
        },
      })

      this.updateCurrentWidget()
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

    async changeAggregationPeriod(aggregationPeriod) {
      await this[this.widgetDetails.actionName]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: {
          aggregation_period: aggregationPeriod,
        },
      })
    },

    closeSettingsModal() {
      this[this.widgetDetails.actionName]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: {
          aggregation_period: this.widgetDetails.aggregation_period,
        },
      })

      this.$emit('close')
    },
  },
}
</script>

<style>
.widget-view {
  flex: 1;
  display: flex;
  flex-direction: column;

  height: 100%;
  width: 450px;

  background-color: var(--background-secondary-color);
}
</style>
