<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widget-name="dataForWidgetModal.widgetName"
    :project-id="projectId"
    :widget-data="this[dataForWidgetModal.widgetName]"
    :action-name="dataForWidgetModal.actionName"
    :is-charts-show="dataForWidgetModal.isChartShow"
    :hasAggregationPeriod="dataForWidgetModal.hasAggregationPeriod"
    @close="closeModal"
  />

  <div class="analytics-wrapper">
    <SearchResults
      :is-show-calendar="false"
      :is-checkbox-clipping-widget="true"
      :currentProject="currentProject"
      :clipping-content="clippingData"
      :is-show-sorting-field="true"
      @update-page="updatePage"
      @update-posts-count="updatePosts"
      @add-sorting-value="addSortingValue"
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
          :summary-data="summary_widget"
          :volume="volume_widget"
          :project-id="projectId"
          :is-open-widget="item.isShow"
          :widgets="availableWidgets"
          :current-project="currentProject"
          @delete-widget="deleteWidget(item.name)"
          @open-settings-modal="openModal(item)"
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
import modalWidgetsConfig from '@/lib/configs/modalWidgetsConfig'

import SearchResults from '@/components/SearchResults'
import VolumeWidget from '@/components/project/widgets/VolumeWidget'
import SummaryWidget from '@/components/project/widgets/SummaryWidget'
import Top10BrandsWidget from '@/components/project/widgets/Top10BrandsWidget'
import Top10CountriesWidget from '@/components/project/widgets/Top10CountriesWidget'
import Top10LanguagesWidget from '@/components/project/widgets/Top10LanguagesWidget'
import SentimentForPeriodWidget from '@/components/project/widgets/SentimentForPeriodWidget'
import ClippingFeedContentWidget from '@/components/project/widgets/ClippingFeedContentWidget'
import Top10AuthorsByVolumeWidget from '@/components/project/widgets/Top10AuthorsByVolumeWidget'
import SentimentTop10AuthorsWidget from '@/components/project/widgets/SentimentTop10AuthorsWidget'
import SentimentTop10SourcesWidget from '@/components/project/widgets/SentimentTop10SourcesWidget'
import SentimentTop10LanguagesWidget from '@/components/project/widgets/SentimentTop10LanguagesWidget'
import SentimentTop10CountriesWidget from '@/components/project/widgets/SentimentTop10CountriesWidget'
import ContentVolumeTop5SourceWidget from '@/components/project/widgets/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/project/widgets/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/project/widgets/ContentVolumeTop5CountriesWidget'
import WidgetSettingsModal from '@/components/project/modals/WidgetSettingsModal'

export default {
  name: 'WidgetsView',
  components: {
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
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
  },
  emits: ['update-page', 'update-posts-count', 'set-sorting-value'],
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
      isOpenWidgetSettingsModal: false,
      dataForWidgetModal: {},
    }
  },
  created() {
    if (!this.availableWidgets) {
      this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    }

    if (!this.clippingData.length) {
      this[action.GET_CLIPPING_FEED_CONTENT_WIDGET](this.projectId)
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
                actionName: this.elementsValue[widgetName].actionName,
                isChartShow: this.elementsValue[widgetName].isChartShow,
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
        data: {[name]: {is_active: false, id: this.availableWidgets[name].id}},
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    },
    updatePage(page, posts) {
      this.$emit('update-page', page, posts)
    },
    updatePosts(page, posts) {
      this.$emit('update-posts-count', page, posts)
    },
    addSortingValue(value) {
      this.$emit('set-sorting-value', value)
    },
    openModal(item) {
      this.dataForWidgetModal = {
        widgetName: item.name,
        actionName: item.actionName,
        isChartShow: item.isChartShow,
        hasAggregationPeriod: item.hasAggregationPeriod,
      }
      this.isOpenWidgetSettingsModal = !this.isOpenWidgetSettingsModal
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

  .search-results {
    min-width: 50%;
  }
}
.widgets-wrapper {
  display: flex;
  gap: 30px;
  overflow: auto;

  min-width: 50%;
  max-height: 60vh;
  margin-top: 63px;

  .analytics-search-results {
    flex: 1;
  }

  .widget-item {
    top: -10px;

    min-width: 96%;
  }
}

@media screen and (max-width: 1000px) {
  .widgets-wrapper {
    margin-top: 105px;
  }
}
</style>
