<template>
  <BaseModal
    :title="widgetDetails.title"
    :is-general-padding="false"
    style="--base-modal-content-padding: 0px"
  >
    <WidgetSettingsScreen
      :widget-details="widgetDetails"
      @save-general-settings="saveGeneralChanges"
      @update-chart-type="($event) => (newChartType = $event)"
      @save-chart-settings="saveChartType"
    >
      <MainWidget
        :widgetDetails="widgetDetails"
        :is-settings="true"
        :new-chart-type="newChartType"
        class="widget-view"
        @open-interactive-data="openInteractiveData"
        @open-sentiment-interactive="openSentimentInteractiveData"
      />
    </WidgetSettingsScreen>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {snakeToPascal} from '@/lib/utilities'

import WidgetSettingsScreen from '@/components/widgets/screens/WidgetSettingsScreen'
import MainWidget from '@/components/widgets/online/MainWidget'
import BaseModal from '@/components/modals/BaseModal'

export default {
  name: 'OnlineWidgetSettingsModal',
  components: {
    WidgetSettingsScreen,
    BaseModal,
    MainWidget,
  },
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
      action.GET_AVAILABLE_WIDGETS,
      action.GET_SENTIMENT_FOR_PERIOD,
      action.GET_CONTENT_VOLUME_TOP_AUTHORS,
      action.GET_CONTENT_VOLUME_TOP_COUNTRIES,
      action.GET_CONTENT_VOLUME_TOP_SOURCES,
      action.GET_SELECTED_DIMENSIONS,
      action.POST_DIMENSIONS_FOR_WIDGET,
    ]),
    snakeToPascal,

    saveGeneralChanges(newSettings) {
      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.widgetDetails.projectId,
        widgetsList: {
          [this.widgetName]: {
            id: this.widgetDetails.id,
            title: newSettings.newWidgetTitle || this.widgetDetails.title,
            description: newSettings.newWidgetDescription,
            aggregation_period: this.widgetDetails.aggregation_period,
          },
        },
      })
    },

    async saveDimensionsForWidget() {
      await this[action.POST_DIMENSIONS_FOR_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        data: {
          smpl_freq: this.widgetDetails.aggregation_period,
          author_dim_pivot: this.selectedDimensions.authors,
          language_dim_pivot: this.selectedDimensions.languages,
          country_dim_pivot: this.selectedDimensions.countries,
          sentiment_dim_pivot: this.selectedDimensions.sentiments,
          source_dim_pivot: this.selectedDimensions.sources,
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.widgetDetails.projectId)

      await this[this.widgetDetails.actionName]({
        projectId: this.widgetDetails.projectId,
        value: {
          smpl_freq: 'day',
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

    openInteractiveData(val, widgetId, fieldName) {
      this.$emit('open-interactive-widget', val, widgetId, fieldName)
    },
    openSentimentInteractiveData(source, sentiment, widgetId) {
      this.$emit('open-sentiment-interactive', source, sentiment, widgetId)
    },
  },
}
</script>
