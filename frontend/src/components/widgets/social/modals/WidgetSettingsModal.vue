<template>
  <BaseModal
    :title="widgetData.title"
    :is-general-padding="false"
    style="--base-modal-content-padding: 0px"
  >
    <WidgetSettingsScreen
      :widget-data="widgetData"
      :widget-name="widgetModalData.widgetName"
      :settings-tabs="widgetModalData.settingsTabs"
      :chart-type="widgetModalData.chartType"
      :project-id="projectId"
      @save-general-settings="saveGeneralChanges"
      @update-chart-type="($event) => (newChartType = $event)"
      @save-chart-settings="saveChartType"
    >
      {{ newChartType }}
      <component
        :is="snakeToPascal(widgetName)"
        :volume="widgetData"
        :chart-type="newChartType || widgetModalData.chartType"
        :is-widget="false"
        :is-open-widget="true"
        :project-id="projectId"
        :widget-id="widgetData.id"
        :title="widgetData.title"
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
import BaseModal from '@/components/modals/BaseModal'

import SummaryWidget from '@/components/widgets/online/SummaryWidget'
import VolumeWidget from '@/components/widgets/online/VolumeWidget'
import Top10BrandsWidget from '@/components/widgets/online/Top10BrandsWidget'
import Top10CountriesWidget from '@/components/widgets/online/Top10CountriesWidget'
import Top10LanguagesWidget from '@/components/widgets/online/Top10LanguagesWidget'
import Top10AuthorsByVolumeWidget from '@/components/widgets/online/Top10AuthorsByVolumeWidget'
import SentimentForPeriodWidget from '@/components/widgets/online/SentimentForPeriodWidget'
import ClippingFeedContentWidget from '@/components/widgets/social/ClippingFeedContentWidget'
import SentimentTop10AuthorsWidget from '@/components/widgets/online/SentimentTop10AuthorsWidget'
import SentimentTop10SourcesWidget from '@/components/widgets/online/SentimentTop10SourcesWidget'
import SentimentTop10LanguagesWidget from '@/components/widgets/online/SentimentTop10LanguagesWidget'
import SentimentTop10CountriesWidget from '@/components/widgets/online/SentimentTop10CountriesWidget'
import ContentVolumeTop5SourceWidget from '@/components/widgets/online/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/widgets/online/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/widgets/online/ContentVolumeTop5CountriesWidget'

export default {
  name: 'OnlineWidgetSettingsModal',
  components: {
    WidgetSettingsScreen,
    BaseModal,
    VolumeWidget,
    Top10LanguagesWidget,
    Top10BrandsWidget,
    Top10CountriesWidget,
    Top10AuthorsByVolumeWidget,
    ContentVolumeTop5SourceWidget,
    ContentVolumeTop5AuthorsWidget,
    ContentVolumeTop5CountriesWidget,
    SentimentTop10SourcesWidget,
    SentimentTop10CountriesWidget,
    SentimentTop10AuthorsWidget,
    SentimentForPeriodWidget,
    SentimentTop10LanguagesWidget,
    ClippingFeedContentWidget,
    SummaryWidget,
  },
  props: {
    widgetData: {type: Object, required: true},
    widgetModalData: {type: Object, required: true},
    projectId: {type: Number, required: true},
    currentProject: {type: [Array, Object], required: false},
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
      return this.widgetModalData.widgetName
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
        projectId: this.projectId,
        widgetsList: {
          [this.widgetName]: {
            id: this.widgetData.id,
            title: newSettings.newWidgetTitle || this.widgetData.title,
            description: newSettings.newWidgetDescription,
            aggregation_period: this.widgetData.aggregation_period,
          },
        },
      })
    },

    async saveDimensionsForWidget() {
      await this[action.POST_DIMENSIONS_FOR_WIDGET]({
        projectId: this.projectId,
        widgetId: this.widgetData.id,
        data: {
          smpl_freq: this.widgetData.aggregation_period,
          author_dim_pivot: this.selectedDimensions.authors,
          language_dim_pivot: this.selectedDimensions.languages,
          country_dim_pivot: this.selectedDimensions.countries,
          sentiment_dim_pivot: this.selectedDimensions.sentiments,
          source_dim_pivot: this.selectedDimensions.sources,
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)

      await this[this.widgetModalData.actionName]({
        projectId: this.projectId,
        value: {
          smpl_freq: 'day',
          author_dim_pivot: this.widgetData.author_dim_pivot || null,
          language_dim_pivot: this.widgetData.language_dim_pivot || null,
          country_dim_pivot: this.widgetData.country_dim_pivot || null,
          sentiment_dim_pivot: this.widgetData.sentiment_dim_pivot || null,
          source_dim_pivot: this.widgetData.source_dim_pivot || null,
        },
        widgetId: this.widgetData.id,
      })
    },

    async saveChartType() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        widgetsList: {
          [this.widgetName]: {
            id: this.widgetData.id,
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
