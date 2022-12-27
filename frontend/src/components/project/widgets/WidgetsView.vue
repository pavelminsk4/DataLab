<template>
  <component
    :is="currentSettingsModal"
    v-if="isOpenModalSettings"
    :project-id="projectId"
    :volume="volumeWidget"
    :sentiment-for-period-value="sentimentForPeriodWidget"
    @close="closeModal()"
  />

  <div v-if="availableWidgets" class="widgets-wrapper">
    <SearchResults
      :is-show-calendar="false"
      :is-checkbox-clipping-widget="true"
      :currentProject="currentProject"
      :clipping-content="clippingData"
      @update-page="updatePage"
      @update-posts-count="updatePosts"
      class="analytics-search-results"
    />

    <div class="widget-items scroll">
      <div
        class="widget-item"
        v-for="item in selectedWidgets"
        v-show="item.isShow"
        :key="item.name"
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
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

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
import ContentVolumeTop10SourceWidget from '@/components/project/widgets/ContentVolumeTop10SourceWidget'
import ContentVolumeTop10AuthorsWidget from '@/components/project/widgets/ContentVolumeTop10AuthorsWidget'
import ContentVolumeTop10CountriesWidget from '@/components/project/widgets/ContentVolumeTop10CountriesWidget'

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
import ContentVolumeTop10SourceWidgetModal from '@/components/project/widgets/modals/ContentVolumeTop10SourceWidgetModal'
import ContentVolumeTop10AuthorsWidgetModal from '@/components/project/widgets/modals/ContentVolumeTop10AuthorsWidgetModal'
import ContentVolumeTop10CountriesWidgetModal from '@/components/project/widgets/modals/ContentVolumeTop10CountriesWidgetModal'

import {snakeToPascal} from '@lib/utilities'

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
    ContentVolumeTop10SourceWidgetModal,
    ContentVolumeTop10AuthorsWidgetModal,
    ContentVolumeTop10CountriesWidgetModal,
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
    ContentVolumeTop10SourceWidget,
    ContentVolumeTop10AuthorsWidget,
    ContentVolumeTop10CountriesWidget,
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
    currentSettingsModal() {
      return this.isOpenModalSettings
    },
    selectedWidgets() {
      return Object.keys(this.availableWidgets)
        .map((widgetName) => {
          if (this.availableWidgets[widgetName].is_active) {
            return {
              name: widgetName,
              widgetName: snakeToPascal(widgetName),
              isShow: this.availableWidgets[widgetName]?.is_active,
              isOpenModal: snakeToPascal(widgetName) + 'Modal',
              isWidget: true,
            }
          }
        })
        .filter((widgets) => widgets)
    },
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
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
      this.isOpenModalSettings = null
    },
  },
}
</script>

<style lang="scss" scoped>
.widgets-wrapper {
  display: flex;
  gap: 30px;

  min-width: 100%;
  margin-top: 30px;

  .analytics-search-results {
    flex: 1;
  }

  .widget-items {
    display: flex;
    flex: 1;
    flex-direction: column;
    gap: 20px;

    height: 1000px;
    padding-right: 20px;
    margin-top: 45px;

    overflow: auto;
  }
}
</style>
