<template>
  <BaseModal
    modal-frame-style="width: 75vw; height: 90vh;"
    :title="generalWidgetData.title"
    :is-general-padding="false"
    style="--base-modal-content-padding: 0px"
  >
    <div class="settings-wrapper">
      <div class="preview-section">
        <div class="chart-title">
          {{ generalWidgetData.title }}
        </div>

        <component
          :is="snakeToPascal(widgetName)"
          :volume="widgetData"
          :chart-type="newChartType || chartType"
          :is-general-widget="false"
          :is-open-widget="true"
          :project-id="projectId"
          :widgets="widgetsList"
        />
      </div>

      <div class="general-wrapper-settings">
        <SettingsButtons @update-setting-panel="updateSettingPanel" />

        <BasicSettingsScreen
          v-if="panelName === 'General'"
          :period="generalWidgetData.aggregation_period"
          :widget-title="generalWidgetData.title"
          :widget-description="generalWidgetData.description"
          :hasAggregationPeriod="hasAggregationPeriod"
          @save-changes="saveChanges"
          @get-widget-params="updateAggregationPeriod"
        />

        <DimensionsScreen
          v-if="panelName === 'Dimensions'"
          :active-dimensions="generalWidgetData"
          :project-id="projectId"
          :widget-author="generalWidgetData.author_dim_pivot"
          :widget-country="generalWidgetData.country_dim_pivot"
          :widget-language="generalWidgetData.language_dim_pivot"
          @save-dimensions-settings="saveDimensions"
        />

        <ChartTypesRadio
          v-if="panelName === 'Chart Layout'"
          :selected="chartType"
          :widget-name="widgetName"
          @update-chart-type="updateChartType"
        />

        <BaseButton class="button" @click="saveChartType">
          <SaveIcon />Save Settings
        </BaseButton>
      </div>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {snakeToPascal} from '@/lib/utilities'

import BaseModal from '@/components/modals/BaseModal'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'
import VolumeWidget from '@/components/project/widgets/VolumeWidget'
import Top10LanguagesWidget from '@/components/project/widgets/Top10LanguagesWidget'
import Top10BrandsWidget from '@/components/project/widgets/Top10BrandsWidget'
import Top10CountriesWidget from '@/components/project/widgets/Top10CountriesWidget'
import Top10AuthorsByVolumeWidget from '@/components/project/widgets/Top10AuthorsByVolumeWidget'
import ContentVolumeTop5SourceWidget from '@/components/project/widgets/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/project/widgets/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/project/widgets/ContentVolumeTop5CountriesWidget'
import SentimentTop10SourcesWidget from '@/components/project/widgets/SentimentTop10SourcesWidget'
import SentimentTop10CountriesWidget from '@/components/project/widgets/SentimentTop10CountriesWidget'
import SentimentTop10AuthorsWidget from '@/components/project/widgets/SentimentTop10AuthorsWidget'
import SentimentTop10LanguagesWidget from '@/components/project/widgets/SentimentTop10LanguagesWidget'
import SentimentForPeriodWidget from '@/components/project/widgets/SentimentForPeriodWidget'
import ChartTypesRadio from '@/components/project/widgets/modals/screens/ChartTypesRadio'
import BaseButton from '@/components/buttons/BaseButton'
import SaveIcon from '@/components/icons/SaveIcon'

export default {
  name: 'WidgetSettingsModal',
  components: {
    SaveIcon,
    BaseButton,
    ChartTypesRadio,
    BaseModal,
    VolumeWidget,
    SettingsButtons,
    DimensionsScreen,
    BasicSettingsScreen,
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
  },
  props: {
    widgetName: {
      type: String,
      required: true,
    },
    projectId: {
      type: Number,
      required: true,
    },
    widgetData: {
      type: Object,
      default: () => {},
    },
    actionName: {
      type: String,
      required: true,
    },
    hasAggregationPeriod: {
      type: Boolean,
      default: true,
    },
    chartType: {
      type: String,
      required: false,
    },
    widgetsList: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      panelName: 'Chart Layout',
      newChartType: '',
    }
  },
  computed: {
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
    }),
    generalWidgetData() {
      return this.widgets[this.widgetName]
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
    ]),
    snakeToPascal,
    formatDate(date) {
      return new Date(date).toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    updateAggregationPeriod(val) {
      try {
        this[this.actionName]({
          projectId: this.projectId,
          value: {
            aggregation_period: val.toLowerCase(),
            author_dim_pivot: this.generalWidgetData.author_dim_pivot || null,
            language_dim_pivot:
              this.generalWidgetData.language_dim_pivot || null,
            country_dim_pivot: this.generalWidgetData.country_dim_pivot || null,
            sentiment_dim_pivot:
              this.generalWidgetData.sentiment_dim_pivot || null,
            source_dim_pivot: this.generalWidgetData.source_dim_pivot || null,
          },
        })
      } catch (e) {
        console.log(e)
      }
    },
    saveChanges(title, description, aggregationPeriod) {
      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          [this.widgetName]: {
            id: this.generalWidgetData.id,
            title: title,
            description: description,
            aggregation_period: aggregationPeriod.toLowerCase(),
          },
        },
      })
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    updateSettingPanel(val) {
      this.panelName = val
    },
    saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.generalWidgetData.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.generalWidgetData.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.generalWidgetData.country_dim_pivot
      }

      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          [this.widgetName]: {
            id: this.generalWidgetData.id,
            aggregation_period: this.generalWidgetData.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.generalWidgetData.sentiment_dim_pivot,
            source_dim_pivot: this.generalWidgetData.source_dim_pivot,
          },
        },
      })
      this[this.actionName]({
        projectId: this.projectId,
        value: {
          id: this.generalWidgetData.id,
          aggregation_period: this.generalWidgetData.aggregation_period,
          author_dim_pivot: author,
          language_dim_pivot: language,
          country_dim_pivot: country,
          sentiment_dim_pivot: this.generalWidgetData.sentiment_dim_pivot,
          source_dim_pivot: this.generalWidgetData.source_dim_pivot,
        },
      })
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    updateChartType(item) {
      this.newChartType = item
    },

    async saveChartType() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          [this.widgetName]: {
            id: this.generalWidgetData.id,
            chart_type: this.newChartType,
          },
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-wrapper {
  display: flex;

  height: 100%;
  min-width: 100%;

  background-color: var(--background-primary-color);

  .preview-section {
    flex: 1;
    width: 50%;
    height: fit-content;
    margin: 24px;

    .chart-title {
      padding: 12px 20px;

      border-bottom: 1px solid var(--border-color);

      font-style: normal;
      font-weight: 500;
      font-size: 18px;
      line-height: 20px;
      color: var(--typography-title-color);
    }

    box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);
    border-radius: 8px;
    background: var(--background-secondary-color);
  }

  .general-wrapper-settings {
    display: flex;
    flex-direction: column;
    align-self: flex-end;
    flex: 0.7;

    padding: 24px;
    height: 100%;

    background-color: var(--background-secondary-color);

    .button {
      gap: 6px;
      align-self: flex-end;

      width: 144px;
      margin-top: 32px;
    }
  }
}
</style>
