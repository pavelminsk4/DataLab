<template>
  <BaseModal
    :title="widgetDetails.title"
    :is-general-padding="false"
    style="--base-modal-content-padding: 0px"
  >
    <div class="settings-wrapper">
      <MainWidget
        v-if="item.isWidget"
        :widgetDetails="item.widgetDetails"
        :chart-type="newChartType || chartType"
        class="widget-view"
        @open-interactive-data="openInteractiveData"
        @open-sentiment-interactive="openSentimentInteractiveData"
      />
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {snakeToPascal} from '@/lib/utilities'

import BaseModal from '@/components/modals/BaseModal'
import MainWidget from '@/components/widgets/online/MainWidget'

export default {
  name: 'WidgetSettingsModal',
  components: {
    BaseModal,
    MainWidget,
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
    currentProject: {
      type: [Array, Object],
      required: false,
    },
    settingsTabs: {
      type: Array,
      required: true,
    },
    availableWidgets: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      panelName: 'General',
      newWidgetTitle: '',
      newWidgetDescription: '',
      newChartType: '',
    }
  },
  computed: {
    ...mapGetters({
      selectedDimensions: get.SELECTED_DIMENSIONS,
    }),
    generalWidgetData() {
      return this.availableWidgets[this.widgetName]
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
    updateSettingPanel(val) {
      this.panelName = val
    },

    updateGeneralSettings(value, optionName) {
      this[optionName] = value
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
          widgetId: this.generalWidgetData.id,
        })
      } catch (e) {
        console.log(e)
      }
    },

    saveGeneralChanges() {
      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        widgetsList: {
          [this.widgetName]: {
            id: this.generalWidgetData.id,
            title: this.newWidgetTitle || this.generalWidgetData.title,
            description: this.newWidgetDescription,
            aggregation_period: this.generalWidgetData.aggregation_period,
          },
        },
      })
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    },

    async saveDimensionsForWidget() {
      await this[action.POST_DIMENSIONS_FOR_WIDGET]({
        projectId: this.projectId,
        widgetId: this.generalWidgetData.id,
        data: {
          smpl_freq: this.generalWidgetData.aggregation_period,
          author_dim_pivot: this.selectedDimensions.authors,
          language_dim_pivot: this.selectedDimensions.languages,
          country_dim_pivot: this.selectedDimensions.countries,
          sentiment_dim_pivot: this.selectedDimensions.sentiments,
          source_dim_pivot: this.selectedDimensions.sources,
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)

      await this[this.actionName]({
        projectId: this.projectId,
        value: {
          smpl_freq: 'day',
          author_dim_pivot: this.generalWidgetData.author_dim_pivot || null,
          language_dim_pivot: this.generalWidgetData.language_dim_pivot || null,
          country_dim_pivot: this.generalWidgetData.country_dim_pivot || null,
          sentiment_dim_pivot:
            this.generalWidgetData.sentiment_dim_pivot || null,
          source_dim_pivot: this.generalWidgetData.source_dim_pivot || null,
        },
        widgetId: this.generalWidgetData.id,
      })
    },

    async saveChartType() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        widgetsList: {
          [this.widgetName]: {
            id: this.generalWidgetData.id,
            chart_type: this.newChartType,
          },
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    },

    saveChanges() {
      if (this.panelName === 'General') return this.saveGeneralChanges()
      if (this.panelName === 'Dimensions') return this.saveDimensionsForWidget()
      if (this.panelName === 'Chart Layout') return this.saveChartType()
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

<style lang="scss" scoped>
.settings-wrapper {
  display: flex;

  min-height: 660px;

  background-color: var(--background-primary-color);

  .preview-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex: 1;

    height: fit-content;
    min-height: 300px;
    margin: 24px;

    .chart-title {
      width: 100%;
      padding: 12px 20px;

      border-bottom: 1px solid var(--border-color);

      font-style: normal;
      font-weight: 500;
      font-size: 18px;
      line-height: 20px;
      color: var(--typography-title-color);
    }

    .widget-view {
      width: 95%;
    }

    box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);
    border-radius: 8px;
    background: var(--background-secondary-color);
  }

  .general-wrapper-settings {
    display: flex;
    flex-direction: column;
    flex: 1;

    padding: 24px;
    min-height: 100%;

    background-color: var(--background-secondary-color);

    .dimensions-tab {
      margin-top: 35px;
    }

    .button {
      gap: 6px;
      align-self: flex-end;

      width: 84px;
      margin-top: 32px;
    }
  }
}
</style>
