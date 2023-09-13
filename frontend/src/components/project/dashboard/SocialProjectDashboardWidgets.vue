<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widgetDetails="selectedWidgets[currentWidgetIndex].widgetDetails"
    @close="closeModal"
  />

  <div v-if="availableWidgets" class="widgets-wrapper scroll">
    <div
      v-for="(item, index) in displayedWidgets"
      :key="item.i"
      class="widget-item"
    >
      <SocialMainWidget
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

  <div v-else class="widgets-wrapper"></div>
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {getWidgetDetails} from '@lib/utilities'
import {widgetsConfig} from '@/lib/configs/widgetsConfigs'

import BaseObserver from '@/components/BaseObserver'
import SocialMainWidget from '@/components/widgets/social/SocialMainWidget'
import WidgetSettingsModal from '@/components/widgets/social/modals/WidgetSettingsModal'

const {mapActions, mapGetters: mapGettersSocial} =
  createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialProjectDashboardWidgets',
  components: {
    SocialMainWidget,
    WidgetSettingsModal,
    BaseObserver,
  },
  emits: [
    'set-sorting-value',
    'open-interactive-widget',
    'update-available-widgets',
    'open-sentiment-interactive-widget',
  ],
  props: {
    projectId: {type: Number, required: true},
    moduleName: {type: String, required: true},
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
    }),
    ...mapGettersSocial({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    clippingData() {
      return this.socialWidgets.clippingFeedContent
    },
    selectedWidgets: {
      get() {
        if (!this.availableWidgets) return
        return Object.keys(this.availableWidgets)
          .map((widgetName) => {
            if (
              this.availableWidgets[widgetName].is_active &&
              widgetsConfig[widgetName]
            ) {
              widgetsConfig.clipping_feed_content.height = this.clippingData
                .length
                ? '400px'
                : '150px'

              return {
                widgetDetails: getWidgetDetails(
                  widgetName,
                  this.availableWidgets[widgetName],
                  this.projectId,
                  this.moduleName
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
    displayedWidgets() {
      return this.selectedWidgets.slice(0, this.countDisplayedWidgets)
    },
  },
  async created() {
    const hasCurrentClippingData =
      this.clippingData?.length &&
      this.clippingData.id === this.availableWidgets.clipping_feed_content.id
    if (
      !hasCurrentClippingData &&
      this.availableWidgets?.clipping_feed_content
    ) {
      await this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
        projectId: this.projectId,
        widgetId: this.availableWidgets.clipping_feed_content.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_CLIPPING_FEED_CONTENT_WIDGET]),
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
.widgets-wrapper {
  display: flex;
  flex-direction: column;
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
