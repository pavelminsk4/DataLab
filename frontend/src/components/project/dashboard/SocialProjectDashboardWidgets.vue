<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widget-name="dataForWidgetModal.widgetName"
    :project-id="projectId"
    :widget-data="this[dataForWidgetModal.widgetName]"
    :action-name="dataForWidgetModal.actionName"
    :is-charts-show="dataForWidgetModal.isChartShow"
    :hasAggregationPeriod="dataForWidgetModal.hasAggregationPeriod"
    :chart-type="dataForWidgetModal.chartType"
    :widgets-list="availableWidgets"
    :current-project="currentProject"
    :summary-data="summary_widget"
    :settings-tabs="dataForWidgetModal.settingsTabs"
    @close="closeModal"
    @open-interactive-widget="openInteractiveData"
  />

  <grid-layout
    v-if="availableWidgets"
    v-model:layout="selectedWidgets"
    :col-num="4"
    :row-height="30"
    :is-resizable="false"
    is-draggable
    vertical-compact
    use-css-transforms
    class="widgets-wrapper scroll"
  >
    <grid-item
      class="widget-item"
      v-for="item in selectedWidgets"
      :static="item.static"
      :x="item.x"
      :y="item.y"
      :w="item.w"
      :h="item.h"
      :i="item.i"
      :key="item.i"
    >
      <component
        v-if="item.isWidget"
        :is="item.widgetName"
        :summary-data="summary_widget"
        :volume="volume_widget"
        :project-id="projectId"
        :is-open-widget="item.isShow"
        :widgets="availableWidgets"
        :widget-id="item.widgetId"
        :current-project="currentProject"
        :chart-type="item.chartType"
        @delete-widget="deleteWidget(item.name)"
        @open-settings-modal="openModal(item)"
        @open-interactive-data="openInteractiveData"
      />
    </grid-item>
  </grid-layout>

  <div v-else class="widgets-wrapper"></div>
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'
import {action} from '@store/modules/social/constants'
import VueGridLayout from 'vue3-grid-layout'
import {snakeToPascal} from '@lib/utilities'
import {modalWidgetsConfig} from '@/lib/configs/widgetsConfigs'

import ContentVolume from '@/components/project/widgets/SocialContentVolumeWidget'
import SummaryWidget from '@/components/project/widgets/SocialSummaryWidget'
import Top10BrandsWidget from '@/components/project/widgets/Top10BrandsWidget'
import Top10CountriesWidget from '@/components/project/widgets/Top10CountriesWidget'
import Top10LanguagesWidget from '@/components/project/widgets/Top10LanguagesWidget'
import SentimentForPeriodWidget from '@/components/project/widgets/SentimentForPeriodWidget'
import ClippingFeedContent from '@/components/project/widgets/SocialClippingFeedContentWidget'
import Top10AuthorsByVolumeWidget from '@/components/project/widgets/Top10AuthorsByVolumeWidget'
import SentimentTop10AuthorsWidget from '@/components/project/widgets/SentimentTop10AuthorsWidget'
import SentimentTop10SourcesWidget from '@/components/project/widgets/SentimentTop10SourcesWidget'
import SentimentTop10LanguagesWidget from '@/components/project/widgets/SentimentTop10LanguagesWidget'
import SentimentTop10CountriesWidget from '@/components/project/widgets/SentimentTop10CountriesWidget'
import ContentVolumeTop5SourceWidget from '@/components/project/widgets/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/project/widgets/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/project/widgets/ContentVolumeTop5CountriesWidget'
import WidgetSettingsModal from '@/components/project/modals/WidgetSettingsModal'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'

const {mapActions} = createNamespacedHelpers('social')

export default {
  name: 'WidgetsView',
  components: {
    InteractiveWidgetModal,
    WidgetSettingsModal,
    ClippingFeedContent,
    ContentVolume,
    SummaryWidget,
    Top10BrandsWidget,
    Top10CountriesWidget,
    Top10LanguagesWidget,
    SentimentForPeriodWidget,
    Top10AuthorsByVolumeWidget,
    SentimentTop10AuthorsWidget,
    SentimentTop10SourcesWidget,
    SentimentTop10LanguagesWidget,
    SentimentTop10CountriesWidget,
    ContentVolumeTop5SourceWidget,
    ContentVolumeTop5AuthorsWidget,
    ContentVolumeTop5CountriesWidget,
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
  },
  emits: ['set-sorting-value', 'open-interactive-widget'],
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  data() {
    return {
      layout: [],
      dataForWidgetModal: {},
      isOpenWidgetSettingsModal: false,
    }
  },
  computed: {
    ...mapGetters({
      summary_widget: get.SUMMARY_WIDGET,
      volume_widget: get.VOLUME_WIDGET,
      sentimentForPeriodWidget: get.SENTIMENT_FOR_PERIOD,
      availableWidgets: get.AVAILABLE_WIDGETS,
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
    selectedWidgets: {
      get() {
        let layout = []

        Object.keys(this.availableWidgets)
          .map((widgetName, index) => {
            if (this.availableWidgets[widgetName].is_active) {
              const configWidgetName =
                widgetName === 'summary_widget'
                  ? widgetName
                  : `${widgetName}_widget`

              return layout.push({
                x: 0,
                y: this.getYAxisValue(layout.length),
                w: 2,
                h: this.elementsValue[configWidgetName].height,
                i: index,
                static: false,
                name: widgetName,
                widgetName: snakeToPascal(widgetName),
                isShow: this.availableWidgets[widgetName]?.is_active,
                isWidget: true,
                widgetId: this.availableWidgets[widgetName]?.id,
                actionName: this.elementsValue[configWidgetName].actionName,
                isChartShow: this.elementsValue[configWidgetName].isChartShow,
                chartType:
                  this.availableWidgets[widgetName]?.chart_type ||
                  modalWidgetsConfig[configWidgetName]?.defaultChartType,
                hasAggregationPeriod:
                  this.elementsValue[configWidgetName].hasAggregationPeriod,
              })
            }
          })
          .filter((widgets) => widgets)

        return layout
      },
      set(val) {
        this.layout = val
      },
    },
    elementsValue() {
      let widgetsElements = modalWidgetsConfig
      widgetsElements.clipping_feed_content_widget.height = this.clippingData
        .length
        ? 13
        : 3.8
      return widgetsElements
    },
  },
  async created() {
    if (
      !this.clippingData.length &&
      this.availableWidgets?.clipping_feed_content
    ) {
      await this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
        projectId: this.projectId,
        widgetId: this.availableWidgets.clipping_feed_content.id,
      })
    }
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
    getYAxisValue(val) {
      return val > 1 ? val - 1 : 0
    },
    async deleteWidget(name) {
      this.$emit('update-selected-widgets', {
        [name]: {is_active: false, id: this.availableWidgets[name].id},
      })
    },
    updatePage(page, posts) {
      this.$emit('update-page', page, posts)
    },
    openModal(item) {
      this.dataForWidgetModal = {
        widgetName: item.name,
        actionName: item.actionName,
        isChartShow: item.isChartShow,
        hasAggregationPeriod: item.hasAggregationPeriod,
        chartType: item.chartType,
        settingsTabs: modalWidgetsConfig[item.name].settingsTabs,
      }
      this.isOpenWidgetSettingsModal = !this.isOpenWidgetSettingsModal
    },
    openInteractiveData(val, widgetId, fieldName) {
      this.$emit('open-interactive-widget', val, widgetId, fieldName)
    },
    closeModal() {
      this.togglePageScroll(false)
      this.isOpenWidgetSettingsModal = false
    },
  },
}
</script>

<style lang="scss" scoped>
.widgets-wrapper {
  display: flex;
  gap: 30px;
  overflow: auto;

  width: 100%;
  max-height: calc(100vh - 255px);

  .widget-item {
    top: -10px;

    min-width: 96%;
  }
}
</style>
