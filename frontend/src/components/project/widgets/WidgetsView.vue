<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widgetDetails="currentWidget"
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
        :key="item.i"
        :static="item.static"
        :x="item.x"
        :y="item.y"
        :w="item.w"
        :h="item.h"
        :i="item.i"
      >
        <MainWidget
          :widgetDetails="item.widgetDetails"
          @delete-widget="deleteWidget(item.widgetDetails.name)"
          @open-settings-modal="openModal(item.widgetDetails)"
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
import {getWidgetDetails} from '@lib/utilities'
import {widgetsConfig} from '@/lib/configs/widgetsConfigs'

import SearchResults from '@/components/SearchResults'

import WidgetSettingsModal from '@/components/widgets/online/modals/WidgetSettingsModal'
import MainWidget from '@/components/widgets/online/MainWidget'

export default {
  name: 'WidgetsView',
  components: {
    WidgetSettingsModal,
    SearchResults,
    MainWidget,
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
      isOpenWidgetSettingsModal: false,
      currentWidget: null,
    }
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
    selectedWidgets: {
      get() {
        return Object.keys(this.availableWidgets)
          .map((widgetName, index) => {
            widgetsConfig.clipping_feed_content_widget.height = this
              .clippingData.length
              ? 13
              : 3.8

            if (this.availableWidgets[widgetName].is_active) {
              return {
                x: 0,
                y: this.getYAxisValue(index + 1),
                w: 2,
                h: widgetsConfig[widgetName].height,
                i: index,
                static: false,

                widgetDetails: getWidgetDetails(
                  widgetName,
                  this.availableWidgets[widgetName],
                  this.projectId
                ),
              }
            }
          })
          .filter((widgets) => widgets)
      },
      set(val) {
        this.layout = val
      },
    },
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
    openModal(widget) {
      this.currentWidget = widget
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
