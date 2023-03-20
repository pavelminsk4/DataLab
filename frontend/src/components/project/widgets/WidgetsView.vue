<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widgetData="currentWidget"
    :widget-modal-data="dataForWidgetModal"
    :project-id="projectId"
    :current-project="currentProject"
    @close="closeModal"
    @open-interactive-widget="openInteractiveData"
    @open-sentiment-interactive="openSentimentInteractiveData"
  />
  <div class="analytics-wrapper">
    <SearchResults
      :is-show-calendar="false"
      :is-checkbox-clipping-widget="true"
      :currentProject="currentProject"
      :clipping-content="clippingData"
      @update-page="updatePage"
      @update-posts-count="updatePosts"
      class="search-results"
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
          :project-id="projectId"
          :is-open-widget="item.isShow"
          :widgets="availableWidgets"
          :widget-id="item.widgetId"
          :current-project="currentProject"
          :chart-type="item.chartType"
          :title="item.title"
          :available-widgets="availableWidgets"
          @delete-widget="deleteWidget(item.name)"
          @open-settings-modal="openModal(item)"
          @open-interactive-data="openInteractiveData"
          @open-sentiment-interactive="openSentimentInteractiveData"
        />
      </grid-item>
    </grid-layout>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import VueGridLayout from 'vue3-grid-layout'
import {snakeToPascal} from '@lib/utilities'
import {modalWidgetsConfig} from '@/lib/configs/widgetsConfigs'

import SummaryWidget from '@/components/widgets/online/SummaryWidget'
import SearchResults from '@/components/SearchResults'
import VolumeWidget from '@/components/widgets/online/VolumeWidget'
import Top10BrandsWidget from '@/components/widgets/online/Top10BrandsWidget'
import Top10CountriesWidget from '@/components/widgets/online/Top10CountriesWidget'
import Top10LanguagesWidget from '@/components/widgets/online/Top10LanguagesWidget'
import Top10AuthorsByVolumeWidget from '@/components/widgets/online/Top10AuthorsByVolumeWidget'
import SentimentForPeriodWidget from '@/components/widgets/online/SentimentForPeriodWidget'
import ClippingFeedContentWidget from '@/components/widgets/online/ClippingFeedContentWidget'
import SentimentTop10AuthorsWidget from '@/components/widgets/online/SentimentTop10AuthorsWidget'
import SentimentTop10SourcesWidget from '@/components/widgets/online/SentimentTop10SourcesWidget'
import SentimentTop10LanguagesWidget from '@/components/widgets/online/SentimentTop10LanguagesWidget'
import SentimentTop10CountriesWidget from '@/components/widgets/online/SentimentTop10CountriesWidget'
import ContentVolumeTop5SourceWidget from '@/components/widgets/online/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/widgets/online/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/widgets/online/ContentVolumeTop5CountriesWidget'
import TopKeywords from '@/components/widgets/online/TopKeywordsWidget'
import WidgetSettingsModal from '@/components/widgets/online/modals/WidgetSettingsModal'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'

export default {
  name: 'WidgetsView',
  components: {
    InteractiveWidgetModal,
    WidgetSettingsModal,
    SearchResults,
    ClippingFeedContentWidget,
    VolumeWidget,
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
    TopKeywords,
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
  },
  emits: [
    'update-page',
    'update-posts-count',
    'set-sorting-value',
    'open-interactive-widget',
    'open-sentiment-interactive-widget',
  ],
  props: {
    projectId: {type: Number, required: true},
    currentProject: {type: [Array, Object], required: false},
  },
  data() {
    return {
      layout: [],
      dataForWidgetModal: {},
      isOpenWidgetSettingsModal: false,
      currentWidget: null,
    }
  },
  async created() {
    if (!this.availableWidgets) {
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    }

    if (!this.clippingData.length) {
      await this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
        projectId: this.projectId,
        widgetId: this.availableWidgets.clipping_feed_content_widget.id,
      })
    }
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
    selectedWidgets: {
      get() {
        let layout = []
        Object.keys(this.availableWidgets)
          .map((widgetName, index) => {
            if (this.availableWidgets[widgetName]?.is_active) {
              return layout.push({
                x: 0,
                y: this.getYAxisValue(layout.length),
                w: 2,
                h: this.elementsValue[widgetName].height,
                i: index,
                static: false,
                name: widgetName,
                widgetName: snakeToPascal(widgetName),
                isShow: this.availableWidgets[widgetName]?.is_active,
                isWidget: true,
                widgetId: this.availableWidgets[widgetName]?.id,
                actionName: this.elementsValue[widgetName].actionName,
                isChartShow: this.elementsValue[widgetName].isChartShow,
                title: this.availableWidgets[widgetName]?.title,
                chartType:
                  this.availableWidgets[widgetName]?.chart_type ||
                  modalWidgetsConfig[widgetName]?.defaultChartType,
                hasAggregationPeriod:
                  this.elementsValue[widgetName].hasAggregationPeriod,
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
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        widgetsList: {
          [name]: {is_active: false, id: this.availableWidgets[name].id},
        },
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    },
    updatePage(page, posts) {
      this.$emit('update-page', page, posts)
    },
    updatePosts(page, posts) {
      this.$emit('update-posts-count', page, posts)
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
      this.currentWidget = this.availableWidgets[item.name]
      this.isOpenWidgetSettingsModal = !this.isOpenWidgetSettingsModal
    },
    openInteractiveData(val, widgetId, fieldName) {
      this.$emit('open-interactive-widget', val, widgetId, fieldName)
    },
    openSentimentInteractiveData(source, sentiment, widgetId) {
      this.$emit(
        'open-sentiment-interactive-widget',
        source,
        sentiment,
        widgetId
      )
    },
    closeModal() {
      this.togglePageScroll(false)
      this.isOpenWidgetSettingsModal = false
    },
  },
}
</script>

<style lang="scss" scoped>
.analytics-wrapper {
  display: flex;
  gap: 40px;

  height: 100%;
  margin-top: 20px;

  .search-results {
    width: 100%;
    height: calc(100vh - 255px);
  }
}
.widgets-wrapper {
  display: flex;
  gap: 30px;
  overflow: auto;

  width: 100%;
  max-height: calc(100vh - 255px);

  .analytics-search-results {
    flex: 1;
  }

  .widget-item {
    top: -10px;

    min-width: 96%;
  }
}
</style>
