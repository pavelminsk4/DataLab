<template>
  <component
    :is="currentSettingsModal"
    v-if="isOpenModalSettings"
    :project-id="projectId"
    :volume="volumeWidget"
    :sentiment-for-period-value="sentimentForPeriodWidget"
    @close="closeModal"
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
          :summary-data="summary"
          :volume="volumeWidget"
          :project-id="projectId"
          :is-open-widget="item.isShow"
          :widgets="availableWidgets"
          :current-project="currentProject"
          @delete-widget="deleteWidget(item.name)"
          @open-settings-modal="openModal(item.isOpenModal)"
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

import VolumeWidgetModal from '@/components/project/widgets/modals/VolumeWidgetModal'
import SummaryWidgetModal from '@/components/project/widgets/modals/SummaryWidgetModal'
import Top10BrandsWidgetModal from '@/components/project/widgets/modals/Top10BrandsWidgetModal'
import Top10CountriesWidgetModal from '@/components/project/widgets/modals/Top10CountriesWidgetModal'
import Top10LanguagesWidgetModal from '@/components/project/widgets/modals/Top10LanguagesWidgetModal'
import SentimentForPeriodWidgetModal from '@/components/project/widgets/modals/SentimentForPeriodWidgetModal'
import ClippingFeedContentWidgetModal from '@/components/project/widgets/modals/ClippingFeedContentWidgetModal'
import Top10AuthorsByVolumeWidgetModal from '@/components/project/widgets/modals/Top10AuthorsByVolumeWidgetModal'
import SentimentTop10SourcesWidgetModal from '@/components/project/widgets/modals/SentimentTop10SourcesWidgetModal'
import SentimentTop10AuthorsWidgetModal from '@/components/project/widgets/modals/SentimentTop10AuthorsWidgetModal'
import SentimentTop10CountriesWidgetModal from '@/components/project/widgets/modals/SentimentTop10CountriesWidgetModal'
import SentimentTop10LanguagesWidgetModal from '@/components/project/widgets/modals/SentimentTop10LanguagesWidgetModal'
import ContentVolumeTop5SourceWidgetModal from '@/components/project/widgets/modals/ContentVolumeTop5SourceWidgetModal'
import ContentVolumeTop5AuthorsWidgetModal from '@/components/project/widgets/modals/ContentVolumeTop5AuthorsWidgetModal'
import ContentVolumeTop5CountriesWidgetModal from '@/components/project/widgets/modals/ContentVolumeTop5CountriesWidgetModal'

export default {
  name: 'WidgetsView',
  components: {
    SearchResults,
    VolumeWidgetModal,
    SummaryWidgetModal,
    Top10BrandsWidgetModal,
    Top10CountriesWidgetModal,
    Top10LanguagesWidgetModal,
    ClippingFeedContentWidget,
    SentimentForPeriodWidgetModal,
    ClippingFeedContentWidgetModal,
    Top10AuthorsByVolumeWidgetModal,
    SentimentTop10SourcesWidgetModal,
    SentimentTop10AuthorsWidgetModal,
    SentimentTop10CountriesWidgetModal,
    SentimentTop10LanguagesWidgetModal,
    ContentVolumeTop5SourceWidgetModal,
    ContentVolumeTop5AuthorsWidgetModal,
    ContentVolumeTop5CountriesWidgetModal,
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
  emits: ['update-page', 'update-posts-count'],
  data() {
    return {
      layout: [],
      isOpenModalSettings: null,
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
      summary: get.SUMMARY_WIDGET,
      volumeWidget: get.VOLUME_WIDGET,
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
                h: this.getElementHeight(widgetName),
                i: index,
                static: false,
                name: widgetName,
                widgetName: snakeToPascal(widgetName),
                isShow: this.availableWidgets[widgetName]?.is_active,
                isOpenModal: snakeToPascal(widgetName) + 'Modal',
                isWidget: true,
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
    currentSettingsModal() {
      return this.isOpenModalSettings
    },
    gridElementsHeight() {
      return {
        summary_widget: 9,
        volume_widget: 15,
        clipping_feed_content_widget: 12,
        top_10_authors_by_volume_widget: 13,
        top_10_brands_widget: 13,
        top_10_countries_widget: 13,
        top_10_languages_widget: 13,
        sentiment_top_10_sources_widget: 12,
        sentiment_top_10_countries_widget: 12,
        sentiment_top_10_authors_widget: 12,
        sentiment_top_10_languages_widget: 12,
        sentiment_for_period_widget: 12,
        content_volume_top_5_authors_widget: 12,
        content_volume_top_5_countries_widget: 12,
        content_volume_top_5_source_widget: 12,
      }
    },
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
    getElementHeight(widgetName) {
      return this.gridElementsHeight[widgetName]
    },
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
    openModal(modalName) {
      this.isOpenModalSettings = modalName
    },
    closeModal() {
      this.togglePageScroll(false)
      this.isOpenModalSettings = null
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

  min-width: 50%;
  max-height: 1000px;
  margin-top: 30px;

  overflow: auto;

  .analytics-search-results {
    flex: 1;
  }

  .widget-item {
    min-width: 96%;
  }
}
</style>
