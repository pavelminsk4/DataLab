<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widgetDetails="currentWidget"
    @close="closeModal"
    @open-interactive-widget="openInteractiveData"
    @open-sentiment-interactive="openSentimentInteractiveData"
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
      <MainWidget
        v-if="item.isWidget"
        :widgetDetails="item.widgetDetails"
        @delete-widget="deleteWidget(item.name)"
        @open-settings-modal="openModal(item.widgetDetails)"
        @open-interactive-data="openInteractiveData"
        @open-sentiment-interactive="openSentimentInteractiveData"
      />
    </grid-item>
  </grid-layout>

  <div v-else class="widgets-wrapper"></div>
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'
import {action} from '@store/constants'
import VueGridLayout from 'vue3-grid-layout'
import {getWidgetDetails} from '@lib/utilities'
import {widgetsConfig} from '@/lib/configs/widgetsConfigs'

import MainWidget from '@/components/widgets/online/MainWidget'
import WidgetSettingsModal from '@/components/widgets/modals/WidgetSettingsModal'

const {mapActions} = createNamespacedHelpers('social')

export default {
  name: 'WidgetsView',
  components: {
    MainWidget,
    WidgetSettingsModal,
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
  },
  emits: [
    'set-sorting-value',
    'open-interactive-widget',
    'update-available-widgets',
  ],
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
      currentWidget: null,
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
        return Object.keys(this.availableWidgets)
          .map((widgetName, index) => {
            if (this.availableWidgets[widgetName].is_active) {
              const configWidgetName = `${widgetName}_widget`

              widgetsConfig.clipping_feed_content_widget.height = this
                .clippingData.length
                ? 13
                : 3.8

              return {
                x: 0,
                y: this.getYAxisValue(index + 1),
                w: 2,
                h: this.widgetsConfig[configWidgetName].height,
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
      this.$emit('update-available-widgets', {
        projectId: this.projectId,
        widgetsList: {
          [name]: {is_active: false, id: this.availableWidgets[name].id},
        },
      })
    },
    updatePage(page, posts) {
      this.$emit('update-page', page, posts)
    },
    openModal(widget) {
      this.currentWidget = widget
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
