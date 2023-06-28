<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widgetDetails="selectedWidgets[currentWidgetIndex].widgetDetails"
    @close="closeModal"
  />
  <div class="analytics-wrapper">
    <SearchResults
      :is-checkbox-clipping-widget="true"
      :clipping-content="clippingData"
      @show-results="updatePageAndPostsCounts"
      class="search-results"
    />
    <div v-if="availableWidgets" class="widgets-wrapper scroll">
      <div
        class="widget-item"
        v-for="(item, index) in displayedWidgets"
        :key="item.i"
      >
        <OnlineMainWidget
          :widgetDetails="item.widgetDetails"
          :style="`height: ${item.widgetDetails.height};`"
          @delete-widget="deleteWidget(item.widgetDetails.name)"
          @open-settings-modal="openModal(index)"
        />
        <BaseObserver
          v-if="index + 1 === displayedWidgets.length"
          @intersect="getItems"
        />
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {getWidgetDetails} from '@lib/utilities'
import {widgetsConfig} from '@/lib/configs/widgetsConfigs'

import SearchResults from '@/components/SearchResults'
import BaseObserver from '@/components/BaseObserver'

import WidgetSettingsModal from '@/components/widgets/online/modals/WidgetSettingsModal'
import OnlineMainWidget from '@/components/widgets/online/OnlineMainWidget'

export default {
  name: 'WidgetsView',
  components: {
    WidgetSettingsModal,
    SearchResults,
    OnlineMainWidget,
    BaseObserver,
  },
  emits: ['update-page'],
  props: {
    projectId: {type: Number, required: true},
    currentProject: {type: [Array, Object], required: false},
  },
  data() {
    return {
      layout: [],
      isOpenWidgetSettingsModal: false,
      currentWidgetIndex: 0,
      countDisplayedWidgets: 2,
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
          .map((widgetName) => {
            widgetsConfig.clipping_feed_content.height = this.clippingData
              .length
              ? '400px'
              : '150px'

            if (
              this.availableWidgets[widgetName].is_active &&
              widgetsConfig[widgetName]
            ) {
              return {
                widgetDetails: getWidgetDetails(
                  widgetName,
                  this.availableWidgets[widgetName],
                  this.projectId,
                  this.currentProject.source
                ),

                isReady: false,
              }
            }
          })
          .filter((widgets) => widgets)
      },
      set(val) {
        this.layout = val
      },
    },
    displayedWidgets() {
      return this.selectedWidgets.slice(0, this.countDisplayedWidgets)
    },
  },
  methods: {
    ...mapActions([action.UPDATE_AVAILABLE_WIDGETS]),
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
    },
    updatePageAndPostsCounts(page, posts) {
      this.$emit('update-page', page, posts)
    },
    openModal(widgetIndex) {
      this.currentWidgetIndex = widgetIndex
      this.isOpenWidgetSettingsModal = !this.isOpenWidgetSettingsModal
    },
    closeModal() {
      this.togglePageScroll(false)
      this.isOpenWidgetSettingsModal = false
    },
    getItems() {
      this.countDisplayedWidgets += 2
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
  flex-direction: column;
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
